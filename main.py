from flask import Flask, render_template, url_for, redirect, request, session, jsonify

import statements as st

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

class User():
    def __init__(self, nombre, correo, numero, cedula, pais):
        self.nombre = nombre
        self.correo = correo
        self.numero = numero
        self.cedula = cedula
        self.pais = pais

class var():
    opcion_correcta = True
    fin_opciones = False
    answer_user = []
    actual_message = ''
    bloqueo = 1
    messages = []

@app.route('/') 
def index():
    return redirect('/login')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    # response = [False, '']
    if request.method == 'POST':
        rq = request.form
        var.user = User(rq['nombre'], rq['correo'], rq['numero'], rq['cedula'], rq['pais'])

        var.messages.append({'from':'bot', 
                             'msg':['Hola '+rq['nombre']+' soy Sonybot, ¿En que te puedo ayudar?']})
        return redirect('/chat')
    return render_template('login.html', alert = '')

@app.route('/chat')
def chat():
    return render_template('chat.html', messages = var.messages)

@app.route('/salir')
def salir():
    var.messages.clear()
    return redirect('/login')

def format(txt):
    return txt.split('\n')

def incorrect():
    var.actual_message = 'Opcion incorrecta'
    var.opcion_correcta = False

@app.route('/backChat')
def backChat():
    if len(var.answer_user) > 0:
        var.answer_user.pop()
    
    if len(var.messages) > 1:
        var.messages.pop()
        var.messages.pop()
    return redirect('/chat')

@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    var.opcion_correcta = True
    var.actual_message = ''

    if request.method == 'POST' and request.form['message'] != '':
        var.answer_user.append(request.form['message'])
        print(var.answer_user)

        try:
            if var.answer_user[0] != '':
                var.actual_message = st.menu_inicial

                match var.answer_user[1]:
                    case 'a': 
                        var.actual_message = st.producto_fallas
                        match var.answer_user[2]:
                            case 'a': 
                                var.actual_message = st.falla_tv
                                match var.answer_user[3]:
                                    case 'a': var.actual_message = st.tv_control
                                    case 'b': var.actual_message = st.tv_imagen
                                    case 'c': var.actual_message = st.tv_audio
                                    case _: incorrect()
                            case 'b': 
                                var.actual_message = st.falla_camara
                                match var.answer_user[3]:
                                    case 'a': var.actual_message = st.cam_compatibilidad
                                    case 'b': var.actual_message = st.cam_webcam
                                    case 'c': var.actual_message = st.cam_calidadFotos
                                    case _: incorrect()
                            case 'c': 
                                var.actual_message = st.falla_ps
                                match var.answer_user[3]:
                                    case 'a': var.actual_message = st.ps_actualizacion
                                    case 'b': var.actual_message = st.ps_no_enciende
                                    case 'c': var.actual_message = st.ps_no_reconoce
                                    case _: incorrect()
                            case 'd': 
                                var.actual_message = st.falla_celular
                                match var.answer_user[3]:
                                    case 'a': var.actual_message = st.cel_actualizacion
                                    case 'b': var.actual_message = st.cel_no_enciende
                                    case 'c': var.actual_message = st.cel_no_carga
                                    case _: incorrect()
                            case _: incorrect()
                    case 'b':
                        var.actual_message = st.info_general
                        match var.answer_user[2]:
                            case 'a': var.actual_message = st.info_general_a
                            case 'b': var.actual_message = st.info_general_b
                            case 'c': var.actual_message = st.info_general_c
                            case 'd': var.actual_message = st.info_general_d
                            case _: incorrect()
                    case 'd':
                        var.actual_message = st.contacto_asesor
                        match var.answer_user[2]:
                                    case 'a': var.actual_message = st.asesor_numero
                                    case 'b': var.actual_message = st.asesor_correo
                                    case 'c': var.actual_message = st.asesor_chat
                                    case _: incorrect()
                    case _: incorrect()

        except:
            print('error')

        var.messages.append({'from':'user', 'msg':format(request.form['message'])})
        var.messages.append({'from':'bot', 'msg':format(var.actual_message)})


        if not var.opcion_correcta:
            var.answer_user.pop()

    return redirect('/chat')
    