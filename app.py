from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    db_password = os.getenv("DB_PASSWORD", "NOT_SET")
    return f"Harness Helm Deployment Success! Secret Length: {len(db_password)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
