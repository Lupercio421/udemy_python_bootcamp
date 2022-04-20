    # %%
"""
# DSNY Bureau of Recycling and Sustainability Skills Assessment: Daniel Lupercio
"""

# %%
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt    
import datetime

# %%
"""
## 1. Using python and pandas library or any other data analysis library, parse the data out of the excel or csv file and complete the following:
"""

# %%
"""
### a. Create a pivot table where tonnages are summed up by material type and year. Combine RESORGANICSTONS,SCHOOLORGANICTONS and LEAVESORGANICTONS into a single column “ORGANICS”.
"""

# %%
DSNY_waste = pd.read_csv("C:/Users/Daniel/Downloads/DSNY_Monthly_Tonnage_Data.csv")
print(DSNY_waste.head(10))
print()

# %%
DSNY_waste['YEAR'] = pd.DatetimeIndex(DSNY_waste['MONTH']).year #datatime package is used to return the year from the 'Month' field
print(DSNY_waste['YEAR'].head(10))
print()

# %%
DSNY_waste['ORGANICS'] = DSNY_waste[["RESORGANICSTONS", "SCHOOLORGANICTONS", "LEAVESORGANICTONS"]].sum(axis = 1)
print(DSNY_waste['ORGANICS'].tail(10))
print()

# %%
DSNY_waste = DSNY_waste.rename(columns={"MGPTONSCOLLECTED":"MGP", "PAPERTONSCOLLECTED": "PAPER", "REFUSETONSCOLLECTED":"REFUSE"})
print(DSNY_waste.head())
print()

# %%
# DSNY_waste[["YEAR", "MGP", "ORGANICS", "PAPER", "REFUSE"]].groupby(['YEAR'], as_index=False).sum() this works great, the variables are ordered correctly, and we groupby the year. as_index=F allows creates a dataframe
DSNY_pivot = DSNY_waste[["YEAR", "MGP", "ORGANICS", "PAPER", "REFUSE"]].groupby(['YEAR'], as_index=False).sum()
print(type(DSNY_pivot))
print(DSNY_pivot.head(5))
print()

# %%
DSNY_pivot.to_csv("DSNY_pivot.csv")

# %%
"""
## 2. Using the pivot table from 1a, create a chart by completing the following:
"""

# %%
"""
### a. Remove the 2022 row from pivot table
"""

# %%
print(DSNY_pivot[(DSNY_pivot['YEAR'] == 2022)]) # returning the row where (Year = 2022), with the index = 32
print()
DSNY_pivot.drop(32, axis=0, inplace=True)

# %%
print(DSNY_pivot.tail(5)) #the row with year = 2022 has been droped

# %%
"""
## b. Using matplotlib or any other visualization library, create a stackplot using the output pivot table from 2a. Use the “YEAR” values for the x-axis and the tonnage numbers for the y-axis. Make sure to label chart elements meaningfully so that anyone can read and understand them.
"""

# %%
plt.stackplot(DSNY_pivot['YEAR'], DSNY_pivot['MGP'], DSNY_pivot["ORGANICS"], DSNY_pivot["PAPER"], DSNY_pivot["REFUSE"]) #The YEAR is passed first, as the X-avis values, the other values after will be interpreted as y-values
plt.legend(['MGP', "ORGANICS", "PAPER", "REFUSE"], loc = "upper left")
plt.xlabel("Year")
plt.ylabel("Tons Collected in Millions")
plt.show()