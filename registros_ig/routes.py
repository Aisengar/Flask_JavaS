from registros_ig import app

@app.route("/")
def inder():
    return "servidor levantado!!"