import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>This is the home page served by Flask.</p>"

@app.route("/api/hello")
def hello_api():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)  # Default to 5000 if PORT isn't set
    app.run(debug=True, host="0.0.0.0", port=port)
