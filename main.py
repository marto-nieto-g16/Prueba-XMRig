from flask import Flask, render_template
import subprocess

app = Flask(__name__)

ruta_xmrig = "xmrig"  # Reemplaza con la ruta correcta a tu ejecutable XMRig
archivo_config = "config.json"  # Reemplaza con la ruta correcta a tu archivo de configuración

@app.route("/")
def inicio():
    return "¡Bienvenido a tu aplicación web de minería con XMRig!"

@app.route("/iniciar_mineria")
def iniciar_mineria():
    try:
        proceso_xmrig = subprocess.Popen([ruta_xmrig, "--config", archivo_config], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proceso_xmrig.communicate()
        if stderr:
            return f"Error al iniciar XMRig: {stderr.decode()}"
        else:
            return "XMRig iniciado correctamente."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
