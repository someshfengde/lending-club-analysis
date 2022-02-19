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

#%%
data = reject['State'].value_counts()


#%%

# wandb.log({"top 10 rejected application states":fig})

#%%

