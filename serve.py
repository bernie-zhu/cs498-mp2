from flask import Flask, jsonify, request
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def route():
    if request.method == "GET":
        return socket.gethostbyname(socket.gethostname())
    elif request.method == "POST":
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "Created process for stress_cpu"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
