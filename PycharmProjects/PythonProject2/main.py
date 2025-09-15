from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "Hello flask!"

if __name__ == "__main__":
    app.run()


@app.route('/hello/<name>/')
def hello(name):
    return render_template("main.html", name=name)


@app.route('/myform', methods=["POST", "GET"])
def get_data():
    print("Reading data")
    print(request.form["form_name"])
    return "Success"