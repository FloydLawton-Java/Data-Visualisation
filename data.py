import pandas as pd 
import plotly.express as px

df=pd.read_csv("C:/Users/v0788/Desktop/Python/Data Visualisation project/Copy+of+data+-+data.csv") 

fig= px.scatter(df, x="date", y="cases", color="country", size_max=60)

fig.show()
