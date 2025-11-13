from flask import Flask, jsonify
import psutil
import os
import platform

APP = Flask(__name__)

# Variáveis globais
INTEGRANTES = "Rodrigo Schiavinatto Plassmann e Thomas Manussadjian Steinhausser"
PID = os.getpid()
SISTEMA = platform.platform()

# Função para coletar métricas dinâmicas
def coletar_metricas():
    memoria_mb = psutil.virtual_memory().used/1024 ** 2
    porcentagem_cpu = psutil.cpu_percent(interval=1)

    return {
        "integrantes": INTEGRANTES,
        "pid": PID,
        "memoria_mb": round(memoria_mb, 1),
        "cpu_percent": cpu_percent,
        "sistema_operacional": SISTEMA
    }

@APP.get("/")
def index():
    m = coletar_metricas()
    return f"""
        <h2>Projeto II - Sistemas Operacionais em Cloud</h2>

        <h3>Métricas atuais</h3>
        <p><b>Integrantes:</b> {m['integrantes']}</p>
        <p><b>PID do processo:</b> {m['pid']}</p>
        <p><b>Memória utilizada (MB):</b> {m['memoria_mb']}</p>
        <p><b>Uso de CPU (%):</b> {m['cpu_percent']}</p>
        <p><b>Sistema operacional:</b> {m['sistema_operacional']}</p>

        <p><a href="/info"><button>Info (JSON)</button></a></p>
        <p><a href="/metricas"><button>Métricas (JSON)</button></a></p>
    """

@APP.get("/info")
def info():
    return jsonify({"integrantes": INTEGRANTES})

@APP.get("/metricas")
def metricas():
    return jsonify(coletar_metricas())

if __name__ == "__main__":
    APP.run(host = "0.0.0.0", port = 5000)