import psutil
from flask import Flask, render_template
from sys import platform

app = Flask(__name__)


@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)


if __name__ == '__main__':
    # if mac -> app.run(debug=True, host = '')
    # else -> app.run(debug=True, host = '0.0.0.0')
    if platform == "darwin":
        app.run(debug=True, host='')
    else:
        app.run(debug=True, host='0.0.0.0')