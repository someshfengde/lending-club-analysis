#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
from wandb_integration import * 
# import wandb 
plt.style.use("ggplot")


#%%
reject = pd.read_csv("../data/reject_sample.csv")

#%%

# rejection applicatoinl date year wise 
def plot_reject_yearwise(data, plot_wandb = False):
    year_wise = data['Application Date'].apply(lambda x: x.split('-')[0]).value_counts()
    year_wise = year_wise.sort_index()
    year_wise = year_wise.reset_index()
    year_wise.columns = ['year', 'count']
    year_wise['year'] = year_wise['year'].astype(int)
    year_wise = year_wise.sort_values(by = 'year')
    plt.plot(year_wise['year'], year_wise['count'], color = 'green')
    plt.title('Rejection Application Year Wise')
    plt.xlabel('year')
    plt.ylabel('count')
    plt.show()
    if plot_wandb:
        # save_plot(name = 'Rejection Application Year Wise' , plot = plt)
        save_plot_line(name = 'Rejection Application Year Wise' , x = year_wise['year'], y = year_wise['count'], title = 'Rejection Application Year Wise', x_label = 'year', y_label = 'count')

plot_reject_yearwise(reject, plot_wandb = True)
#%%

    

#%%
# plotting loan title with the requested categories 
def plot_loan_title_category(data, plot_wandb= False ):
    data_counts = data['Loan Title'].value_counts()
    fig = plt.figure(figsize= (10,5))
    plt.title("top 10 rejected loan titles")
    plt.xlabel("loan title")
    plt.ylabel("count")
    plt.bar(x = data_counts[:10].keys(), height = data_counts[:10].values)
    plt.xticks(rotation=90)
    plt.show()
    if plot_wandb:
        # wandb.log({"top 10 rejected loan titles":fig})
        save_bar_plot(label = list(data_counts[:10].keys()),data = data_counts[:10].values, title = 'top 10 rejected loan titles', x_label = 'loan title', y_label = 'count')

    fig = plt.figure(figsize = (10,5))
    plt.title("least rejected loan titles")
    plt.xlabel("loan title")
    plt.ylabel("count")
    plt.bar(x = data_counts[-10:].keys(), height = data_counts[-10:].values)
    plt.xticks(rotation=90)
    plt.show()
    if plot_wandb:
        # wandb.log({"least rejected loan titles":fig})
        save_bar_plot(label = list(data_counts[-10:].keys()), data = data_counts[-10:].values, title = 'least rejected loan titles', x_label = 'loan title', y_label = 'count')

    return 

plot_loan_title_category(reject, plot_wandb = True)

#%%

# plotting risk score 
def plot_risk_score_category(data, plot_wandb = False):
    null_vals = data['Risk_Score'].isna().sum()/len(data['Risk_Score'])* 100
    desc = data['Risk_Score'].describe()
    desc = desc[['min', '25%', "50%", "75%",'max']].values
    risk_cat = pd.cut(data['Risk_Score'], bins=desc, labels=[f'< {desc[1]}', f'{desc[1]} < val < {desc[2]}',f'{desc[2]} < val < {desc[3]}',f'>{desc[3]}'])
    val_cou = risk_cat.value_counts()
    fig = plt.figure()
    plt.bar(x = val_cou.keys(),height =  val_cou.values)
    plt.xticks(rotation=90)
    plt.title(f"Risk Score \n there are {null_vals:.2f}% null values")
    if plot_wandb:
        # wandb.log({f"Risk Score \n there are {null_vals:.2f}% null values":fig})
        save_bar_plot(label = list(val_cou.keys()), data = val_cou.values, title = 'Risk Score', x_label = 'Risk Score', y_label = 'count')
    return 


#%%

# plotting states with most rejected applications

def plot_state_category(data, plot_wandb = False):
    data = data['State'].value_counts()
    fig = plt.figure(figsize = (10,5))
    plt.title("top 10 rejected application states")
    plt.xlabel("state")
    plt.ylabel("count")
    plt.bar(x = data[:10].keys(), height = data[:10].values)
    plt.show() 
    if plot_wandb:
        # wandb.log({"top 10 rejected application states":fig})
        save_bar_plot(label = list(data[:10].keys()), data = data[:10].values, title = 'top 10 rejected application states', x_label = 'state', y_label = 'count')

#%%

# plotting employment length
def plot_employment_length_category(data, plot_wandb = False):
    data = data['Employment Length'].value_counts()
    fig = plt.figure(figsize = (10,5))
    plt.title("rejected application reletion with employment length")
    plt.xlabel("Employment Length")
    plt.ylabel("count")
    plt.bar(x = data.keys(), height = data.values)
    plt.show()
    if plot_wandb:
        # wandb.log({"rejected application reletion with employment length":fig})
        save_bar_plot(label = list(data.keys()), data = data.values, title = 'rejected application reletion with employment length', x_label = 'Employment Length', y_label = 'count')
    print("here we can observe that we are < 1 year emp length are getting rejected most")

#%% 
# plotting most rejected application policy Code wise 
def plot_policy_code_category(data, plot_wandb=False):
    data = data['Policy Code'].value_counts()
    fig = plt.figure(figsize = (10,5))
    plt.title("top 10 rejected application policy code")
    plt.xlabel("policy code")
    plt.ylabel("count")
    plt.bar(x = data.keys(), height = data.values)
    plt.show()
    if plot_wandb:
        # wandb.log({"top 10 rejected application policy code":fig})
        save_bar_plot(label = list(data.keys()), data = data.values, title = 'top 10 rejected application policy code', x_label = 'policy code', y_label = 'count')


#%%
def plot_amount_requested_category(data, plot_wandb = False ):
    desc = data['Amount Requested'].describe()
    desc = desc[['min', '25%', "50%", "75%",'max']].values
    amount_cat = pd.cut(data['Amount Requested'], bins=desc, labels=[f'< {desc[1]}', f'{desc[1]} < val < {desc[2]}',f'{desc[2]} < val < {desc[3]}',f'>{desc[3]}'])
    val_cou = amount_cat.value_counts()
    fig = plt.figure(figsize = (10,5))
    plt.bar(x = val_cou.keys(),height =  val_cou.values)
    plt.xticks(rotation=90)
    plt.title("Amount Requested")
    plt.show()
    if plot_wandb:
        # wandb.log({"Amount Requested":fig})
        save_bar_plot(label = list(val_cou.keys()), data = val_cou.values, title = 'Amount Requested', x_label = 'Amount Requested', y_label = 'count')