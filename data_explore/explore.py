# %% import data
import pandas as pd
data_path = "/home/wwj/src/L4S-LLM/llm_framework/data/exp_pools/exp_pool.csv"
df = pd.read_csv(data_path)

# %% explore data
print("info: ", df.info())
print("df.describe(): ", df.describe())
print("df.head(): ", df.head())
# %%
