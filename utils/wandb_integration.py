#%% 
import wandb as wandb
import time

#getting current time 

# run = wandb.init(
#         project ="Zest-AI",
#         name = f"run at {time.time()}"
#     )

def save_plot(name, plot):
    """
    saves plot to wandb
    inputs:
        name: name of the plot
        plot: plot to be saved
    outputs:
        None
    """
    wandb.log({name: plot})
    return None


def save_bar_plot(label , data, title = "", x_label = "", y_label=""):
    """
    this takes input as the labels and values and plots graph on wandb dashboard for
    input:
        label: labels for the values expects list
        data: values for the bars
    output:
        plots graphs to wandb
    """
    wandb_table_data = []
    for i in range(len(data)):
        wandb_table_data.append([label[i],data[i]])

    table = wandb.Table(data =wandb_table_data, columns=[x_label, y_label] )

    bar_plot = wandb.plot.bar(table, label = x_label,value = y_label, title=f"{title}")
    wandb.log({title :bar_plot })

    return None 


def save_plot_line(name ,
                    x , y ,
                    title = '',
                    x_label = '', y_label = ''):
    """
    this takes input as the labels and values and plots graph on wandb dashboard for
    input:
        name: name of the plot
        x: x axis values
        y: y axis values
        title: title of the plot
        x_label: x axis label
        y_label: y axis label
    output:
        plots graphs to wandb
    """
    data = [[x, y] for (x, y) in zip(x,y)]
    table = wandb.Table(data=data, columns = [x_label, y_label])
    wandb.log({f"{title}" : wandb.plot.line(table, x_label, y_label,
            title=f"{title}")})

    return None