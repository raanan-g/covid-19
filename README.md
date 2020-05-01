# Geominr COVID-19 Data Repository.
Geominr has been collecting data surrounding the COVID-19 outbreak in the United States' largest metropolitan areas. This repository contains multiple data files which are organized by county (five-digit FIPS code). If you have any questions please contact us at info@geominr.com.

## Contents:
* [Data Files](https://github.com/geominr/covid-19#data-files)
* [Data Summary](https://github.com/geominr/covid-19#data-summary)
* [Data Quality](https://github.com/geominr/covid-19#data-quality)

## Data Summary


## Data Quality
The reporting of accurate coronavirus data from local health departments has been extremely difficult, especially in the areas that are hardest hit. Using the following code, we generate two data sets containing the locations and times at which cumulative counts of COVID-19 cases and deaths were less than they were on a previous day. These issues in the data can be deleterious to ongoing efforts to model the spread of the virus and guide policy decisions going forward.  
```(python)
url4 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
url5 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
dthsUS = pd.read_csv(url5)
confUS = pd.read_csv(url4)
days = dthsUS.columns[12:] # days holds all of the date columns
ci, di=[],[] 
dflags, cflags=[],[]
cvals, cvals2=[],[]
dvals, dvals2=[],[]
ckey, dkey=[],[]
for i in dthsUS.index:
    for t in range(1, len(days)):
        if dthsUS[days[t]][i] < dthsUS[days[t-1]][i]:
            di.append(dthsUS.FIPS[i])
            dkey.append(dthsUS.Combined_Key[i])
            dflags.append(days[t])
            dvals.append(dthsUS[days[t]][i])
            dvals2.append(dthsUS[days[t-1]][i])
        if confUS[days[t]][i] < confUS[days[t-1]][i]:
            ci.append(confUS.FIPS[i])
            ckey.append(confUS.Combined_Key[i])
            cflags.append(days[t])
            cvals.append(confUS[days[t]][i])
            cvals2.append(confUS[days[t-1]][i])
cases_flags = pd.DataFrame({'FIPS':ci,'Combined_Key':ckey,
                            'Flagged Dates':cflags,'Value Day 1':cvals2,'Value Day 2':cvals})
deaths_flags = pd.DataFrame({'FIPS':di,'Combined_Key':dkey,
                             'Flagged Dates':dflags,'Value Day 1':dvals2,'Value Day 2':dvals})
```
These files are available in this repository and have been shared with the Johns Hopkins Center for Systems Science and Engineering.


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





