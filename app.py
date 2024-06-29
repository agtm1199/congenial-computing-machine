from flask import Flask

app = Flask('basic app')

@app.route("/")
def main():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
    )