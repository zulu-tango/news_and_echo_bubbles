from flask import Flask, request, jsonify
from preproc_base_data.summerizer.summ import sshleifer_summarize

app = Flask(__name__) # creates a Flask web application instance.

@app.route('/summarize', methods=['POST']) #define a endpoint /summarize
def summarize():
    data = request.get_json()
    text = data['text']
    summary = sshleifer_summarize(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
