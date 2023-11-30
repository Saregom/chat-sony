from flask import Flask, render_template, url_for, redirect, request, session, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/') 
def index():
    return redirect('/login')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    # response = [False, '']
    if request.method == 'POST':
        return redirect('/chat')
    #     response = person_cont.verifyClient(request.form['email'], request.form['password'])
    #     if response[0]:
    #         session['user_id'] = response[2]
    #         session['user_type'] = response[3]
    #         return redirect('/home')

    return render_template('login.html', alert = '')

messages = [{'from':'bot', 'msg':['Hola soy Sonybot, ¿En que te puedo ayudar?']}]

@app.route('/chat')
def chat():

    return render_template('chat.html', messages = messages)


# --------------- 0
menu_inicial = '''Por favor seleccione una opcion:
                a) Un producto presenta fallas.
                b) Información general sobre un producto.
                c) Preguntas frecuentes. 
                d) Contactame con un asesor.'''

# --------------- 1
producto_fallas = '''Lamentamos mucho tu situación porfavor proporciona los siguientes datos en un solo mensaje y en breve un asistente se pondrá en contacto:
Su correo personal.
Producto con el cual estas presentando fallas.
Problemas que presenta el equipo.'''
info_general = '''Por favor seleccione una opcion:
                a) SonicVision 4K
                b) SonicAudio Surround Sound System
                c) ChillZone Sonic Fridge
                d) SonicCharge Wireless Charging Station'''
contacto_asesor = '''Te invitamos al a ingresar al siguiente enlace donde
                podras contar con la atención de uno de nuestros asistentes:
                https://www.sony.com.co/corporate/CO/servicioysoporte/servicio.html'''

# ---------------- 2
info_general_a = '''SonicVision 4k Smart TV:
                    Experimenta la velocidad en alta definición. Este televisor inteligente de última generación ofrece una calidad de imagen sorprendente y funciones inteligentes para acceder a tus contenidos favoritos'''
info_general_b = '''SonicAudio Surround Sound System:
                    Sumérgete en el sonido supersónico con este sistema de sonido envolvente. Desde explosiones hasta música, cada detalle cobra vida para una experiencia auditiva inigualable.'''
info_general_c = '''ChillZone Sonic Fridge:
                    Mantén tus bebidas y snacks frescos con estilo. Esta nevera con diseño Sonic no solo es funcional, sino que también agrega un toque de diversión a tu espacio.'''
info_general_d = '''SonicCharge Wireless Charging Station:
                    Olvídate de los cables con esta estación de carga inalámbrica. Compatible con una variedad de dispositivos, mantiene tus gadgets cargados mientras muestras tu amor por Sonic.'''

rta_info_falla = '''Gracias por la información proporcionada en breve un asesor te contactara, recomendamos estar atento a su correo.'''

def format(txt):
    return txt.split('\n')

class var():
    pos_pregunta = 1
    opcion_correcta = True
    fin_opciones = False
    answer_user = []
    actual_message = ''
    bloqueo = 1

def incorrect():
    var.actual_message = 'Opcion incorrecta'
    var.opcion_correcta = False

@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    var.opcion_correcta = True
    var.actual_message = ''

    if request.method == 'POST' and request.form['message'] != '':
        var.answer_user.append(request.form['message'])
        print(var.answer_user)

        try:
            if var.answer_user[0] != '':
                var.actual_message = menu_inicial

                match var.answer_user[1]:
                    case 'a': 
                        if var.bloqueo == 1:
                            var.actual_message = producto_fallas
                            var.bloqueo = 2
                        else:
                            if var.answer_user[2] != ' ':
                                print(444)
                                var.actual_message = contacto_asesor
                    case 'b':
                        var.actual_message = info_general
                        match var.answer_user[2]:
                            case 'a': var.actual_message = info_general_a
                            case 'b': var.actual_message = info_general_b
                            case 'c': var.actual_message = info_general_c
                            case 'd': var.actual_message = info_general_d
                            case _: incorrect()
                    case 'd':
                        var.actual_message = contacto_asesor
                    case _: incorrect()

        except:
            print('error')

        messages.append({'from':'user', 'msg':format(request.form['message'])})
        messages.append({'from':'bot', 'msg':format(var.actual_message)})


        if var.opcion_correcta:
            var.pos_pregunta = var.pos_pregunta + 1
        else:
            var.answer_user.pop()

    return redirect('/chat')
    