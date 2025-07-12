import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <h1>Hello World from Railway!</h1>
    <p>This is a basic Python Flask app running on Railway.</p>
    <p>Environment: Railway Cloud</p>
    """

@app.route("/health")
def health_check():
    return {"status": "healthy", "message": "App is running!"}

if __name__ == "__main__":
    # Railway provides the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
