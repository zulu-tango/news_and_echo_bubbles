from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_chunks(inp_str):
    max_chunk = 500
    inp_str = inp_str.replace('.', '.<eos>')
    inp_str = inp_str.replace('?', '?<eos>')
    inp_str = inp_str.replace('!', '!<eos>')

    sentences = inp_str.split('<eos>')
    current_chunk = 0
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1:
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    return chunks

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    sentence = data.get('sentence')
    max_length = data.get('max_length', 150)
    min_length = data.get('min_length', 50)
    do_sample = data.get('do_sample', False)

    chunks = generate_chunks(sentence)
    result = summarizer(chunks,
                        max_length=max_length,
                        min_length=min_length,
                        do_sample=do_sample)

    summary = ' '.join([summ['summary_text'] for summ in result])
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(port=8000)
