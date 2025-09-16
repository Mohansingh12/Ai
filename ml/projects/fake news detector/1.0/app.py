from flask import Flask, render_template, request, jsonify
from api import get_answer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/get_answer', methods=['POST'])
def api_get_answer():
    try:
        data = request.get_json(silent=True) or {}
        question = data.get('question', '')
        if not question or not isinstance(question, str):
            return jsonify({"error": "Invalid or missing 'question'"}), 400

        result = get_answer(question)

        if isinstance(result, dict):
            answer_text = result.get('response') or result.get('message') or str(result)
        else:
            answer_text = str(result)

        return jsonify({"answer": answer_text})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

if __name__ == '__main__':
    app.run(debug=True)
