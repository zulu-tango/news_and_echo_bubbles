import tensorflow as tf
from tensorflow.keras import activations, optimizers, losses
from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification

def bert_tokenizer():
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
    