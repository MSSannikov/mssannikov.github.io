# Exploring Kaggle's Telco Churn Data Set
## by Maksim Sannikov


## Telco Customer Churn

The Telco data set consists of 7032 records with 21 different variables. The variables consist of monthly charges, total charges, customer tenure, and a variety of other categorical attributes used to describe the cuustomers. I dropped customers that had 0 total charges because they also have 0 for tenure.

The data and associated documentation can be found here:
https://www.kaggle.com/blastchar/telco-customer-churn


## Summary of Findings

In the exploration phase, I discovered that there was a fairly strong relationship between a customers tenure (churn), and binned bill size, subscription services (type of internet, if they have phone, etc), and contract type.

It appeared that the most prominent relationship occurred between tenure and contract type - meaning that customers with one and two year contracts maintain a greater probability of remaining customers than customers on a month to month contract.  However, that was not the only influence.  Customers that have only phone through telco have the best survival rate.

As it ends up, the best survival rate is found among those customers that have two year contracts, very high bills and subscribe to both phone and Fiber optic internet service.  Additionally, the worst survival rate is found among those with the lowest bills that are on month to month contracts and subscribe to both phone and DSL.


## Key Insights for Presentation

For the presentation, I focus largely on the relationship between monthly charges and tenure, as well as the influence of services subscribed, and contract type.  

Based on the distribution, monthly charges appear to dictate which services a user subscribes to.  This is important 

After introducing the distributions, I move on to sharing the survival rates among the various variables.  It is very apparent that contract is by far the most impactful variable on survival rate and a close second turned out to be InternetService.  When combining everything together, the picture becomes clearer.  Customers with seemingly all of the service offerings while on a two year contract tend to stick around longer on average than the rest.
