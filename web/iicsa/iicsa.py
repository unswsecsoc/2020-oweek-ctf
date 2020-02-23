#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
string = form.getvalue("input", None)
flag = "OWEEK{h3y_1m_PRe77y_keWl}"



# top secret decoding formula
def decode(encrypted):
    out = ''
    for x in encrypted:
        out += chr(128 - x)
    return out

# function to check password
def chk_pass(password):
    # password is encoded so you hackers can't see it
    ENCODED_PASS = [16, 20, 77, 31, 78, 59, 33, 76, 50, 28, 33, 73, 24, 76, 50, 21, 39, 80, 11]
    return password == decode(ENCODED_PASS)



print("Content-type: text/html\n")
if string is None:
    print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>IICSA</title>
</head>
<body>
    <h1>Welcome to my secret stash!</h1>
    <p>I have a secret hidden here. But do you know the password?</p>
    <form method="post" id="form">
        <input type="text" name="input" value="" autofocus/>
        <button type="submit" form="form">Go</button>
    </form>
</body>
</html>
    """)
else:
    correct = chk_pass(string)
    print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>My Secret Stash!</title>
</head>
<body>
    <h1>Welcome to my secret stash!</h1>""")
    if correct:
        print(f"""
    <p>Hello, me! Here's your secret:</p>
    <pre>{flag}</pre>""")
    else:
        print(f"""
    <p>Sorry, that's not right. Try again?</p>
    <form method="post" id="form">
        <input type="text" name="input" value="{string}" autofocus/>
        <button type="submit" form="form">Go</button>
    </form>""")
    print(f"""
</body>
</html>
    """)
