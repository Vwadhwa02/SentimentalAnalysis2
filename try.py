import pandas as pd
from textblob import TextBlob
import csv
df=pd.read_csv("Reviews.csv")
print(df)
#print(df["hjvhg"])
#d=dict()
d=dict(df["Reviews"])
print(d,len(d))
l=list()
for i in range(len(d)):
    l+=[TextBlob(d[i]).sentiment.polarity,]
print(l)
lr=list()
for i in l:
    if i>0:
        lr+=["Positive",]
    elif i<0:
        lr+=["Negetive",]
    else:
        lr+=["Moderate",]
print(lr)
#print(dict(lr))
df["polarity"]=l
df["sentiment"]=lr
#print(df)
df.to_csv("Reviews.csv",index=False,mode="a")
print("Done!!")