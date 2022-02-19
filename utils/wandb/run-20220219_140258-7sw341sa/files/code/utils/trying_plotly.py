#%%

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns 
from wandb_integration import * 
# import wandb 
plt.style.use("ggplot")
import plotly.express as px

#%%
reject = pd.read_csv("../data/reject_sample.csv")




data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()

def plot_state_category(data, plot_wandb = False):
    data = data['State'].value_counts()
    fig = plt.figure(figsize = (10,5))
    plt.title("top 10 rejected application states")
    plt.xlabel("state")
    plt.ylabel("count")
    plt.bar(x = data[:10].keys(), height = data[:10].values)
    plt.show() 
    if plot_wandb:
        wandb.log({"top 10 rejected application states":fig})