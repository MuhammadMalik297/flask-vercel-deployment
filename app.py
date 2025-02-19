from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Deploying Flask App at Vercel - i21-2688 by Muhammad Malik"

if __name__ == "__main__":
    app.run(debug=True)
