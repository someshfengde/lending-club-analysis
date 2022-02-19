#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from yaspin import yaspin
import seaborn as sns 
from utils.wandb_integration import * 
# import wandb 
plt.style.use("ggplot")
import plotly.express as px 


# rejection applicatoinl date year wise 
def plot_reject_yearwise(data, plot_wandb = False):
    year_wise = data['Application Date'].apply(lambda x: x.split('-')[0]).value_counts()
    year_wise = year_wise.sort_index()
    year_wise = year_wise.reset_index()
    year_wise.columns = ['year', 'count']
    year_wise['year'] = year_wise['year'].astype(int)
    year_wise = year_wise.sort_values(by = 'year')
    fig = px.line(x = year_wise['year'], y = year_wise['count'])
    fig.update_layout(title_text="rejected application year wise", xaxis_title="year", yaxis_title="count")
    fig.show()
    if plot_wandb:
        save_plot(name = 'reject_year_wise', plot = fig)


#%%

    

#%%
# plotting loan title with the requested categories 
def plot_loan_title_category(data, plot_wandb= False ):
    data_counts = data['Loan Title'].value_counts()
    fig = px.bar(x = data_counts[:10].keys(), y = data_counts[:10].values, color = data_counts[:10].values)
    fig.update_layout(title_text="top 10 rejected loan titles", xaxis_title="loan title", yaxis_title="count")
    fig.show()
    if plot_wandb:
        save_plot(name = 'reject_loan_title', plot = fig)

    fig = px.bar(x = data_counts[-10:].keys(), y = data_counts[-10:].values, color = data_counts[-10:].values)
    fig.update_layout(title_text="least rejected loan titles", xaxis_title="loan title", yaxis_title="count")
    fig.show()
    if plot_wandb:
        save_plot(name = 'reject_loan_title', plot = fig)

    return 

# plotting risk score 
def plot_risk_score_category(data, plot_wandb = False):
    null_vals = data['Risk_Score'].isna().sum()/len(data['Risk_Score'])* 100
    desc = data['Risk_Score'].describe()
    desc = desc[['min', '25%', "50%", "75%",'max']].values
    risk_cat = pd.cut(data['Risk_Score'], bins=desc, labels=[f'< {desc[1]}', f'{desc[1]} < val < {desc[2]}',f'{desc[2]} < val < {desc[3]}',f'>{desc[3]}'])
    val_cou = risk_cat.value_counts()

    fig = px.bar(x = val_cou.keys(), y = val_cou.values, color = val_cou.values)
    fig.update_layout(title_text=f"Risk Score \n there are {null_vals:.2f}% null values", xaxis_title="risk score", yaxis_title="count")
    fig.show()
    if plot_wandb:
        save_plot(name = 'reject_risk_score', plot = fig)
    return 


#%%

# plotting states with most rejected applications
def plot_state_category(data, plot_wandb = False):  
    data = data['State'].value_counts()
    fig = plt.figure(figsize = (10,5))
    fig = px.bar(x = data[:10].keys(), y = data[:10].values,
    title = 'top 10 rejected application states', 
    color = data[:10].values, 
    )
    fig.update_layout(title_text="top 10 rejected application states", 
                    xaxis_title="state", yaxis_title="count")

    fig.show()
    if plot_wandb:
        wandb.log({"top 10 rejected application states":fig})


#%%

# plotting employment length
def plot_employment_length_category(data, plot_wandb = False):
    data = data['Employment Length'].value_counts()

    fig = px.bar(x=data.keys(), y=data.values, color=data.values)
    fig.update_layout(title_text="rejected application reletion with employment length", 
    xaxis_title="Employment Length", yaxis_title="count")
    fig.show()
    if plot_wandb:
        save_plot(name = 'reject_employment_length', plot = fig)
        # save_bar_plot(label = list(data.keys()), data = data.values, title = 'rejected application reletion with employment length', x_label = 'Employment Length', y_label = 'count')
    print("here we can observe that we are < 1 year emp length are getting rejected most")



#%% 
# plotting most rejected application policy Code wise 
def plot_policy_code_category(data, plot_wandb=False):
    data = data['Policy Code'].value_counts()

    fig = px.bar(x=data.keys(), y=data.values, color=data.values)
    fig.update_layout(title_text="rejected application reletion with policy code",
    xaxis_title="Policy Code", yaxis_title="count")
    fig.show()

    if plot_wandb:
        save_plot(name = 'reject_policy_code', plot = fig)
   


#%%
def plot_amount_requested_category(data, plot_wandb = False ):
    desc = data['Amount Requested'].describe()
    desc = desc[['min', '25%', "50%", "75%",'max']].values
    amount_cat = pd.cut(data['Amount Requested'], bins=desc, labels=[f'< {desc[1]}', f'{desc[1]} < val < {desc[2]}',f'{desc[2]} < val < {desc[3]}',f'>{desc[3]}'])
    val_cou = amount_cat.value_counts()

    fig = px.bar(x = val_cou.keys(), y = val_cou.values, color = val_cou.values)
    fig.update_layout(title_text=f"Amount Requested", xaxis_title="Amount Requested", yaxis_title="count")

    fig.show()
    if plot_wandb:
        save_plot(name = 'reject_amount_requested', plot = fig)
     


