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
# Analysis Report

## Dataset Description

Columns and types:

```
book_id                        int64
goodreads_book_id              int64
best_book_id                   int64
work_id                        int64
books_count                    int64
isbn                          object
isbn13                       float64
authors                       object
original_publication_year    float64
original_title                object
title                         object
language_code                 object
average_rating               float64
ratings_count                  int64
work_ratings_count             int64
work_text_reviews_count        int64
ratings_1                      int64
ratings_2                      int64
ratings_3                      int64
ratings_4                      int64
ratings_5                      int64
image_url                     object
small_image_url               object
Cluster                        int32
```

## Summary Statistics

```
            book_id  goodreads_book_id  best_book_id       work_id   books_count       isbn        isbn13       authors  original_publication_year original_title           title language_code  average_rating  ratings_count  work_ratings_count  work_text_reviews_count      ratings_1      ratings_2      ratings_3     ratings_4     ratings_5                                                                                 image_url                                                                         small_image_url
count   10000.00000       1.000000e+04  1.000000e+04  1.000000e+04  10000.000000       9300  9.415000e+03         10000                9979.000000           9415           10000          8916    10000.000000   1.000000e+04        1.000000e+04             10000.000000   10000.000000   10000.000000   10000.000000  1.000000e+04  1.000000e+04                                                                                     10000                                                                                   10000
unique          NaN                NaN           NaN           NaN           NaN       9300           NaN          4664                        NaN           9274            9964            25             NaN            NaN                 NaN                      NaN            NaN            NaN            NaN           NaN           NaN                                                                                      6669                                                                                    6669
top             NaN                NaN           NaN           NaN           NaN  439023483           NaN  Stephen King                        NaN                 Selected Poems           eng             NaN            NaN                 NaN                      NaN            NaN            NaN            NaN           NaN           NaN  https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png  https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png
freq            NaN                NaN           NaN           NaN           NaN          1           NaN            60                        NaN              5               4          6341             NaN            NaN                 NaN                      NaN            NaN            NaN            NaN           NaN           NaN                                                                                      3332                                                                                    3332
mean     5000.50000       5.264697e+06  5.471214e+06  8.646183e+06     75.712700        NaN  9.755044e+12           NaN                1981.987674            NaN             NaN           NaN        4.002191   5.400124e+04        5.968732e+04              2919.955300    1345.040600    3110.885000   11475.893800  1.996570e+04  2.378981e+04                                                                                       NaN                                                                                     NaN
std      2886.89568       7.575462e+06  7.827330e+06  1.175106e+07    170.470728        NaN  4.428619e+11           NaN                 152.576665            NaN             NaN           NaN        0.254427   1.573700e+05        1.678038e+05              6124.378132    6635.626263    9717.123578   28546.449183  5.144736e+04  7.976889e+04                                                                                       NaN                                                                                     NaN
min         1.00000       1.000000e+00  1.000000e+00  8.700000e+01      1.000000        NaN  1.951703e+08           NaN               -1750.000000            NaN             NaN           NaN        2.470000   2.716000e+03        5.510000e+03                 3.000000      11.000000      30.000000     323.000000  7.500000e+02  7.540000e+02                                                                                       NaN                                                                                     NaN
25%      2500.75000       4.627575e+04  4.791175e+04  1.008841e+06     23.000000        NaN  9.780316e+12           NaN                1990.000000            NaN             NaN           NaN        3.850000   1.356875e+04        1.543875e+04               694.000000     196.000000     656.000000    3112.000000  5.405750e+03  5.334000e+03                                                                                       NaN                                                                                     NaN
50%      5000.50000       3.949655e+05  4.251235e+05  2.719524e+06     40.000000        NaN  9.780452e+12           NaN                2004.000000            NaN             NaN           NaN        4.020000   2.115550e+04        2.383250e+04              1402.000000     391.000000    1163.000000    4894.000000  8.269500e+03  8.836000e+03                                                                                       NaN                                                                                     NaN
75%      7500.25000       9.382225e+06  9.636112e+06  1.451775e+07     67.000000        NaN  9.780831e+12           NaN                2011.000000            NaN             NaN           NaN        4.180000   4.105350e+04        4.591500e+04              2744.250000     885.000000    2353.250000    9287.000000  1.602350e+04  1.730450e+04                                                                                       NaN                                                                                     NaN
max     10000.00000       3.328864e+07  3.553423e+07  5.639960e+07   3455.000000        NaN  9.790008e+12           NaN                2017.000000            NaN             NaN           NaN        4.820000   4.780653e+06        4.942365e+06            155254.000000  456191.000000  436802.000000  793319.000000  1.481305e+06  3.011543e+06                                                                                       NaN                                                                                     NaN
```

## Missing Values

```
book_id                         0
goodreads_book_id               0
best_book_id                    0
work_id                         0
books_count                     0
isbn                          700
isbn13                        585
authors                         0
original_publication_year      21
original_title                585
title                           0
language_code                1084
average_rating                  0
ratings_count                   0
work_ratings_count              0
work_text_reviews_count         0
ratings_1                       0
ratings_2                       0
ratings_3                       0
ratings_4                       0
ratings_5                       0
image_url                       0
small_image_url                 0
```

## Correlation Matrix

![Correlation Matrix](correlation_matrix.png)

## Clustering Results

![Cluster Pairplot](cluster_pairplot.png)

## Narrative Analysis

### Narrative Report on Book Dataset Analysis

#### Overview

The dataset consists of 10,000 records related to books, encompassing various attributes such as book identifiers, authors, publication years, ratings, reviews, and image URLs. The analysis of this dataset provides valuable insights into trends relating to book popularity, ratings, authorship, and publication characteristics.

#### Key Insights

1. **Authors Representation**:
   - The dataset features a diverse authorship pool with a total of 4,664 unique authors. However, Stephen King is notably the most frequently listed author, appearing in 60 entries. This suggests that certain authors may cover a significant share of readership or that their works are more extensively cataloged.
   - The implication is twofold: publishers and marketing teams may want to consider working with prolific authors to boost visibility, while new authors may benefit from strategies to differentiate themselves in a saturated market.

2. **Rating Distribution**:
   - The average rating across the dataset is approximately 4.00, indicating that books generally receive favorable reviews. However, the ratings distribution, with notable counts in the 1 to 5 stars range�specifically, over 63% of books receive 4 or 5 stars�highlights a potential skew in user ratings, suggesting a preference for popular or critically acclaimed titles.
   - This trend implies that ratings could be influenced more by marketing strategies than content quality, guiding publishers to invest more in promotional efforts for lesser-known titles.

3. **Language Diversity**:
   - The `language_code` column shows a significant number of missing values (1,084 out of 10,000 entries). This suggests that a considerable portion of the dataset lacks language identification, which could inhibit comprehensive analysis on readership demographics or trends within specific language groups.
   - To address this, efforts to standardize and complete the language data would enhance analytical depth and potentially allow better localization and targeted marketing strategies.

4. **Correlations**:
   - A correlation analysis reveals significant relationships between the number of ratings (`ratings_count`, `work_ratings_count`) and the quality of ratings (average rating). Specifically, higher engagement in terms of ratings appears to correlate with more favorable ratings, highlighting the importance of reader interaction.
   - This suggests that boosting reader engagement (via innovative promotional strategies, social media integration, and community-building activities) could lead to improved ratings and overall book visibility.

5. **Publication Trends**:
   - The average year of original publication is around 1982, with books published as recently as 2017. This reveals a mix of newer titles alongside classic literature, suggesting that readers value both contemporary and traditional works. However, there are 21 entries with missing publication years, which could skew analyses.
   - Publishers could analyze popular books from earlier decades against newer releases to strategize reprints or discover opportunities within vintage literature to tap into nostalgia-based marketing.

6. **ISBN Coverage**:
   - The dataset reveals that 700 records and 585 records are missing ISBN and ISBN13 values, respectively. Given that ISBNs play a crucial role in book tracking and sales, the absence of these identifiers limits sales and inventory insights. 
   - Ensuring the ISBN data is complete can improve database functionality and aid in more effective inventory management while facilitating better tracking for marketing efforts.

#### Implications of Insights

- **Marketing Strategies**: The concentration of popular authors, along with the evident favorability of ratings, suggests that marketing campaigns could capitalize on well-known authors while also exploring ways to bring attention to lesser-known titles through targeted engagement initiatives (book clubs, social media interactions).
  
- **Data Enhancement**: Increasing the dataset's completeness, especially in the language code, ISBN, and publication date columns, will allow for more nuanced analyses. This should be prioritized to optimize future marketing strategies and reader outreach programs.

- **Reader Engagement**: The correlation between reader reviews and ratings highlights an opportunity for increased reader engagement. Marketing teams should work on creating platforms for reader interaction, such as online book clubs or review submission incentives, to both increase ratings and deepen community ties.

- **Publication Strategy**: By analyzing periods of strong publishing output alongside modern trends, teams can forecast what types of books may re-enter the market and how to position new works against existing favorites.

#### Conclusion

The analysis of this book dataset reveals critical insights into readership trends, author popularity, and engagement strategies. By addressing the areas of data incompleteness, leveraging the strengths of authorship diversity, and enhancing reader engagement efforts, stakeholders can better navigate the competitive landscape of book marketing and publishing.
