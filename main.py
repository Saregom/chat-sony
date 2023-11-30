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

messages = [
    {'from':'bot',
     'msg':'hello im bot'}, 
    {'from':'bot',
     'msg':'claro, te pueo ayudar'},
    {'from':'bot',
     'msg':'hello im bot'},
    # {'from':'user',
    #  'msg':'ayuda en mi tv'},
    # {'from':'bot',
    #  'msg':'hello im bot'}, 
    # {'from':'user',
    #  'msg':'hello i have a problem'},
    # {'from':'bot',
    #  'msg':'claro, te pueo ayudar'},
    # {'from':'user',
    #  'msg':'ayuda en mi tv'},
    #  {'from':'bot',
    #  'msg':'hello im bot'}, 
    # {'from':'user',
    #  'msg':'hello i have a problem'},
    # {'from':'bot',
    #  'msg':'claro, te pueo ayudar'},
    # {'from':'user',
    #  'msg':'ayuda en mi tv'},
    #  {'from':'user',
    #  'msg':'ayuda en mi tv'},
    #  {'from':'bot',
    #  'msg':'hello im bot'}, 
    # {'from':'user',
    #  'msg':'hello i have a problem'},
    # {'from':'bot',
    #  'msg':'claro, te pueo ayudar'},
    # {'from':'user',
    #  'msg':'ayuda en mi tv'}
    ]

for message in messages:
    print(message['from'] == 'bot')

@app.route('/chat')
def chat():

    return render_template('chat.html', messages = messages)

@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    if request.method == 'POST':
        
        messages.append(
            {'from':'user', 
            'msg':request.form['message']})
        
        
    return redirect('/chat')
    