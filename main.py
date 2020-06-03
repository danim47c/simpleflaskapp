from flask import Flask, request, render_template, make_response, redirect

KEY = 'hola'

app = Flask(__name__)


@app.route('/')
def index():

    cookie = request.cookies.get('key')

    if not cookie:
        return render_template('index.html')

    else:
        return redirect('/privado')

@app.route('/privado')
def privado():
    cookie = request.cookies.get('key')

    if not cookie or cookie != KEY:
        return redirect('/')

    else:
        return render_template('private.html', key=KEY)

@app.route('/entrar', methods=['POST'])
def entrar():
    key = request.form.get('key')

    if key!=KEY:
        return redirect('/failed')

    else:
        response = make_response(redirect('/privado'))

        response.set_cookie('key', KEY)

        return response

@app.route('/failed')
def fallo():
    return render_template('failed.html')

@app.route('/salir')
def salir():
    response = make_response(redirect('/'))

    response.delete_cookie('key')

    return response


app.run(host='localhost', port=8080, debug=True)
