from flask import Flask

app = Flask(__name__)

@app.route('/')
def starting():
    return "I am currently doing CI/CD pipeline using GitHub Action"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7645)