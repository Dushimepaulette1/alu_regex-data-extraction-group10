from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Regular expressions
patterns = {
    "Email": r"^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$",
    "URL": r"^(http:\/\/|https:\/\/)([a-z]+)\.([a-z]+)\.([a-z]{2,8})(\/[a-z]+)?$",
    "Phone Number": r"^(\(?)(\d{3})(\)?)([\s\.-]?)(\d{3})([-\.]?)(\d{4})$",
    "Credit Card": r"^((\d{4})([\s-]?))*$",
    "Time": r"^(\d{1,2}):(\d{2})(\s(PM|AM))?(\s\(\d{2}-([a-z]+)\s([a-z]+)\))?$",
    "HTML Tag": r"^<(\w+)(\s\w+="(\w\.?-?)+")*>$",
    "Hashtag": r"^\#(\w)+$",
    "Currency": r"^<(\w+)(\s\w+="(\w\.?-?)+")*>$"
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

