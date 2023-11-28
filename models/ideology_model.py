### !pip install tensorflow transformers
### need to make sure we have tensorflow installed in our environment????


##### import necessary packages #####
import tensorflow as tf
from tensorflow.keras import optimizers, losses
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
from tensorflow.keras.callbacks import EarlyStopping


##### define environment variables #####
BATCH_SIZE = 2
LEARNING_RATE = 3e-5
TOKEN_MAX_LEN = 50   ### currently set at 50 to speed up basic model training
TEST_SPLIT = 0.2
VALIDATION_SPLIT = 0.3   ### refers to split withing training data (not whole dataset)
EPOCHS = 5   ### currently set to 5 to speed up basic model training
PATIENCE = 2   ### currently set to 2 due to the low number of epochs (5)


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


# defining the tokenizer here so that it can be changed later
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")


def text_tokenizer(X,
                   tokenizer,
                   max_len = TOKEN_MAX_LEN,
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
                     test_split = TEST_SPLIT,
                     val_split = VALIDATION_SPLIT,
                     batch_size = BATCH_SIZE):
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
                   model_name = "distilbert-base-uncased",
                   learning_rate = LEARNING_RATE,
                   batch_size = BATCH_SIZE,
                   epochs = EPOCHS,
                   patience = PATIENCE):

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
              callbacks = EarlyStopping(patience = PATIENCE, restore_best_weights = True))

    return model


def ideology_model_evaluator(model,
                             tfdataset_test,
                             batch_size = BATCH_SIZE):
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
