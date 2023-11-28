from preproc_base_data.pre_proc_pipe import concat_for_pre_built
from preproc_base_data.train_test_split import train_test_split
from preproc_base_data.pre_proc_pipe import pipe_for_pre_made_transformer_left, concat_for_pre_built

# df_1 = concat_for_pre_built()

# print(train_test_split(dataframe=df_1))

print(concat_for_pre_built())
import pandas as pd
df = concat_for_pre_built()
df.to_csv('Data/cleaned_data.csv')
