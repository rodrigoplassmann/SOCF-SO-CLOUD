from flask import Flask
import psutil
import os
import platform

APP = Flask(__name__)

@APP.get("/")
def index():
    nomes = "Rodrigo Schiavinatto Plassmann e Thomas Manussadjian Steinhausser"
    pid = os.getpid()
    memoria_mb = psutil.virtual_memory().used/1024 ** 2
    porcentagem_cpu = psutil.cpu_percent(interval=1)
    sistema_operacional = platform.platform()

    return f"""
        <h2>Nomes: {nomes}</h2>
        <h2>PID: {pid}</h2>
        <h2>Memória usada: {memoria_mb:.1f} MB</h2>
        <h2>CPU: {porcentagem_cpu}%</h2>
        <h2>Sistema operacional: {sistema_operacional}</h2>
    """

if __name__ == "__main__":
    APP.run(host = "0.0.0.0", port = 5000)