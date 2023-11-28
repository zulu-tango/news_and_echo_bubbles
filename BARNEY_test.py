from preproc_base_data.pre_proc_pipe import concat_for_pre_built
from preproc_base_data.train_test_split import train_test_split
from preproc_base_data.pre_proc_pipe import pipe_for_pre_made_transformer_left, concat_for_pre_built
from preproc_base_data.data import get_data_left,get_data_right


# df_1 = concat_for_pre_built()

# print(train_test_split(dataframe=df_1))

<<<<<<< HEAD
print(concat_for_pre_built())
import pandas as pd
df = concat_for_pre_built()
df.to_csv('Data/cleaned_data.csv')
=======
if __name__ == "__main__":
    # print(get_data_right()['text'])
    print(concat_for_pre_built()['pre_process_text'].nunique())
    print(concat_for_pre_built())
>>>>>>> 7a90eda92fb4299854c7dd0389988be597df0f4f
