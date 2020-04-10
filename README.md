# Whats-In-My-Makeup-Bag

### Presentation:
https://docs.google.com/presentation/d/1D423buf9mRmoyYd_Y_Px--UYyISzgiUIupycwaf3miw/edit?usp=sharing 

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

## Project Description & Motivation
* Analyzed records of cosmetic products with known/suspected harmful chemicals
* Used data from a CSV file with over 110,000 records
    * Reported to the California Safe Cosmetics Program from 2009-2020, updated daily
    * Had over 600 companies, 120 chemicals
* Was motivated as a cosmetics user to find a safer company

#### Data Source
Chemicals in Cosmetics csv: https://healthdata.gov/dataset/chemicals-cosmetics
 * Downloaded: 2020-04-05

#### Description of Data 
Contains 113,732 rows with fields including cosmetic label names, company/manufacturer names, product categories, reported chemicals, number of reported chemicals for each product, dates of reporting, and dates of product discontinuation or reformulation, if available.

> ## Question: Do certain companies handle having harmful cosmetic products differently?

## Data Wrangling
* Loaded csv into a Pandas DataFrame
* Focused on less than half of the 22 columns, most importantly:
    * CDPHId (identifies unique products)
    * CompanyName
    * DiscontinuedDate (to classify discontinued products)
    * ChemicalDateRemoved (to classify reformulated products)
* Classified products as discontinued/reformulated with date columns
* Cleaned categorical columns 

![categorical_col_cleaning](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Screen%20Shot%202020-04-10%20at%201.30.35%20PM.png)

## EDA
### Status of Reported Products
* Nearly 37,000 products reported
* Around 31,500 not yet reformulated/discontinued
* 4,500 were discontinued and 1,000 were only reformulated

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

### Product Discontinuations
* Two peaks in July 2013 and Oct 2016

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)
![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

### Comparing Product Discontinuations
* Buth-Na-Bodhaige: 454/1045 (43%) discontinued
* Proctor & Gamble: 578/902 (64%) discontinued
* May take over 2-3 years for products to be discontinued

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

### Comparing Product Status Ratios
* Half the top 10 companies have a ratio of reformulated or discontinued products close to 0

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

## Hypothesis Testing
### Ratio Reformulated or Discontinued
### Hypothesis Test #1: 2 Big Nail Product Companies
1. Revlon
* \# Reformulated/ Discontinued = 118
* \# Samples = 1,458
* Ratio = 0.081
2. OPI
* \# Reformulated/ Discontinued = 13
* \# Samples = 236
* Ratio = 0.055

> Null Hypothesis: 
There is no statistically significant difference in the ratio reformulated or discontinued for two companies:   

> PRevlon = POpi

> Alternate Hypothesis: 
There is a statistically significant difference in the ratio for two companies:             

> PRevlon =/= POpi

* Threshold = 0.05
* P-value = 0.08
* *Failed to reject null*

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

### Hypothesis Test #2: 2 Big High-End Product Companies
1. Chanel
 * \# Reformulated/ Discontinued = 5
 * \# Samples = 88
 * Ratio = 0.057
2. Estee Lauder
* \# Reformulated/ Discontinued = 0
* \# Samples = 68
* Ratio = 0

> Null Hypothesis: 
There is no statistically significant difference in the ratio reformulated or discontinued for two companies:

> PChanel = PEstee Lauder

> Alternate Hypothesis: 
There is a statistically significant difference in the ratio for two companies:

> PChanel =/= PEstee Lauder

 * Threshold = 0.05
 * P-value = 0.02
 * *Reject null hypothesis*

 ![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

## Conclusion

* Majority (85%) of reported products have not yet been reformulated or discontinued
* On average, it took over 2-3 years for products to be discontinued
    *Even for 2 companies that discontinued the most products
* There was no statistically significant difference between 2 big nail product companies
* There was a statistically significant difference between 2 big high-end companies

> **Q:** Do certain companies handle having harmful cosmetics products much differently? 

> **A:** Some may.

* **Something to consider:** Dataset contained only harmful products
* **Future work:** Additional domain knowledge/data would help to classify most harmful products vs least harmful

___

## Additional EDA Plots

 ![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

 ![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

 ![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

 ![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)