#%%
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from utils.wandb_integration import *
import plotly.express as px


def preprocess_df(df):
    """
    preprocess the selecting particular cols from whole dataframe 
    
    """

    final_features = ['addr_state', 'annual_inc', 'earliest_cr_line', 'emp_length', 'emp_title', 'fico_range_high', 'fico_range_low', 'grade', 'home_ownership', 'application_type',
                    'initial_list_status', 'int_rate', 'loan_amnt', 'num_actv_bc_tl', 'loan_status', 'mort_acc', 'tot_cur_bal', 'open_acc', 'pub_rec', 'pub_rec_bankruptcies', 
                    'purpose', 'revol_bal', 'revol_util', 'sub_grade', 'term', 'title', 'total_acc', 'verification_status']

    df = df[final_features]
    return df 

def plot_categotical_features_accept(data, plot_wandb = False):
    """
    this function plots the categorical features in the dataframe.
    input: 
        data: dataframe
    output: 
        various categorical plots present in dataframe
    """
    data = preprocess_df(data)
    cat_cols = ['addr_state',
    'earliest_cr_line',
    'emp_length',
    'emp_title',    
    'grade',
    'home_ownership',
    'application_type',
    'initial_list_status',
    'loan_status',
    'purpose',
    'sub_grade',
    'term',
    'title',
    'verification_status']

    for x in cat_cols:
        # value coutns doesnt include NAN values
        filtered_num = data[x].value_counts() 
        if len(filtered_num) > 15 :
            fig = px.bar(x = filtered_num[:15].keys(), y = filtered_num[:15].values, color = filtered_num[:15].values)
            fig.update_layout(title = f'{x} top 15 values', 
                            xaxis_title = x,
                            yaxis_title = 'count')
            fig.show()


            if plot_wandb:
                save_plot(name = f'{x}_top_15_values', plot = fig)
                
        else:
            fig = px.bar(x = filtered_num.keys(), y = filtered_num.values, color = filtered_num.values)
            fig.update_layout(title = f'{x}', 
                            xaxis_title = x,
                            yaxis_title = 'count')
            fig.show()

            if plot_wandb:
                save_plot(name = f'{x}', plot = fig)
    
    return None 

def other_plots(df, plot_wandb= False):
    """
    shows other plots for accpeted dataframe
    inputs:
        df: dataframe
    outputs:
        differnt plots

    income less than 25k is considered in following graphs
    """
    df = preprocess_df(df)
    plot_annual_income(df, plot_wandb)
    # draw correletion df 
    draw_correletion_plot(df, plot_wandb)
    # plotting the loan status vs annual income
    earliest_cr_line_plot(df, plot_wandb)
    return None 


def earliest_cr_line_plot(df,plot_wandb = False):
    cf = df.copy()
    cf['earliest_cr_line'] = cf['earliest_cr_line'].dropna().apply(lambda date: int(date[-4:]))
    fig = plt.figure(figsize=(10,6))
    plot= sns.displot(data=cf, x='earliest_cr_line', hue='loan_status', bins=100, height=4, aspect=3, kde=True, palette='viridis')
    plt.title('loan_status vs annual income < 25k ')
    plt.xlabel("earliest_cr_line")
    plt.ylabel("loan_status")
    plt.show()
    if plot_wandb:
                save_plot(name = 'loan_status vs annual income < 25k', plot = plt)
    del cf

    return None 

def plot_annual_income(df,plot_wandb = False):
    df_con = df[df['annual_inc'] <= 250000].copy()
    # plot the density curve for annyal distribution
    fig = plt.figure(figsize=(10,6))
    plot = sns.distplot(x=df_con['annual_inc'])
    plt.title("Annual income distribution < 25k ")
    plt.xlabel("annual income")
    plt.ylabel("count")
    plt.show()
    if plot_wandb:
                save_plot(name = 'Annual income distribution < 25k', plot = plt)

    # checking distribution for people who paid loan fully and charged off 
    fig = plt.figure(figsize=(10,6))
    plot = sns.displot(data=df_con, x='annual_inc', hue='loan_status', bins=80, height=5, aspect=3, kde=True, palette='viridis');
    plt.title("plot for fully paid and charged off")
    plt.xlabel("annual income")
    plt.ylabel("loan_status")
    plt.show()
    if plot_wandb:
                save_plot(name = 'plot for fully paid and charged off', plot = plt)
    del df_con # saving some space 
    return plot 


def draw_correletion_plot(df,plot_wandb = False):
    """
    draws correletion plot with respect to other features in dataframe 
    """
    # loan status correletion with other features
    df_temp = df.copy()
    df_temp = df_temp[(df_temp['loan_status'] == 'Fully Paid') | (df_temp['loan_status'] == 'Charged Off')]
    df_temp['loan_status'] = pd.get_dummies(df_temp['loan_status'], drop_first=True)
    fig = plt.figure(figsize=(10,6))
    plot = df_temp.corr()['loan_status'].sort_values().drop('loan_status').plot(kind='bar', cmap='viridis') # correlation with loan_status for continuous features with loan_status feature dropped
    plt.xticks(rotation=90)
    plt.title("correletion between loan satus and other features")
    plt.xlabel("features")
    plt.ylabel("correletion")
    plt.show()
    if plot_wandb:
                save_plot(name = 'correletion between loan satus and other features', plot = plt)
    del df_temp # deleting temp datafrmae to free up memory

    return plot
