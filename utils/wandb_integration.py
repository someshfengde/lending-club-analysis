#%% 
import wandb as wandb
import time

#getting current time 

# wandb.login()

run = wandb.init(
        project ="Zest-AI",
        name = f"run at {time.time()}"
    )

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