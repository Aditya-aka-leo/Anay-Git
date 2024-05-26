from flask import Flask, request
from flask_cors import CORS  # Import CORS extension
from genre_classf_CNN import genre

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    url = request.args.get('url')
    print(url)
    if url:
        return genre(url)
    else:
        return "No URL provided."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
