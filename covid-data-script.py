import pandas as pd; import numpy as np; import json
from weightedstats import weighted_median, weighted_mean
from bs4 import BeautifulSoup; import requests
##########################################################################################
##########################################################################################

##########################################################################################
##########################################################################################
url1 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
url2 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
url3 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
url4 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
url5 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
#conf = pd.read_csv(url1)
#dths = pd.read_csv(url2)
#recd = pd.read_csv(url3)
print('Loading Johns Hopkins Data.....', end='')
confUS = pd.read_csv(url4)
dthsUS = pd.read_csv(url5)
confUS = confUS[confUS.Long_!=0]
dthsUS = dthsUS[dthsUS.Long_!=0]
print('Done')
print('Generating 5-digit FIPS codes.....', end='')
def get_fips(fips):
    fips = fips.replace('.0','')
    if len(fips) == 4:
        return '0'+fips
    else:
        return fips
confUS['FIPS'] = [get_fips(str(i)) for i in confUS.FIPS]
dthsUS['FIPS'] = [get_fips(str(i)) for i in dthsUS.FIPS]
print('Done')
##########################################################################################
##########################################################################################

##########################################################################################
##########################################################################################
print('Loading hospital data........', end='')
hospitals = pd.read_csv('Hospitals.csv')
hospitals = hospitals[hospitals.TYPE.isin(['GENERAL ACUTE CARE','CRITICAL ACCESS','MILITARY'])].reset_index()
hospitals['COUNTYFIPS'] = hospitals.COUNTYFIPS.astype(str)
nhosp = []
nhosp999 = []
totalbeds = []
for x in dthsUS.index:
    hdf = hospitals[hospitals.COUNTYFIPS==dthsUS.FIPS[x]].reset_index()
    nhosp.append(len(hdf)) # count hospitals 
    nhosp999.append(len(hdf[hdf.BEDS==-999])) # total without total beds
    totalbeds.append(hdf[hdf.BEDS!=-999].BEDS.sum()) # total beds
dthsUS['nhosp'] = nhosp
dthsUS['nhosp999'] = nhosp999
dthsUS['totalbeds'] = totalbeds
print('Done')
print('Calculating estimated total beds.....', end = '')
r = requests.get('https://www.ahd.com/state_statistics.html')
soup = BeautifulSoup(r.content, 'html.parser')
columns = [i.text for i in soup.find_all('th')]
rows = [i.text for i in soup.find_all('tr')[1:len(soup.find_all('tr'))-2]]
for i in range(0, len(rows)):
    rows[i] = rows[i].split('\n')[1:7]
avghbeds = pd.DataFrame({'state':[row[0].split(' - ')[1] for row in rows[1:]], 
              'avgbeds':[(int(row[2].replace(',',''))/int(row[1].replace(',',''))) for row in rows[1:]]})
estbeds = []
for i in dthsUS.index:
    state = dthsUS.Province_State[i]
    if dthsUS.nhosp999[i] > 0:
        stateavgs = avghbeds[avghbeds.state==state].reset_index()
        if len(stateavgs) > 0:
            est = int(dthsUS.totalbeds[i] + (dthsUS.nhosp999[i] * stateavgs.avgbeds[0]))
            estbeds.append(est)
        else:
            estbeds.append(np.nan)
    else:
        estbeds.append(dthsUS.totalbeds[i])      
dthsUS['estbeds'] = estbeds
print('Done')
##########################################################################################
##########################################################################################
"""
Read in and record demographic data on age and race/hispanic population
"""
##########################################################################################
##########################################################################################
print('Loading Census Data.....', end = '')
ageUS = pd.read_csv('C:/Users/raana/OneDrive/Desktop/Geominr/Data/USA/Counties/Data/ACSSE2018.K200104_data_with_overlays_2020-04-11T175905.csv', 
                    header=1, 
                    usecols=['id','Geographic Area Name', 
                             'Estimate!!Total','Estimate!!Total!!18 to 24 years','Estimate!!Total!!25 to 34 years', 
                             'Estimate!!Total!!35 to 44 years','Estimate!!Total!!45 to 54 years', 
                             'Estimate!!Total!!55 to 64 years', 'Estimate!!Total!!65 years and over']
                   )
ageUS['id'] = [str(x)[9:] for x in ageUS.id]
ageUS.rename(columns={'id':'FIPS'}, inplace=True)
rnm = {}
for i in ageUS.columns:
    if 'Total!!' in i:
        x = i.replace('Estimate!!Total!!','')
        x = x.split(' ')
        if x[2] == 'and':
            x[2] = 'over'
        rnm[i] = 'popage{}_{}'.format(x[0],x[2])
ageUS.rename(columns=rnm,inplace=True)
print('Done')
print('Merging Census data....', end ='')
confUS = pd.merge(confUS, ageUS, on = 'FIPS', how = 'left')
dthsUS = pd.merge(dthsUS, ageUS, on = 'FIPS', how = 'left')
for df in [confUS, dthsUS]:
    for i in ['popage18_24','popage25_34','popage35_44','popage45_54','popage55_64','popage65_over']:
        df[i+'%2018'] = [df[i][x]/df['Estimate!!Total'][x] for x in df.index]
demUS = pd.read_csv('C:/Users/raana/OneDrive/Desktop/Geominr/Data/USA/Counties/Data/ACSDP1Y2010.DP05_data_with_overlays_2020-04-11T185031.csv', 
                    header=1, usecols = ['id','Geographic Area Name', 'Estimate!!HISPANIC OR LATINO AND RACE!!Total population',
                                          'Estimate!!RACE!!One race!!Black or African American',
                                          'Estimate!!HISPANIC OR LATINO AND RACE!!Hispanic or Latino (of any race)'])
demUS['id'] = [str(x)[9:] for x in demUS.id]
demUS.rename(columns={'id':'FIPS', 
                      'Estimate!!HISPANIC OR LATINO AND RACE!!Hispanic or Latino (of any race)':'pophisp18', 
                      'Estimate!!RACE!!One race!!Black or African American':'popblack18',
                      'Estimate!!HISPANIC OR LATINO AND RACE!!Total population':'acspop18'
                     }, inplace=True)
demUS['pophisp%2018'] = [demUS['pophisp18'][x]/demUS['acspop18'][x] for x in demUS.index]
pbl = []
for i in demUS['popblack18']:
    if i == 'N':
        pbl.append(np.nan)
    else:
        pbl.append(int(i))
demUS['popblack18'] = pbl
demUS['popblack%2018'] = [demUS['popblack18'][x]/demUS['acspop18'][x] for x in demUS.index]
confUS = pd.merge(confUS, demUS, on = 'FIPS', how = 'left')
dthsUS = pd.merge(dthsUS, demUS, on = 'FIPS', how = 'left')
for col in confUS.columns:
    if '%' in col:
        confUS[col] = confUS[col]*100
        dthsUS[col] = dthsUS[col]*100
print('Done')     
##########################################################################################
##########################################################################################
"""
Read in the CDC Data and use get_coufips() to identify the county
by the first five digits of the eleven-digit TractFIPS code, which 
is contained in the second part of each UniqueID (e.g., 1718823-17115001100). 
"""
##########################################################################################
##########################################################################################
print('Loading CDC 500 Cities Data.....')
cdcdf = pd.read_csv('500_Cities__Local_Data_for_Better_Health__2019_release.csv')#.dropna(subset=['TractFIPS'])
def get_coufips(fips):
    if fips:
        if len(fips.split('-')) == 1:
            return fips[:5]
        else:
            return fips.split('-')[1][:5] 
    else:
        return np.nan
print('Aggregating data....')
cdcdf['FIPS'] = [get_coufips(fips) for fips in cdcdf.UniqueID]
cdcdf['PopulationCount'] = [int(pop.replace(',','')) for pop in cdcdf.PopulationCount]
cdcdf.dropna(subset=['FIPS'],inplace=True)
coudf = pd.DataFrame({'FIPS':cdcdf.FIPS.unique()})
x = 0
for mid in cdcdf.MeasureId.unique():
    ndf = cdcdf[cdcdf.Year==2017][cdcdf.MeasureId==mid]
    print('Progress: {:.2%}'.format(x/len(cdcdf.MeasureId.unique())), end = '\r')
    if len(ndf) > 0:
        wtd_medians = []
        pops = []
        for i in coudf.FIPS:
            if len(ndf[ndf.FIPS==i]) > 0:
                nndf = ndf[ndf.FIPS==i].reset_index()
                pop = nndf.PopulationCount.sum()
                pops.append(pop)
                value = weighted_median([v for v in nndf.Data_Value], weights=[v for v in nndf.PopulationCount])
                wtd_medians.append(value)
            else:
                wtd_medians.append(np.nan)
                pops.append(np.nan)
        coudf['pop500'] = pops
        coudf[mid] = wtd_medians
        
    x+=1
##########################################################################################
##########################################################################################
""" 
Defining a Metro Area by cdcdf[cdcdf.FIPS==i].CityName.unique(),
which returns every CityName (as defined by CDC 500 Cities) within the 5 digit FIPS grouping
"""
##########################################################################################
##########################################################################################
metro_area = []
for i in coudf.FIPS:
    metro_area.append(str([x for x in cdcdf[cdcdf.FIPS==i].CityName.unique()]).replace("[","").replace("]","").replace("'",""))
coudf['METRO'] = metro_area
print('Done')
##########################################################################################
##########################################################################################
"""
Here we merge all the data together
"""
##########################################################################################
##########################################################################################

print('Merging data......', end='')
cdc_covid_dths = pd.merge(coudf[['FIPS', 'pop500', 'METRO', 'CASTHMA', 'HIGHCHOL', 'DIABETES', 'OBESITY', 
                                 'CANCER', 'STROKE', 'MHLTH', 'CSMOKING', 'CHOLSCREEN', 
                                 'ACCESS2', 'CHD', 'CHECKUP', 'KIDNEY', 'BINGE', 'LPA', 
                                 'ARTHRITIS', 'BPMED', 'PHLTH', 'BPHIGH', 'COPD']], 
                          dthsUS.drop(columns=['UID', 'iso2', 'iso3', 'code3', 
                                               'Country_Region']), 
                          on='FIPS', 
                          how='left')

cdc_covid_conf = pd.merge(coudf[['FIPS', 'pop500', 'METRO', 'CASTHMA', 'HIGHCHOL', 'DIABETES', 'OBESITY', 
                                 'CANCER', 'STROKE', 'MHLTH', 'CSMOKING', 'CHOLSCREEN', 
                                 'ACCESS2', 'CHD', 'CHECKUP', 'KIDNEY', 'BINGE', 'LPA', 
                                 'ARTHRITIS', 'BPMED', 'PHLTH', 'BPHIGH', 'COPD']], 
                          confUS.drop(columns=['UID', 'iso2', 'iso3', 'code3', 
                                               'Country_Region']), 
                          on='FIPS', 
                          how='left')
print('Done')
##########################################################################################
#########################################################################################
#  Ignore this...
##########################################################################################
##########################################################################################
"""
wikicity = []
wikistate = []
wikipop18 = []
wikicities = []
for x in cdc_covid_conf.index:
    citylist = []
    totalpop = 0
    state = ''
    for i in wiki.index:
        if wiki.Name[i] in cdc_covid_dths.METRO[x] and wiki.State[i].strip() == cdc_covid_conf['Province_State'][x]:
            citylist.append(wiki.Name[i])
            totalpop += int(wiki.pop2018[i].replace(',',''))
            state = wiki.State[i]
    if len(citylist) > 1:   
        wikicity.append(str(citylist).replace('[','').replace(']','').replace("'","")+', ')
    elif len(citylist) == 1:
        wikicity.append(citylist[0])
    else:
        wikicity.append('')
    wikicities.append(len(citylist))
    wikistate.append(state)
    wikipop18.append(totalpop)
cdc_covid_conf['wikistate'] = wikistate
cdc_covid_conf['wikicity'] = wikicity
cdc_covid_conf['wikicities'] = wikicities
cdc_covid_conf['wikipop18'] = wikipop18

wikicity = []
wikistate = []
wikipop18 = []
wikicities = []
for x in cdc_covid_dths.index:
    citylist = []
    totalpop = 0
    state = ''
    for i in wiki.index:
        if wiki.Name[i] in cdc_covid_dths.METRO[x] and wiki.State[i].strip() == cdc_covid_dths['Province_State'][x]:
            citylist.append(wiki.Name[i])
            totalpop += int(wiki.pop2018[i].replace(',',''))
            state = wiki.State[i]
    if len(citylist) > 1:   
        wikicity.append(str(citylist).replace('[','').replace(']','').replace("'","")+', ')
    elif len(citylist) == 1:
        wikicity.append(citylist[0])
    else:
        wikicity.append('')
    wikicities.append(len(citylist))
    wikistate.append(state)
    wikipop18.append(totalpop)
cdc_covid_dths['wikistate'] = wikistate
cdc_covid_dths['wikicity'] = wikicity
cdc_covid_dths['wikicities'] = wikicities
cdc_covid_dths['wikipop18'] = wikipop18
"""
##########################################################################################
#########################################################################################
"""
Here we aggregate the 5 boroughs of New York City into one county
"""
##########################################################################################
##########################################################################################
print('Aggregating New York City data...', end='')
medians = ['pophisp%2018','popblack%2018', 'popage65_over%2018']
for mid in cdcdf.MeasureId.unique():
    if mid in cdc_covid_dths.columns:
        medians.append(mid)
for mid in medians:
    try:
        cdc_covid_conf.at[90, mid] = cdc_covid_conf[cdc_covid_conf.METRO=="'New York'"][mid].median()
    except KeyError:
        continue
sums = ['pop500','nhosp','nhosp999','totalbeds','estbeds']
for col in sums:
    try:
        cdc_covid_conf.at[90, col] = cdc_covid_conf[cdc_covid_conf.METRO=="'New York'"][col].sum()
    except KeyError:
        continue
print('Done')
##########################################################################################
#########################################################################################
""" 
Get time series data into the right format
"""
##########################################################################################
##########################################################################################
print('Preparing data.......', end='')
tscols = ['FIPS']
rnm = {}
for col in cdc_covid_dths.columns:
    if '/' in col:
        m, d, yy = col.split('/')
        if len(m) == 1:
            m = '0'+m
        if len(d) == 1:
            d = '0'+d
        mmddyyyy = m+'-'+d+'-'+yy+'20'
        tscols.append(mmddyyyy)
        rnm[col] = mmddyyyy
cdc_covid_dths.rename(columns=rnm, inplace=True)
cdc_covid_conf.rename(columns=rnm, inplace=True)
#for mid in cdcdf.MeasureId.unique():
#    if mid in cdc_covid_dths.columns:
#        print("'{}',".format(mid), end='')
##########################################################################################
##########################################################################################
"""
Drop all rows with missing data for COVID-19 and flag counties currently listed with no
confirmed cases.
"""
##########################################################################################
##########################################################################################
cdc_covid_conf.dropna(subset=[tscols[1]], inplace=True)
cdc_covid_dths.dropna(subset=[tscols[1]], inplace=True)
cdc_covid_conf.reset_index(inplace=True)
zero = []
for i in cdc_covid_conf.index:
    if cdc_covid_conf[tscols[len(tscols)-1]][i] == 0:
        zero.append('FLAG')
    else:
        zero.append('NO_FLAG')
# Here we drop the data and make sure that the deaths file and the cases file 
# are in the same order
cdc_covid_conf['FLAG'] = zero
cdc_covid_conf = cdc_covid_conf[cdc_covid_conf.FLAG!='FLAG']
cdc_covid_dths = cdc_covid_dths[cdc_covid_dths.FIPS.isin(cdc_covid_conf.FIPS)]
print('Done')
##########################################################################################
#########################################################################################
"""
Save static data and dynamic data by FIPS code in different files with the same order 
"""
##########################################################################################
##########################################################################################
print('Saving data.......',end='')
cdc_covid_dths[['FIPS','Province_State','Combined_Key','Lat','Long_','Population', 
                
                'METRO','pop500','CASTHMA','HIGHCHOL','DIABETES','OBESITY','CANCER', 
                'STROKE','MHLTH','CSMOKING','CHOLSCREEN','ACCESS2','CHD','CHECKUP', 
                'KIDNEY','BINGE','LPA','ARTHRITIS','BPMED','PHLTH','BPHIGH','COPD',
                
                'nhosp','nhosp999','totalbeds','estbeds', 
                'popage65_over%2018','popblack%2018','pophisp%2018']].fillna('NAN').to_csv('covid-county-data/static.csv', index=False)
cdc_covid_dths[tscols].fillna('NAN').to_csv('covid-county-data/covid-deaths.csv', index=False)
cdc_covid_conf[tscols].fillna('NAN').to_csv('covid-county-data/covid-cases.csv', index=False)
print('Done')