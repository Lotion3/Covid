from pandas.io.parsers import read_csv
import plotly_express as px
import pandas as pd

df=pd.read_csv("Copy+of+data+-+data.csv")
gr=px.line(df,x="date",y="cases",color="country",title="Covid Cases")
print(df)
gr.show()