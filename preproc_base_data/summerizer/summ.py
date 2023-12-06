from transformers import pipeline
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = TFAutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6", from_pt=True)

def sshleifer_summarize(text):
    # Encode the text
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)
    # Generate summary for the text
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

    return decoded_output

# print(sshleifer_summarize("""Former U.K. Prime Minister Boris Johnson will face a two-day grilling by the country’s official COVID-19 inquiry next week.

# Johnson will appear Wednesday, December 6 through Thursday, December 7 for a marathon session that will look at how his government handled the pandemic.

# It’s likely to be an uncomfortable time for Johnson, who was ousted as prime minister last year and has been the subject of damaging testimony at the inquiry so far as former aides and officials questioned his judgment and grip during the crisis.

# On Wednesday, Johnson’s former Health Secretary Sajid Javid asserted that top aide Dominic Cummings, and not Johnson himself, had been the real power in No.10 Downing Street as the virus raged.

# That was disputed by Dominic Raab, who served as Johnson’s deputy.

# The inquiry has also heard claims that Johnson veered from a pro- to anti-lockdown position at key moments; saw COVID-19 as “nature’s way of dealing with old people” — and even asked government medical advisers whether blowing a hairdryer up the nose could cure the virus"""))
