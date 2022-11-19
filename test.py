import pandas as pd,numpy as np

pred = 65566 
df = pd.read_csv("laptop_data.csv")
prices = df["Price"]
print(prices)
m=0
my_list = [pred]

nearby = list()
for i in prices:
     if i >= pred-1000 and i <= pred+1000:
          my_list.append(i) 
print(my_list)