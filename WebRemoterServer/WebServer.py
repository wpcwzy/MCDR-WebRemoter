from flask import Flask,render_template,request
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
auth=HTTPBasicAuth()

command=""

httpPort=8080
#Example:
# users = [
#     {'username': 'TANGhz17', 'password': 'TANGhz17'},
#     {'username}: 'wpcwzy', 'password': 'wpc123wzy'}
# ]

users = [
    {'username': '', 'password': ''}
]

outputs=[]

@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None

@app.route('/')
@auth.login_required
def index():
    return render_template("index.html",contents=outputs)

@app.route('/execute',methods=['POST'])
@auth.login_required
def execute():
    global command
    command=request.form.get("command")
    return render_template("success.html",contents=outputs)

@app.route('/upload',methods=['POST'])
def upload():
    global outputs
    if 'MCDR-WebRemoter' in request.headers:
        output=request.form.get("output")
        outputs.insert(0,output)
        if(len(outputs)>100):
            outputs.pop()
        return "Success"
    else:
        return render_template("no_access.html")

@app.route('/get_command')
def get():
    global command
    if 'MCDR-WebRemoter' in request.headers:
        data=command
        command=""
        return data
    else:
        return render_template("no_access.html")

def start_server():
    app.run("0.0.0.0",httpPort,debug=False)
