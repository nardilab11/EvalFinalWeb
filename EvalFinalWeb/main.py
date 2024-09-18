from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/calculocompras', methods=['GET', 'POST'])
def calculoCompras():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        porc = 0.0
        if edad >= 18 and edad <= 30:
            porc = 0.15
        elif edad > 30:
            porc = 0.25
        totalBruto = 9000 * tarros
        descuento = totalBruto * porc
        totalNeto = totalBruto - descuento
        return render_template('calculocompras.html', nombre=nombre, totalBruto=totalBruto, descuento=descuento, totalNeto=totalNeto)
    return render_template('calculocompras.html')

@app.route('/iniciosesion', methods=['GET', 'POST'])
def inicioSesion():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contra = str(request.form['contra'])
        mensaje = ""
        if nombre == "juan" and contra == "admin":
            mensaje = "Bienvenido Administrador juan"
        elif nombre == "pepe" and contra == "user":
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('iniciosesion.html', mensaje=mensaje)
    return render_template('iniciosesion.html')


if __name__ == '__main__':
    app.run(debug=True)