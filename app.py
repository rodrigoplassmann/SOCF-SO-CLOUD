from flask import Flask
import psutil
import os
import platform

APP = Flask(__name__)

@APP.get("/")
def index():
    return """
        <h2>Projeto II - Sistemas operacionais em cloud</h2>
        <p><a href="/info"><button>Info</button></a></p>
        <p><a href="/metricas"><button>Métricas</button></a></p>
      """

@APP.get("/info")
def info():
    return """
        <h2>Integrantes: Rodrigo Schiavinatto Plassmann e Thomas Manussadjian Steinhausser</h2>
        <a href="/"><button>Voltar</button></a>
    """

@APP.get("/metricas")
def metricas():
    nomes = "Rodrigo Schiavinatto Plassmann e Thomas Manussadjian Steinhausser"
    pid = os.getpid()
    memoria_mb = psutil.virtual_memory().used/1024 ** 2
    porcentagem_cpu = psutil.cpu_percent(interval=1)
    sistema_operacional = platform.platform()

    return {
        "nomes": nomes,
        "pid": pid,
        "memoria_mb": round(memoria_mb, 1),
        "porcentagem_cpu": porcentagem_cpu,
        "sistema_operacional": sistema_operacional
    }

if __name__ == "__main__":
    APP.run(host = "0.0.0.0", port = 5000)