### !pip install tensorflow transformers
### need to make sure we have tensorflow installed in our environment????

##### import necessary packages #####
import os # needed to get environmental variables
import tensorflow as tf
from tensorflow.keras import optimizers, losses
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.datasets import load_iris
from datetime import datetime


##### get the ideology model (IM) environment variables #####
IM_MODEL_NAME = os.environ.get('IM_MODEL_NAME')
IM_BATCH_SIZE = int(os.environ.get('IM_BATCH_SIZE'))
IM_LEARNING_RATE = float(os.environ.get('IM_LEARNING_RATE'))
IM_TOKEN_MAX_LEN = int(os.environ.get('IM_TOKEN_MAX_LEN'))
IM_TEST_SPLIT = float(os.environ.get('IM_TEST_SPLIT'))
IM_VALIDATION_SPLIT = float(os.environ.get('IM_VALIDATION_SPLIT'))
IM_EPOCHS = int(os.environ.get('IM_EPOCHS'))
IM_PATIENCE = int(os.environ.get('IM_PATIENCE'))


def get_X_and_y(df):
    """
    Gets from our dataset: (i) the feature (i.e. X - the pre-processed text);
    and (ii) the target (i.e. y - the ideology: left wing = 0 / right wing = 1).
    These need to be converted into lists for use in our model.
    """

    X = df["pre_process_text"].tolist()
    y = df["classifier"].tolist()

    return X, y

###### SUGGESTIONS:
###### change "pre_process_text" to "preprocessed_text" or similar (in underlying pre-processed dataset)
###### change "classifier" to "ideology" or similar (in underlying pre-processed dataset)


def instantiate_tokenizer(model_name = IM_MODEL_NAME):
    """
    Define the tokenizer we want to use in our modelling.
    """

    tokenizer = DistilBertTokenizer.from_pretrained(model_name)

    return tokenizer


def text_tokenizer(X,
                   tokenizer,
                   max_len = IM_TOKEN_MAX_LEN,
                   truncation = True,
                   padding = "max_length"):
    """
    Returns a dictionary of tokenized text with 2 keys: "input_ids" and "attention_mask".
    These 2 keys are required for the input into the DistilBert model.
    """

    tokens = tokenizer(X, max_length = max_len, truncation = truncation, padding = padding)

    return tokens


def tf_dataset_constructor(tokens,
                           y):
    """
    Using the tokenized input from the text_tokenizer function,
    returns TensorFlow objects for use in the DistilBert model.
    """

    tfdataset = tf.data.Dataset.from_tensor_slices((dict(tokens),y))

    return tfdataset


def train_test_split(X,
                     tfdataset,
                     test_split = IM_TEST_SPLIT,
                     val_split = IM_VALIDATION_SPLIT,
                     batch_size = IM_BATCH_SIZE):
    """
    This function splits the TensorFlow object created in the tf_dataset_constructor function
    into train, valdiation and test sets.
    """

    # get the sizes of the train and validation sets
    train_size = int(len(X) * (1-test_split))
    val_size = int(train_size * val_split)

    # shuffle the full dataset
    tfdataset = tfdataset.shuffle(len(X))

    # from the full datset, get out the train, validation and test sets
    tfdataset_train = tfdataset.take(train_size)
    tfdataset_val = tfdataset.skip(train_size - val_size).take(val_size)
    tfdataset_test = tfdataset.skip(train_size)

    # batch the train, validation and test sets
    tfdataset_train = tfdataset_train.batch(batch_size)
    tfdataset_val = tfdataset_val.batch(batch_size)
    tfdataset_test = tfdataset_test.batch(batch_size)

    return tfdataset_train, tfdataset_val, tfdataset_test


def ideology_model(tfdataset_train,
                   tfdataset_val,
                   model_name = IM_MODEL_NAME,
                   learning_rate = IM_LEARNING_RATE,
                   batch_size = IM_BATCH_SIZE,
                   epochs = IM_EPOCHS,
                   patience = IM_PATIENCE,
                   save = 'yes'):

    """
    Set up an run a DistilBert model on our TensorFlow training dataset.
    """

    # set up model
    model = TFDistilBertForSequenceClassification.from_pretrained(model_name)

    # define loss function
    loss = losses.SparseCategoricalCrossentropy(from_logits=True)

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


    if save == 'yes':
        save_model(model)

    return model


def ideology_model_evaluator(model,
                             tfdataset_test,
                             batch_size = IM_BATCH_SIZE):
    """
    Evaluate our model on the TensorFlow test dataset
    """

    benchmarks = model.evaluate(tfdataset_test, batch_size = batch_size, return_dict = True)
    accuracy = benchmarks["accuracy"]

    return accuracy


def ideology_model_predictor(model,
                             tokens):
    """
    This function uses the model output from the ideology_model function to output the
    probabilities of each individual article being left or right wing (0 = left wing,
    1 = right wing). As the model spits out log odds rather than probabilities, these
    also need to be converted in this function into probabilities.
    """

    # firstly create a TensorFlow version of our tokenized dataset without our y
    tfdataset_no_y = tf.data.Dataset.from_tensor_slices(dict(tokens))

    # use this to get out the logits for our model
    pred_logits = model.predict(tfdataset_no_y)[0]

    # convert these into probabilties
    pred_probas = tf.nn.softmax(pred_logits).numpy()

    return pred_probas


def full_ideology_model(df):
    """
    Combine all above functions into one master function, except for the
    ideology_model_evaluator function, as we do not need the accuracy output here.
    """

    X, y = get_X_and_y(df)

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

    model = ideology_model(tfdataset_train,
                           tfdataset_val,
                           model_name = IM_MODEL_NAME,
                           learning_rate = IM_LEARNING_RATE,
                           batch_size = IM_BATCH_SIZE,
                           epochs = IM_EPOCHS,
                           patience = IM_PATIENCE)


    pred_probas = ideology_model_predictor(model, tokens)

    #add column back to orginal dataframe

    df['pred_probas'] = pred_probas[:,1]
    # return the second column, which shows the probability of the article being right-wing
    # a score near to 1 is very right wing; a score near to 0 is very left wing
    return df

def save_model(model):
    dt_string = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    model.save_pretrained(f"sentiment_model_{dt_string}")


def load_model(filename):

    # load model
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained(filename)
    return loaded_model
