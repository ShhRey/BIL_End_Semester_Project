import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('D:/Shrey/BIL-Project/Suicide.csv')

data=data.drop(['HDI for year','country-year'],axis=1)                  #dropping these two columns

#-----Table------------------------------------------------------------------------------------------------------------------------------------------------------------

grouop_data=data.groupby(['age','sex'])['suicides_no'].sum().unstack()  #collecting data and making table using 'unstack()' function
grouop_data=grouop_data.reset_index().melt(id_vars='age')               #arranging according to age
grouop_data_female=grouop_data.iloc[:6,:]                               #retrieving 6 rows using 'iloc' function
print("\n--Table of Suicides according to Female Age Groups--\n")
from IPython.display import display
display(grouop_data_female)                                             #displaying table
print("\n")

#-----Country vs. suicide_no-------------------------------------------------------------------------------------------------------------------------------------------

suicidesNo=[]
for country in data.country.unique():                                   
    suicidesNo.append(sum(data[data['country']==country].suicides_no))  #getting total no of suicides of all countries

suicidesNo=pd.DataFrame(suicidesNo,columns=['suicides_no'])             
country=pd.DataFrame(data.country.unique(),columns=['country'])
data_suicide_countr=pd.concat([suicidesNo,country],axis=1)              #definind data and axis to plot

data_suicide_countr=data_suicide_countr.sort_values(by='suicides_no',ascending=False)#displaying plot in descending order(i.e. from highest no. of suicides to lowest)

sns.barplot(y=data_suicide_countr.country[:20],x=data_suicide_countr.suicides_no[:20])  #displaying bars of only 20 countries with highest no. of suicides
plt.title("20 Countries with Higest Suicide Number from 1985 to 2016")
plt.show()

#-----Population vs. Age_group-----------------------------------------------------------------------------------------------------------------------------------------

index_suicide=[]
for age in data['age'].unique():
    index_suicide.append(sum(data[data['age']==age].suicides_no)/len(data[data['age']==age].suicides_no))  #getting suicide rate of each age group
    
plt.bar(['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years'],index_suicide,align='center',alpha=0.5) #defining xticks
plt.xticks(rotation=45)                                                 #rotating xticks by 45 degree anticlockwise
plt.title("Suicide rates of Different Age Groups")
plt.show()
