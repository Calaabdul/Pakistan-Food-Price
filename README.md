# Pakistan Food Price Prediction
This project aims to predict the prices of various food items in Pakistan using Machine Learning. Accurate food price predictions can help in decision making for farmers, consumers, and government, leading to better food security and economic stability.
Food prices can fluctuate due to various factors such as weather conditions and economical reasons like inflation, market demand, and supply chain issues. This project uses machine learning to analyze these factors and predict future prices.

## Data Description
The dataset includes historical prices of various food items from 2004 to 2019 in different regions of Pakistan. 
It includes additional features such as:
- Date : 
- commododity name: Name of food item
- unit: Unit of measurement
- category
- price
- currency: Currency unit
- country: Country name
- admname: Adm1 name
- adm1id: Adm1 code
- mktname: Market name
- mktid: Market ID
- cmid: Commodity ID
- ptid: Pid
- umid: Umid
- catid: Item type code
- sn : Meta ID

### Data Sources
- The data was collected from  World Food Programme.[World Food Program](https://www.wfp.org/)
- (https://data.worldbank.org/)https://www.kaggle.com/datasets/hussainaliarif/pakistan-food-prices/data

## Models
I experimented with several models including:
- Ridge Regression
- Decision Trees

The models were evaluated based on R-squared (R²) performance metric.The best-performing model was the Ridge

