from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Prompt Collector</title>
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
            <h3>Received Prompt:</h3>
            <pre>{{ prompt }}</pre>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = None
    if request.method == "POST":
        prompt = request.form["prompt"]
    return render_template_string(HTML_FORM, prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)

