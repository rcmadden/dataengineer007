from flask import Flask, render_template
import os
# TODO: change to use url_for
app = Flask(__name__, static_url_path="/static", static_folder="static")
#app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

if __name__ == "__main__":
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)