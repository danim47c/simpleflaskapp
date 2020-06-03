from flask import Flask, request, make_response, render_template

app = Flask(__name__)

# main.py
@app.route('/')
def ruta():
    return render_template('index.html', nombre='Plantilla')
"""
# plantilla.html
<p>El nombre es: <b>{{ nombre }}</b></p>
"""
app.run(host='localhost', port=8080, debug=True)
