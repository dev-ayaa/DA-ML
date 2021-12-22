# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl

# %%
dataTableA = {
    'A': 12,
    'B': 34,
    'C': 94,
    'D': 89
}
dataTableB = {
    'A': 12,
    'B': 34,
    'C': 94,
    'D': 89
}

print(pd.DataFrame({"Data_1": dataTableA, "Data_2": dataTableB}))
# %%
sd_1 = pd.Series(np.linspace(1, 10, 6))
sd_2 = pd.Series(np.linspace(1, 23, 6))
sd_3 = pd.Series(np.linspace(1, 145, 6))
sd_4 = pd.Series(np.linspace(1, 4, 6))
sd_5 = pd.Series(np.linspace(1, 34, 6))
sd_6 = pd.Series(np.linspace(1, 65, 6))
sd_7 = pd.Series(np.linspace(1, 11, 6))
sd_8 = pd.Series(np.linspace(1, 90, 6))
sd_9 = pd.Series(np.linspace(1, 43, 6))

frame_data = pd.DataFrame(
    {'D1': sd_1, 'D2': sd_2, 'D3': sd_3, 'D4': sd_4, 'D5': sd_5, 'D6': sd_6, 'D7': sd_7, 'D8': sd_8, 'D9': sd_9})
frame_data

# %%
# row= axis=0, and column = axis=1
car_sales = pd.read_csv("data/car-sales.csv")
# Expoting data to csv files / format
car_sales.to_csv("new_car_sales.csv", index=False)
new_cars = pd.read_csv("new_car_sales.csv")
new_cars
##
# %%
#Checking the description of planets.csv data
planets= pd.read_csv("data/planets.csv")
# planets.dtypes
#%%
planets_datatypes= planets.dtypes
planets_datatypes

#%%
columns= planets.columns
columns

#%%
data_des= planets.describe()
data_des
