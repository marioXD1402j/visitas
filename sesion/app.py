from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/', methods=['GET'])
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form.get('profesion', 'No especificada')
    
    return redirect(url_for('futuro'))

@app.route('/futuro', methods=['GET'])
def futuro():
    nombre = session.get('nombre', 'Desconocido')
    lugar = session.get('lugar', 'un lugar misterioso')
    numero = session.get('numero', 'X')
    comida = session.get('comida', 'una comida deliciosa')
    profesion = session.get('profesion', 'desempleado')
    
    
    mensajes = [
        f"Soy el adivino del Dojo, {nombre} tendrá un viaje muy largo dentro de {numero} años a {lugar} y estará el resto de sus días preparando {comida} para todas las personas que quiere.",
        f"Soy el adivino del Dojo, {nombre} tendrá {numero} años de mala suerte, nunca conocerá {lugar} y jamás volvió a comer {comida}."
    ]
    mensaje = random.choice(mensajes)
    
    return render_template('futuro.html', mensaje=mensaje, profesion=profesion)

if __name__ == '__main__':
    app.run(debug=True)
