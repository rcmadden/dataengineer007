from flask import Flask, render_template
# TODO: change to use url_for
app = Flask(__name__, static_url_path="/static", static_folder="static")
#app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

#if __name__ == '__main__':
#    app.debug = True  # TODO: Set to false on deployment
#:    app.run()


