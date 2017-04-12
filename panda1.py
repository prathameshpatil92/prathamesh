import pandas as pd

#1:
mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
ufo_cols=['col1','col2','col3','col4','col5']
mymoviedata.columns=ufo_cols
#print(mymoviedata)

#2:
#print(mymoviedata.col3)

#3:

mymoviedata["col6"]=mymoviedata.col2.apply(str) +","+ mymoviedata.col4
print(mymoviedata)

#4:
#print(mymoviedata.columns)
#print(mymoviedata)
#mydata1=pd.read_csv("http://bit.ly/uforeports")
#type(mydata1)
#print(mydata1.City+ " "+mydata1.State)
#mydata1["location"]=mydata1.City + " , "+ mydata1.State
#print(mydata1)
'''
mydata2=pd.read_csv("http://bit.ly/imdbratings")
print(mydata2.head())
mydata2.describe()
'''

