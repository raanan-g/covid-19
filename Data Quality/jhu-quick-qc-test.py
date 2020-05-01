import pandas as pd
url4 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
url5 = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
dthsUS = pd.read_csv(url5)
confUS = pd.read_csv(url4)
days = dthsUS.columns[12:]
ci,di=[],[]
dflags,cflags=[],[]
cvals,cvals2=[],[]
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
deaths_flags.to_csv('jhu_uscounty_covidDeaths_flags.csv')
cases_flags.to_csv('jhu_uscounty_covidCases_flags.csv')
