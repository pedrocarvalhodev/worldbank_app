
# coding: utf-8

# http://wbdata.readthedocs.io/en/latest/

# In[ ]:

########################################################################################################
# WORLD PROGRESS - INDICATORS, RANKINGS, TENDENCIES, PREDICTIVE, CAUSAL, OPTIMIZATION, RECOMMENDATIONS
# Descriptive Dasboard (movies + gapminder) 
# - Interactive filters ( Tableau )
# - <See Plots> 
# Cluster
# - group similar countries by data in visual sense
# Causal + Predictive
# - Statsmodels ARIMA / Sklearn -> report with line in other color and risk variance (= r forecast)
# Optimization
# - PuLP ( Slider + PuLP ) interactive integer | linear optmization 
# Recommendation
# - Some recomendation based on optimization
# DOWNLOAD REPORT - interactive jupyter notebook html
########################################################################################################

# Plots
# 1. Relationship - scatterplot > color (cluster), lines (optimization), bubble ( 3Dimensions ), regression (R car)
# 2. Composition - barchart, Donut
# 3. Comparison > Bar charts
# 4. TimeSeries - 
# 5. boxplot, violin
# 6. dd style (heatmap)
# 7. geomapping

# Replicate MOVIES (gapminder) with World Bank Data
# 1. select many countries
# 2. 2 metrics Y axis and bubble size (y is time)
# 3. select format of data


# http://bokeh.pydata.org/en/latest/docs/gallery.html

# http://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/00%20-%20intro.ipynb#Interaction

# In[ ]:

#!cp /home/pedro/Downloads/gapminder.ipynb ./


# In[ ]:

#!jupyter notebook gapminder.ipynb


# In[ ]:

import wbdata
import pandas


# In[ ]:

import datetime


# In[ ]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# In[ ]:

#set up the countries I want
countries = ["CL","UY","HU"]
 
#set up the indicator I want (just build up the dict if you want more than one)
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}
 
#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
dfu = df.unstack(level=0)

# a simple matplotlib plot with legend, labels and a title
dfu.plot(); 
plt.legend(loc='best'); 
plt.title("GNI Per Capita ($USD, Atlas Method)"); 
plt.xlabel('Date'); plt.ylabel('GNI Per Capita ($USD, Atlas Method');


# In[ ]:

wbdata.get_source()


# In[ ]:

# 1 DOing Business
wbdata.get_indicator(source=1)


# In[ ]:

wbdata.search_countries("Brazil")


# In[ ]:

#wbdata.get_data(indicator, country=u'all', data_date=None, convert_date=False, pandas=False, 
#column_name=u'value', keep_levels=False)
wbdata.get_data("IC.BUS.EASE.XQ", country=u'BRA')


# In[ ]:

data_date = (datetime.datetime(2010, 1, 1), datetime.datetime(2011, 1, 1))
wbdata.get_data("IC.BUS.EASE.XQ", country=("USA", "BRA"), data_date=data_date)


# In[ ]:

wbdata.search_indicators("gdp per capita")


# In[ ]:

wbdata.get_incomelevel()


# In[ ]:

countries = [i['id'] for i in wbdata.get_country(incomelevel="OEC", display=False)]
indicators = {"IC.BUS.EASE.XQ": "doing_business", "NY.GDP.PCAP.PP.KD": "gdppc"}
df = wbdata.get_dataframe(indicators, country=countries, convert_date=True)
df.describe()


# In[ ]:

df = df.dropna()
df.gdppc.corr(df.doing_business)


# In[ ]:




# In[ ]:




# In[ ]:



