from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def sshleifer_summarize(text):
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
    # Encode the text
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)

    # Generate summary for the text
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)

    # Decode the output to get the summary
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded_output
