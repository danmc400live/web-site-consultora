from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/sendMail",methods=['POST'])
def sendMail():
    msg = ''
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    return render_template('index.html')

