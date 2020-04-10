# Whats-In-My-Makeup-Bag

#### Presentation:
https://docs.google.com/presentation/d/1D423buf9mRmoyYd_Y_Px--UYyISzgiUIupycwaf3miw/edit?usp=sharing 

![Dangers-of-Makeup.jpg](https://github.com/chelseanbr/Whats-In-My-Makeup-Bag/blob/eda/images/Dangers-of-Makeup.jpg)

## Project Description
* Analyzed products with chemicals linked to cancer, birth defects, or other harm
    * Reported to the California Safe Cosmetics Program from 2009-2020
* Used data from a CSV file with over 110,000 records
    * From over 600 companies 
* Was motivated as a cosmetics user to choose a safer company
* Compared different companies within dataset for hypothesis testing

## Data Source
Chemicals in Cosmetics csv: https://healthdata.gov/dataset/chemicals-cosmetics
 * Downloaded: 2020-04-05

## Description of Data 
Contains 113,732 rows with cosmetic label names, company/manufacturer names, product categories, reported chemicals, number of reported chemicals for each product, dates of reporting, and dates of product discontinuation or reformulation if available.

## Data Wrangling
* Loaded csv file into a Pandas DataFrame
* Focused on less than half of the 22 columns, most importantly:
    * CDPHId (identifies unique products)
    * CompanyName
    * InitialDateReported
    * DiscontinuedDate (existence used to classify discontinued products)
    * ChemicalDateRemoved (existence used to classify reformulated products)
* Converted columns to date-time format and classified products with new columns
* Calculated time to discontinuation in days with DiscontinuedDate - InitialDateReported
* Cleaned categorical columns since wanted to do hypothesis testing with CompanyNames 

## EDA and Hypothesis Testing


## Conclusion