from flask import Flask
import subprocess

app = Flask(__name__)

print("Hello man")

@app.route("/")
def hello():
    subprocess.run(["docker", "service", "update", "--image", "mcr.microsoft.com/mssql/server:2017-latest-ubuntu", "8501086f25b6"])
    return "Hello, World!"