from flask import Flask, render_template, request, redirect, url_for, make_response

secret  = "username=admin and password=true"

app = Flask(__name__,
            static_folder = './templates',
            template_folder = './templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': return redirect(url_for('index'))
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        auth = "username=" + username + " and password=" + password.lower()
        if auth == secret:
            return "OWEEK{r0bOtz_FTW}", 200, {'Content-Type': 'text/plain'}
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

