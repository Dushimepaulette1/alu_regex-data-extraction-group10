from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Regular expressions
patterns = {
    "Email": r"^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$",
    "URL": r"https?://[\w\.-]+(?:\.[\w\.-]+)+[/\w\.-]*",
    "Phone Number": r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",
    "Credit Card": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "Time (24-hour)": r"\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b",
    "Time (12-hour)": r"\b(1[0-2]|0?[1-9]):[0-5][0-9]\s?[APMapm]{2}\b",
    "HTML Tag": r"<[^>]+>",
    "Hashtag": r"#\w+",
    "Currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_input():
    user_input = request.form['user_input']
    results = {key: re.findall(pattern, user_input) for key, pattern in patterns.items()}
    return render_template('result.html', results=results, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)

