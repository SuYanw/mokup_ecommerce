from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def default_page():
    return "You're not allowed to access this page"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4001, load_dotenv=True)