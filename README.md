# Geominr COVID-19 Data Repository.
Thank you for visiting the Geominr COVID-19 data repository. All materials in this repository have been collected and maintained by Raanan Gurewitsch. If you have any questions or comments, please contact me at raanan@geominr.com.

## Contents:
* [Data Files](https://github.com/geominr/covid-19#data-files)
* [Data Summary](https://github.com/geominr/covid-19#data-summary)
* [Data Quality](https://github.com/geominr/covid-19#data-quality)

## Data Summary
This repository contains daily coronavirus data for 345 total US counties from 32 states and the District of Columbia. Each county-level time series of daily cumulative* total COVID-19 cases and deaths was matched by five-digit FIPS code or county name to dynamic and static variables from eight additional data sources. By combining data from multiple sources based on geographic region, we are able to examine the impact of social distancinging as well as various social and environmental determinants of health on the spread of the novel coronavirus in American metropolitan regions. Rich contextual data can offer insights into which communities were most vulnerable to experience rapid spread of the virus or high case fatality rates and help guide local and national policies aimed at curbing the virus and allocating scarce resources to assist with response efforts.  
#### Dynamic Data
The dynamic data sets include the daily aggregate changes in human mobility from Google's Community Mobility Reports and air quality levels from the Environmental Protection Agency's AirNow API. Organized by destination type, each mobility data set contains the percent change in visits to grocery stores, workplaces, transit stations and parks within a geographic area. The matrices containing daily air quality index values for ozone, PM2.5 and PM1.0 vary in completeness by pollutant type.
#### Static Data


 
## Data Files:

### 110 largest metro counties
##### COVID-19 US counties time series data (Source: [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series))
* [Confirmed Cases](https://github.com/geominr/covid-19/blob/master/covid-county-data/110%20Cities/Covid19-cases-110USCities.csv)
* [COVID-19 Deaths](https://github.com/geominr/covid-19/blob/master/covid-county-data/110%20Cities/Covid19-deaths-110USCities.csv)

##### Health, hospitals and population data (Sources: [CDC](https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2019-relea/6vp6-wxuq), [Census QuickFacts](https://www.census.gov/quickfacts/fact/table/US/PST045219), [HIFLD](https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals), [American Hospital Directory](https://www.ahd.com/state_statistics.html), [GINI Index](https://www.census.gov/topics/income-poverty/income-inequality/about/metrics/gini-index.html), [Social Vulnerability Index](https://svi.cdc.gov/index.html))
* [Static variables](https://github.com/geominr/covid-19/blob/master/covid-county-data/110%20Cities/static-110USCities.csv)

##### Air Quality Data (Source: [AirNow API](https://docs.airnowapi.org/webservices))
* [Daily AQI PM2.5](https://github.com/geominr/covid-19/blob/master/covid-county-data/110%20Cities/pm25-110.csv)
* [Daily AQI OZONE](https://github.com/geominr/covid-19/blob/master/covid-county-data/110%20Cities/ozone-110.csv)
* [Daily AQI PM10](https://github.com/geominr/covid-19/blob/master/covid-county-data/110%20Cities/pm10-110.csv)

### 345 metropolitan counties (Same sources as above)
##### COVID-19 US counties time series data
* [Confirmed Cases](https://github.com/geominr/covid-19/blob/master/covid-county-data/covid-cases.csv)
* [COVID-19 Deaths](https://github.com/geominr/covid-19/blob/master/covid-county-data/covid-deaths.csv)

##### Health, hospitals and population data
* [Static variables](https://github.com/geominr/covid-19/blob/master/covid-county-data/static.csv)

##### Time series data on county-level mobility (Source: [Google COVID-19 Community Mobility Reports](https://www.google.com/covid19/mobility/))
* [Workplaces](https://github.com/geominr/covid-19/blob/master/covid-county-data/workplaces_percent_change_from_baseline.csv)
* [Transit Stations](https://github.com/geominr/covid-19/blob/master/covid-county-data/transit_stations_percent_change_from_baseline.csv)
* [Residential](https://github.com/geominr/covid-19/blob/master/covid-county-data/residential_percent_change_from_baseline.csv)
* [Grocery and Pharmacy](https://github.com/geominr/covid-19/blob/master/covid-county-data/grocery_and_pharmacy_percent_change_from_baseline.csv)
* [Retail and Recreation](https://github.com/geominr/covid-19/blob/master/covid-county-data/retail_and_recreation_percent_change_from_baseline.csv)
* [Parks](https://github.com/geominr/covid-19/blob/master/covid-county-data/parks_percent_change_from_baseline.csv)


### COVID-19 Data Quality 
The reporting of accurate coronavirus data from local health departments has been extremely difficult, especially in the areas that are hardest hit. Using the code in [jhu-quick-qc-test.py](https://github.com/geominr/covid-19/blob/master/Data%20Quality/jhu-quick-qc-test.py), we generate two data sets containing the locations and times at which cumulative counts of COVID-19 cases and deaths were less than they were on a previous day. These issues in the data can be deleterious to ongoing efforts to model the spread of the virus and guide policy decisions going forward. Both files are available in this repository and have been shared with the Johns Hopkins Center for Systems Science and Engineering.
* [Flagged observations - cases](https://github.com/geominr/covid-19/blob/master/covid-county-data/data-quality/jhu_uscounty_covidCases_flags.csv)
* [Flagged observations - deaths](https://github.com/geominr/covid-19/blob/master/covid-county-data/data-quality/jhu_uscounty_covidDeaths_flags.csv)






