from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/', methods=['GET'])
def index():
    
    if 'visitas' not in session:
        session['visitas'] = 0
    if 'reinicios' not in session:
        session['reinicios'] = 0
    
    
    session['visitas'] += 1
    
    visitas = session.get('visitas', 0)
    reinicios = session.get('reinicios', 0)
    
    return render_template('index.html', visitas=visitas, reinicios=reinicios)

@app.route('/destruir_sesion', methods=['GET'])
def destruir_sesion():
    
    session.clear()  
    return redirect(url_for('index'))

@app.route('/aumentar', methods=['POST'])
def aumentar():                 
    if 'visitas' in session:
        session['visitas'] += 2
    return redirect(url_for('index'))

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    session['visitas'] = 0
    session['reinicios'] += 1
    return redirect(url_for('index'))

@app.route('/incrementar', methods=['POST'])
def incrementar():
    try:
        incremento = int(request.form['incremento'])
        if 'visitas' in session:
            session['visitas'] += incremento
    except ValueError:
        pass                            
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
