MIT License

Copyright (c) 2024 Snehasis5

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
##Columns and types:
'''
Country name                         object
year                                  int64
Life Ladder                         float64
Log GDP per capita                  float64
Social support                      float64
Healthy life expectancy at birth    float64
Freedom to make life choices        float64
Generosity                          float64
Perceptions of corruption           float64
Positive affect                     float64
Negative affect                     float64
Cluster                               int32

'''



##Summary Statistics
'''       Country name         year  Life Ladder  Log GDP per capita  Social support  Healthy life expectancy at birth  Freedom to make life choices   Generosity  Perceptions of corruption  Positive affect  Negative affect
count          2363  2363.000000  2363.000000         2335.000000     2350.000000                       2300.000000                   2327.000000  2282.000000                2238.000000      2339.000000      2347.000000
unique          165          NaN          NaN                 NaN             NaN                               NaN                           NaN          NaN                        NaN              NaN              NaN
top         Lebanon          NaN          NaN                 NaN             NaN                               NaN                           NaN          NaN                        NaN              NaN              NaN
freq             18          NaN          NaN                 NaN             NaN                               NaN                           NaN          NaN                        NaN              NaN              NaN
mean            NaN  2014.763860     5.483566            9.399671        0.809369                         63.401828                      0.750282     0.000098                   0.743971         0.651882         0.273151
std             NaN     5.059436     1.125522            1.152069        0.121212                          6.842644                      0.139357     0.161388                   0.184865         0.106240         0.087131
min             NaN  2005.000000     1.281000            5.527000        0.228000                          6.720000                      0.228000    -0.340000                   0.035000         0.179000         0.083000
25%             NaN  2011.000000     4.647000            8.506500        0.744000                         59.195000                      0.661000    -0.112000                   0.687000         0.572000         0.209000
50%             NaN  2015.000000     5.449000            9.503000        0.834500                         65.100000                      0.771000    -0.022000                   0.798500         0.663000         0.262000
75%             NaN  2019.000000     6.323500           10.392500        0.904000                         68.552500                      0.862000     0.093750                   0.867750         0.737000         0.326000
max             NaN  2023.000000     8.019000           11.676000        0.987000                         74.600000                      0.985000     0.700000                   0.983000         0.884000         0.705000
'''

##Missing Values
'''
Country name                          0
year                                  0
Life Ladder                           0
Log GDP per capita                   28
Social support                       13
Healthy life expectancy at birth     63
Freedom to make life choices         36
Generosity                           81
Perceptions of corruption           125
Positive affect                      24
Negative affect                      16
'''
#Narrative Report
Introduction
The dataset under analysis contains information related to various countries' well-being indicators over time, spanning from 2005 to 2023. It includes data on life satisfaction, economic indicators, social factors, and perceptions of various societal elements. This dataset is valuable for understanding how different countries compare on various factors that contribute to quality of life, economic prosperity, and social well-being. The data, analyzed across several columns, provides insights into the relationship between factors like GDP, social support, freedom of life choices, generosity, and perceptions of corruption.

Dataset Structure
The dataset consists of several columns, each representing a specific variable that contributes to the overall analysis. Below is a breakdown of the columns and their respective data types:

Country name: Categorical data type (object) representing the name of the country.
year: Numeric data type (int64) representing the year of observation, ranging from 2005 to 2023.
Life Ladder: Continuous data type (float64) that measures subjective well-being or life satisfaction, where higher values represent greater life satisfaction.
Log GDP per capita: Continuous data type (float64) that provides the logarithmic transformation of GDP per capita, a measure of the economic output per individual in a country.
Social support: Continuous data type (float64) measuring the level of social support, indicating how much people in a country feel they have support from others when needed.
Healthy life expectancy at birth: Continuous data type (float64) representing the number of years a newborn is expected to live in good health.
Freedom to make life choices: Continuous data type (float64) indicating the level of freedom individuals feel they have to make important decisions in life.
Generosity: Continuous data type (float64) representing people's tendency to be generous in their society, measured in terms of donations and volunteering.
Perceptions of corruption: Continuous data type (float64) that measures the perceived level of corruption in public institutions within a country, with higher values indicating greater perceived corruption.
Positive affect: Continuous data type (float64) measuring the frequency of positive emotions (like joy or pride) experienced by individuals in the country.
Negative affect: Continuous data type (float64) measuring the frequency of negative emotions (like sadness or anger) experienced by individuals in the country.
Cluster: Integer data type (int32) categorizing countries into groups based on similar characteristics, possibly related to their socio-economic conditions and well-being metrics.
Summary Statistics
The summary statistics reveal a range of insights about the overall distribution of the data:

Country Distribution:

The dataset covers 2363 records, including data from 165 unique countries, with Lebanon being the most frequent country in the dataset, occurring 18 times. This suggests Lebanon might have periodic data points or outlier observations compared to other countries.
Time Span:

The data spans from 2005 to 2023, with the average year being around 2014.76. This indicates a roughly consistent coverage of the years, providing a longitudinal view of the indicators.
Life Ladder:

The mean value for the Life Ladder (a measure of life satisfaction) is approximately 5.48, with a standard deviation of 1.13, indicating moderate variability across the countries. The life satisfaction score ranges from 1.28 (a low value indicating very low life satisfaction) to 8.02 (a high value indicating very high life satisfaction).
Log GDP per capita:

The average Log GDP per capita is 9.40, with a significant spread (standard deviation of 1.15). The logarithmic nature of the GDP per capita helps to normalize the values, avoiding extreme outliers caused by countries with very high GDPs. The range goes from 5.53 to 11.68, indicating considerable economic disparity between countries.
Social Support:

The mean value for Social support is 0.81, which suggests a relatively high level of social support across countries. The standard deviation of 0.12 indicates that there is some variation in how much social support is available across the countries.
Healthy Life Expectancy:

The average Healthy life expectancy at birth is 63.4 years, with a relatively wide range (from 6.72 years to 74.6 years). The variation suggests that health outcomes are heavily dependent on regional and socio-economic factors.
Freedom to Make Life Choices:

The Freedom to make life choices has a mean value of 0.75, with values ranging from 0.23 (indicating limited freedom) to 0.99 (indicating high freedom). This metric likely reflects the level of democracy, governance, and individual rights in different countries.
Generosity:

The Generosity score has a mean value close to 0.00, suggesting that most countries show no significant generosity. This is likely because generosity can vary widely and is dependent on local cultural norms. There is significant variance, as indicated by a high standard deviation of 0.16.
Perceptions of Corruption:

The Perceptions of corruption measure has an average value close to 0.74, with a wide range. The standard deviation of 0.18 reflects that perceptions of corruption vary substantially from country to country, with some countries perceiving high levels of corruption in their institutions.
Affective States:

The Positive affect and Negative affect columns, with means of 0.74 and 0.65, respectively, indicate the general emotional well-being of the population. Positive affect is slightly higher than negative affect on average, although the variability in both suggests some countries experience more emotional extremes than others.
Missing Data Analysis
The dataset also includes missing values, which require attention for any further analysis:

Log GDP per capita has 28 missing values, which is a notable gap, considering the importance of this variable in analyzing economic conditions.
Social support has 13 missing values.
Healthy life expectancy at birth has the highest number of missing values, with 63 records missing.
Freedom to make life choices and Generosity also have missing values (36 and 81, respectively), which might indicate difficulties in measuring these indicators in some countries.
Perceptions of corruption has 125 missing values, which may be due to the absence of specific corruption indices or surveys for certain countries in the dataset.
Positive affect and Negative affect have relatively fewer missing values (24 and 16, respectively), suggesting more consistent data collection for these measures.
Conclusion and Recommendations
The dataset provides a rich overview of well-being metrics across countries, offering valuable insights into how countries compare on key indicators such as life satisfaction, economic output, social support, and freedom. However, the presence of missing values, especially in variables like Log GDP per capita, Generosity, and Perceptions of corruption, could limit the robustness of any conclusions drawn from the data.

To improve the quality of the analysis, it would be beneficial to handle the missing data through imputation or other techniques, depending on the severity and pattern of the missingness. Additionally, further statistical analyses, such as correlation studies and regression models, could uncover the relationships between these indicators and identify drivers of well-being in different regions.

This dataset could be leveraged to assess policy changes, identify global trends, and develop recommendations for improving quality of life in various countries.
