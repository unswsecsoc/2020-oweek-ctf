from flask import Flask, render_template, request, redirect, url_for, make_response
import secret

app = Flask(__name__,
            static_folder = './templates',
            template_folder = './templates')

@app.route('/', methods=['GET'])
def index():
    resp = make_response(render_template('index.html', error=secret.error, user=secret.user, pswd=secret.pswd))
    resp.set_cookie('access-granted', 'nope', 0)
    secret.error = False
    return resp

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': return redirect(url_for('index'))
    elif request.method == 'POST':
        username = request.form['username']
        try:
            if request.form['password'].lower() != 'true':
                password = str(eval(request.form['password'])).lower()
            else:
                password = 'TRUE'
        except:
            password = request.form['password']
        auth = "username=" + username + " and password=" + password
        if auth == secret.secret:
            secret.error = False
            resp = make_response(redirect(url_for('getflag')))
            resp.set_cookie('access-granted', 'y4s5')
            return resp
        secret.error = True
        secret.user = username
        secret.pswd = password
        return redirect(url_for('index'))

@app.route('/flag', methods=['GET'])
def getflag():
    if request.cookies.get('access-granted') == 'y4s5':
        return "OWEEK{ev3Ry7h1nG_iZ_trUe_fl4G_15_p3rMitt3d}", 200, {'Content-Type': 'text/plain'}
    return redirect(url_for('index'))

@app.route('/robots.txt', methods=['GET'])
def robots():
    with open('robots.txt', 'r') as f:
        return f.read(), 200, {'Content-Type': 'text/plain'}

@app.route('/admin_stuff', methods=['GET'])
def admin():
    return """
    // Only admin knows the secret ...
    
    function checkAdmin(username, password) {
        if username is admin and password is true
            login -> true
        else
            login -> false
    }
    """, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
