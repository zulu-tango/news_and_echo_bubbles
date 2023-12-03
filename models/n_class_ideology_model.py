### !pip install tensorflow transformers
### need to make sure we have tensorflow installed in our environment????

##### import necessary packages #####
import os # needed to get environmental variables
import numpy as np
import tensorflow as tf
from tensorflow.keras import optimizers, losses
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
from tensorflow.keras.callbacks import EarlyStopping


##### get the ideology model (IM) environment variables #####
##### cast the variables to int / float where necessary #####
IM_MODEL_NAME = os.environ.get('IM_MODEL_NAME')
IM_BATCH_SIZE = int(os.environ.get('IM_BATCH_SIZE'))
IM_LEARNING_RATE = float(os.environ.get('IM_LEARNING_RATE'))
IM_TOKEN_MAX_LEN = int(os.environ.get('IM_TOKEN_MAX_LEN'))
IM_TEST_SPLIT = float(os.environ.get('IM_TEST_SPLIT'))
IM_VALIDATION_SPLIT = float(os.environ.get('IM_VALIDATION_SPLIT'))
IM_EPOCHS = int(os.environ.get('IM_EPOCHS'))
IM_PATIENCE = int(os.environ.get('IM_PATIENCE'))


from models.ideology_model import instantiate_tokenizer, text_tokenizer, tf_dataset_constructor,\
    train_test_split, ideology_model_evaluator, ideology_model_predictor

n = 5 # n being the number of classes into which we divide polticial ideology
####### n = 3 is left / centre / right
####### n = 5 is left / leans left / centre / leans right / right

### Here I define the mapping dictionaries for 3 and 5 way splits
### In theory, we should use One Hot Encoding, BUT this gives out extra columns which I don't want
### What I actually want is all of these binary values to be a list within a single target column

three_hot_dict = {-1 : [1,0,0],
                  0 : [0,1,0],
                  1 : [0,0,1]}

five_hot_dict = {-2 : [1,0,0,0,0],
                 -1 : [0,1,0,0,0],
                 0 : [0,0,1,0,0],
                 1 : [0,0,0,1,0],
                 2 : [0,0,0,0,1]}


def bias_score_encoding(df, n):

    if n == 5:
        df["one_hot_discrete"] = df["5_step_classifier"].map(five_hot_dict)

    if n == 3:
        df["one_hot_discrete"] = df["3_step_classifier"].map(three_hot_dict)

    return df


def n_class_get_X_and_y(df):
    """
    Get the X and y model inputs for our model from our dataframe.
    These need to be converted into lists for use in our model.
    """

    X = df["pre_process_text"].tolist()
    y = df["one_hot_discrete"].tolist()

    return X, y


def n_class_ideology_model(tfdataset_train,
                           tfdataset_val,
                           n,
                           model_name = IM_MODEL_NAME,
                           learning_rate = IM_LEARNING_RATE,
                           batch_size = IM_BATCH_SIZE,
                           epochs = IM_EPOCHS,
                           patience = IM_PATIENCE):

    """
    Set up an run a DistilBert model on our TensorFlow training dataset.
    Changing the loss in this version to a "BinaryCrossentropy" loss
    """

    # set up model
    model = TFDistilBertForSequenceClassification.from_pretrained(model_name, num_labels = n)

    # define loss function
    loss = losses.BinaryCrossentropy(from_logits=True)

    # define optimizer to be used to minimise loss
    optimizer = optimizers.Adam(learning_rate)

    # compile model
    model.compile(optimizer = optimizer,
                  loss = loss,
                  metrics = "accuracy")

    # fit model
    model.fit(tfdataset_train,
              batch_size = batch_size,
              epochs = epochs,
              validation_data = tfdataset_val,
              callbacks = EarlyStopping(patience = patience, restore_best_weights = True))

    save_model_5(model)
    print('model saved')

    return model


def top_class(pred_probas):
    """
    This function looks at the array of predicted probabilites for each article and outputs
    the ideology corresponding to the highest probability
    """

    top_class_list = []

    for row in range(len(pred_probas)):

        conversion_dict = {0 : "left",
                       1 : "leans left",
                       2 : "centre",
                       3 : "leans right",
                       4 : "right"}

        top_class_list.append(conversion_dict[np.argmax(pred_probas[row])])

    return top_class_list


def full_n_class_ideology_model(df, n):

    """
    Combine above functions into one master function.
    """
    df = bias_score_encoding(df, n)
    X, y = n_class_get_X_and_y(df)
    tokenizer = instantiate_tokenizer(model_name = IM_MODEL_NAME)
    tokens = text_tokenizer(X,
                            tokenizer,
                            max_len = IM_TOKEN_MAX_LEN,
                            truncation = True,
                            padding = "max_length")
    tfdataset = tf_dataset_constructor(tokens, y)

    # the following function automatically returns the test dataset, even though this is
    # not used further, as we do not evaluate the model accuracy within this function.

    tfdataset_train, tfdataset_val, tfdataset_test =\
    train_test_split(X,
                    tfdataset,
                    test_split = IM_TEST_SPLIT,
                    val_split = IM_VALIDATION_SPLIT,
                    batch_size = IM_BATCH_SIZE)

    model = n_class_ideology_model(tfdataset_train,
                                   tfdataset_val,
                                   n,
                                   model_name = IM_MODEL_NAME,
                                   learning_rate = IM_LEARNING_RATE,
                                   batch_size = IM_BATCH_SIZE,
                                   epochs = IM_EPOCHS,
                                   patience = IM_PATIENCE)

    pred_probas = ideology_model_predictor(model, tokens)
    top_class_list = top_class(pred_probas)
    df['pred_class'] = top_class_list

    return df

def save_model_5(model):
    model.save_pretrained(f"sentiment_model_saturday_5")



