from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import openai
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Code Generator Assistant</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #fefae0;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            padding-top: 40px;
        }
        .header img {
            width: 100px;
            opacity: 0.8;
        }
        .container {
            max-width: 600px;
            margin: 30px auto;
            background-color: #ffffff;
            padding: 30px 40px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        label {
            font-weight: 600;
            font-size: 18px;
            color: #283618;
        }
        input[type="text"] {
            padding: 12px;
            width: 80%;
            margin-top: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
        }
        input[type="submit"] {
            margin-top: 20px;
            padding: 12px 28px;
            background-color: #606c38;
            border: none;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        input[type="submit"]:hover {
            background-color: #4a5a27;
        }
        h3 {
            margin-top: 30px;
            color: #283618;
        }
        pre {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 8px;
            white-space: pre-wrap;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://cdn-icons-png.flaticon.com/512/1087/1087923.png" alt="Prompt Icon">
    </div>
    <div class="container">
        <form method="POST">
            <label for="prompt">Enter your prompt:</label><br>
            <input type="text" id="prompt" name="prompt"><br>
            <input type="submit" value="Submit">
        </form>
        {% if prompt %}
            <h3>Prompt:</h3>
            <pre>{{ prompt }}</pre>
        {% endif %}
        {% if title %}
            <h3>Generated Title:</h3>
            <pre>{{ title }}</pre>
        {% endif %}
        {% if code %}
            <h3>Generated Code:</h3>
            <pre>{{ code }}</pre>
        {% endif %}
    </div>
</body>
</html>
"""

system_prompt = """You are a coding assistant.

IMPORTANT:
- You MUST fill the fields: 'detail', 'compact', and 'video'.
- 'detail' must contain detailed step-by-step information based on the user's request.
- 'compact' must contain a one-sentence summary of the whole task.
- 'video' must contain the list of steps describing how the task was done.
- DO NOT leave any of these fields empty.
- Before the code, write a meaningful title inside [ ] brackets. 
- After the title, generate Python code in the following structure:

from s4e.config import *
from s4e.task import Task

class Job(Task):
    def run(self):
        asset = self.asset
        self.output['detail'] = [detailed items here]
        self.output['compact'] = [compact summary here]
        self.output['video'] = [step-by-step actions here]

        # Actual code solving the user's request

    def calculate_score(self):
        # Set a score based on task complexity:
        # Example: Easy task = 2, Medium = 5, Hard = 8, Critical = max_score
        self.score = self.param['max_score']

Respond exactly in this format.

NEVER leave 'detail', 'compact', or 'video' empty.
"""

def generate_code_and_title(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        content = response.choices[0].message.content
        lines = content.split("\n")
        title = lines[0].strip()
        code = "\n".join(lines[2:]).strip("`")
        return title, code
    except Exception as e:
        return "Error", f"OpenAI API Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = title = code = None
    if request.method == "POST":
        prompt = request.form.get("prompt", "")
        if prompt:
            title, code = generate_code_and_title(prompt)
    return render_template_string(HTML_FORM, prompt=prompt, title=title, code=code)

if __name__ == "__main__":
    app.run(debug=True)

