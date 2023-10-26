import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Doubling Time Visualization")


df = pd.read_csv("astroph.csv")

df["year"] = df["versions"].str[-20:-16]

add_sidebar = st.sidebar.selectbox("Select Display",("Barchart","Exponential Fit"))
# make a barplot of the year column based on freqeuncy of each year sorted by year
st.bar_chart(df["year"].value_counts().sort_index())
# display the above plot in the streamlit app


# fit papers per year to a function of form 2^(a(x-2000)) from 2000 to 2006
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
def func(x, a,b):
    return b*2**(a*(x-1992))

# print the fitted function


# display the distribution of years in the year column in df
papers_per_year = df['year'].value_counts().sort_index()
# change index of papers_per_year to integers
papers_per_year.index = papers_per_year.index.astype(int)

popt, pcov = curve_fit(func, papers_per_year.index[:17], papers_per_year[:17])

# plot papers per year and the fitted function
plt.scatter(papers_per_year.index[:17], papers_per_year[:17], label="y = b*2^(a(x-2000))"+"\na = " + str(popt[0]) + "\nb = " + str(popt[1]))
plt.plot(papers_per_year.index[:17], func(papers_per_year.index[:17], *popt), 'r-', label='Fit')
plt.scatter(papers_per_year.index[:17],papers_per_year[:17],color = "b", label = "Data")
# add text to the legend of the graph

print("y = b*2^(a(x-1992))")
print("a = " + str(popt[0]))
print("b = " + str(popt[1]))

# add appropriate labels
plt.xlabel('Year')
plt.ylabel("Number of Papers Per Year")
plt.title("Doubling Time is "+ str(1/popt[0]) + "years")
# html figure
plt.legend()
st.pyplot()
#plt.savefig('doubling.png')