import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests  # Using requests to send HTTP requests
import numpy as np
import chardet  # Library for detecting file encoding
from sklearn.cluster import KMeans

# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
        return result['encoding']

# Fetch the proxy token from environment variable
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")

if not AIPROXY_TOKEN:
    print("Error: AIPROXY_TOKEN environment variable not set.")
    sys.exit(1)

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: uv run autolysis.py <dataset.csv>")
    sys.exit(1)

dataset_path = sys.argv[1]

if not os.path.isfile(dataset_path):
    print(f"Error: File '{dataset_path}' does not exist.")
    sys.exit(1)

# Detect encoding and read the dataset
encoding = detect_encoding(dataset_path)
data = pd.read_csv(dataset_path, encoding=encoding)

# Check for missing values and dataset summary
missing_values = data.isnull().sum()
summary_stats = data.describe(include='all')

# Generate a correlation matrix (only for numerical columns)
numerical_data = data.select_dtypes(include=[np.number])
correlation_matrix = numerical_data.corr()

# Save correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")

# Define the save directory (change this as needed)
save_dir = os.getcwd()  # Save in the current working directory
os.makedirs(save_dir, exist_ok=True)  # Ensure the directory exists

heatmap_path = os.path.join(save_dir, "correlation_matrix.png")
plt.savefig(heatmap_path)
plt.close()

# Basic clustering with KMeans (only if sufficient numerical data exists)
pairplot_path = None
if len(numerical_data.columns) > 1:
    # Apply KMeans clustering with 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(numerical_data.fillna(0))

    # Save pairplot with clusters and color palette customization
    plt.figure(figsize=(10, 8))
    sns.pairplot(data, 
                 hue="Cluster",  # Use the 'Cluster' column as hue
                 diag_kind="hist",  # Use Kernel Density Estimation for diagonal plots
                 palette="dark",   # Set a more vibrant color palette
                 markers=["o", "s", "D"],  # Use different markers for each cluster
                 plot_kws={'alpha': 1},  # Set transparency for scatter points
                 height=3)  # Control the size of each facet

    # Save the enhanced pairplot as a PNG image
    pairplot_path = os.path.join(save_dir, "cluster_pairplot.png")
    plt.savefig(pairplot_path)
    plt.close()

# OpenAI Proxy API request
proxy_url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

def query_llm(prompt):
    headers = {
        'Authorization': f'Bearer {AIPROXY_TOKEN}',  # Using AIPROXY_TOKEN
        'Content-Type': 'application/json'
    }

    payload = {
        "model": "gpt-4o-mini",  # You can use any model here
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }

    try:
        response = requests.post(proxy_url, json=payload, headers=headers, timeout=30)  # Timeout after 30 seconds
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        print(f"Error querying LLM: {e}")
        return ""

# Prepare a summary of the dataset for the LLM
summary_prompt = f"The dataset has the following columns and types: {data.dtypes.to_dict()}\n\n"
summary_prompt += f"Here are the summary statistics:\n{summary_stats.to_string()}\n\n"
summary_prompt += f"Here are the missing values in each column:\n{missing_values.to_string()}\n\n"

if len(correlation_matrix.columns) > 1:
    summary_prompt += "Here is the correlation matrix for numerical data:\n"
    summary_prompt += correlation_matrix.to_string() + "\n\n"

llm_summary = query_llm(summary_prompt + "Write a narrative report based on this data. Comment analytically about the data, key insights and trends you can derive from the data by highlighting key findings and what are the implications of those insights (i.e what to do with the insights)")

# Check if llm_summary is empty
if not llm_summary.strip():
    llm_summary = "No narrative analysis available."

# Generate a markdown file
with open(os.path.join(save_dir, "README.md"), "w") as f:
    f.write("# Analysis Report\n\n")
    f.write("## Dataset Description\n\n")
    f.write(f"Columns and types:\n\n```\n{data.dtypes.to_string()}\n```\n\n")
    f.write("## Summary Statistics\n\n")
    f.write(f"```\n{summary_stats.to_string()}\n```\n\n")
    f.write("## Missing Values\n\n")
    f.write(f"```\n{missing_values.to_string()}\n```\n\n")
    
    if len(correlation_matrix.columns) > 1:
        f.write("## Correlation Matrix\n\n")
        f.write(f"![Correlation Matrix]({heatmap_path})\n\n")

    if pairplot_path:
        f.write("## Clustering Results\n\n")
        f.write(f"![Cluster Pairplot]({pairplot_path})\n\n")

    f.write("## Narrative Analysis\n\n")
    f.write(llm_summary + "\n")

print("Analysis complete. Check the README.md and generated PNG files.")
