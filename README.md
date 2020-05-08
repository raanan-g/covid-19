# Geominr COVID-19 Data Repository.
Thank you for visiting the Geominr COVID-19 data repository. All materials in this repository have been collected and maintained by Raanan Gurewitsch. If you have any questions or comments, please contact me at raanan@geominr.com.

## Contents:
* [Data Summary](https://github.com/geominr/covid-19#data-summary)
* [Data Files](https://github.com/geominr/covid-19#data-files)

## Data Summary
This repository contains daily coronavirus data for 345 total US counties from 32 states and the District of Columbia. Each county-level time series of daily cumulative* total COVID-19 cases and deaths was matched by five-digit FIPS code or county name to dynamic and static variables from eight additional data sources. By combining data from multiple sources, we are able to examine the impact of social distancing as well as various pre-existing social and environmental determinants of health on the spread of the novel coronavirus in American metropolitan regions. This rich collection of contextual data can offer insights into which communities were most vulnerable and help guide local and national policies aimed at curbing the spread and allocating scarce resources to bolster ongoing response efforts.  
\* Some cumulative counts are non-cumulative. See [Data Quality](https://github.com/geominr/covid-19#covid-19-data-quality) Section
#### Dynamic Data
The dynamic data sets include the daily aggregate changes in human mobility from Google's [Community Mobility Reports](https://www.google.com/covid19/mobility/) and air quality levels from the Environmental Protection Agency's [AirNow API](https://docs.airnowapi.org/webservices). Organized by destination type, each mobility data set contains the percent change in visits to grocery stores, workplaces, transit stations and parks within a given county. The matrices containing daily air quality index values for ozone, PM2.5 and PM1.0 vary in completeness by pollutant type and are not quality assured.
#### Static Data
<p>The static data in this repository was collected from the US Census Bureau, Centers for Disease Control and Prevention (CDC) and the Department of Homeland Security. The 48 different fields cover the domains of health status, hospital capacity and socioeconomic and demographic conditions. For specific definitions of each field in this data set, see the <a href="https://github.com/geominr/covid-19/blob/master/StaticDataDictionary.csv">Data Dictionary</a> file.</p>
<p>Data on health outcomes, prevention measures and unhealthy behaviors were extracted from the CDC's <a href="https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2019-relea/6vp6-wxuq">500 Cities Local Data for Better Health</a> program. These fields consist of twenty measures of the median crude or age-adjusted prevalence of conditions such as respiratory disease, obesity or smoking. These values were aggregated from census tract to the county level using the first five digits of the eleven digit tract FIPS code. Because a single county may consist of multiple individual cities, we include the list of all city labels within each aggregate group to represent the greater metropolitan area. </p>
<p>Demographic variables were gathered from the <a href="https://www.census.gov/quickfacts/fact/table/US/PST045219">Census QuickFacts</a> online resource using an automated web scraping algorithm and cover relevant areas such as age, race, income and population density. Additional socioeconomic variables include the Gini Index, which measures economic inequality and <a href="https://svi.cdc.gov/index.html">Social Vulnerability Index</a> rankings from the CDC.</p>
<p>Lastly, the total number of general acute care, critical access and military hospitals within each county are included in the data. We list the number of known beds, estimated number of beds--total known beds plus the number of hospitals without number of beds times the average number of beds per hospital in that state--and the estimated number of beds per 1,000 people. This data was collected from the Homeland Infrastructure Foundation-Level Data (<a href="https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals">HIFLD</a>) resource and the <a href="https://www.ahd.com/state_statistics.html">American Hospital Directory</a></p>

#### New York City data
Time series data for the 5 individual counties (boroughs) in New York City were not available in the Johns Hopkins CSSE dataset. Rather, the total number of cases and deaths for the entire city of New York are reported and assigned the FIPS code of New York County (Manhattan). To ensure consistent geography across the static and dynamic data, we compute the median or sum of each static field for the 5 counties. For more detailed data on Covid-19 in New York City, see the NYC Department of Health's [data repository](https://github.com/nychealth/coronavirus-data).
 
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
* [Static variables](https://github.com/geominr/covid-19/blob/master/covid-county-data/static.csv) - *Warning:* Some columns in this data set have faulty values

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






