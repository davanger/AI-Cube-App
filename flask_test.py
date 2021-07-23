import random

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_url_path='/templates/briefcubing')

@app.route("/")
def home():
    return "Hello, World!"

    
@app.route("/cube_test")
def cube_test():
    cwd = os.getcwd()

    template_path = os.path.join("briefcubing", "index.html")
    return render_template("briefcubing/index.html")
    # return render_template("D:\EPITA\ActionLearning\CubeWeb\briefcubing\index.html")
    # return os.getcwd()
    

    # render test.html
    # concatenate os.getcwd() with template path
    
@app.route("/cube_test2")
def cube_test2():

    template_path = os.path.join("briefcubing", "index.html")
    return render_template("index2.html")

@app.route("/freecube")
def freecube():

    template_path = os.path.join("index.html")
    return render_template("freecube.html")

    # return render_template("D:\EPITA\ActionLearning\CubeWeb\briefcubing\index.html")
    # return os.getcwd()
    

    # render test.html
    # concatenate os.getcwd() with template path

@app.route("/bluetooth")
def bluetooth():
    return render_template("bluetooth.html")

@app.route("/briefcubing/<path:path>")
def briefcubing_static_dir(path):
    return send_from_directory("briefcubing/", path)

@app.route("/freecube/<path:path>")
def freecube_static_dir(path):
    return send_from_directory("freecube/", path)

@app.route("/images/<path:path>")
def images_static_dir(path):
    return send_from_directory("images/", path)

@app.route("/solve/<string:scramble>")
def solve_for(scramble):
    return render_template("solve_for.html", scramble=scramble)

@app.route("/solve/<string:step>/<string:scramble>")
def solve(step, scramble):
    return render_template("solve.html", scramble=scramble, step=step)

@app.route("/get_scramble/")
def get_scramble():
    file_path = "scrambles.txt"
    scramble = ""
    with open(file_path) as f:
        lines = f.readlines()
        scramble = lines[random.randint(0, len(lines)-1)].replace("\n", "")
    return scramble


if __name__ == "__main__":
    app.run(debug=True)