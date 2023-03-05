# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:29:00 2023

@author: Kisha
"""

import pandas as pd
import matplotlib.pyplot as plt

#read excel excel file
ukvisaentry = pd.read_excel(r"D:\project\entry-visas1-sep-2018-tables.xlsx")
#selected rows from the DF
rdc = ukvisaentry.iloc[[116,33,125,131,175,183]] 
print(rdc)
labels1 = ['India', 'Bangladesh', 'Japan', 'Korea (South)', 'Nigeria', 'Pakistan']
# Defined a Function
def Immigration_on_years(a,b): 
    plt.figure(figsize = (20,10)) 
    plt.pie(a[b], autopct='%1.1f%%', labels = labels1, rotatelabels = True)
    plt.title("Immigration on {}".format(b))
    plt.legend()
    plt.show()
Immigration_on_years(rdc,2017)

crude = pd.read_csv(r"D:\project\Crude oil imp_USD.csv")
print(crude)

crude.dropna(inplace=True)
#creating Line plot
plt.figure(figsize=(15,9))
plt.plot(crude["Year"], crude["France"], label="France")
plt.plot(crude["Year"], crude["Germany"], label="Germany")
plt.plot(crude["Year"], crude["Italy"], label="Italy")
plt.plot(crude["Year"], crude["Spain"], label="Spain")
plt.plot(crude["Year"], crude["UK"], label="UK")
plt.plot(crude["Year"], crude["Japan"], label="Japan")
plt.plot(crude["Year"], crude["Canada"], label="Canada")
plt.plot(crude["Year"], crude["USA"], label="USA")
# set labels and show the legend
plt.xlabel('Year')
plt.ylabel("US Dollars")
plt.title('Crude oil import percentage(USD)')
plt.legend()
plt.savefig('Line_plot.png')
plt.show()


# Defining a function to create bar plot
def players(x):
    x.sort_values('Price (US$)',ascending=False)
    wpl = x.head(10)
    plt.figure(figsize=(15,8))
    plt.barh(wpl['Player'].head(15),wpl['Price (US$)'].head(15))
    plt.xlabel('Price in USD')
    plt.ylabel('Players')
    plt.title('Highest auctioned players')
    plt.show
#Importing the data
wpl=pd.read_csv(r"D:\project\auction_2023.csv")
#Calling the players function
players(wpl)





