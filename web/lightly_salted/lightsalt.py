#!/usr/bin/python3
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
string = form.getvalue("input", None)
flag = "OWEEK{SP1cY_3El_3gGs}"


# top secret patented 'hexhash' algorithm
# we use single letter variable names to make it faster
HXDIGIT = "0123456789abcdef"
def hexhash(msg):
    h = ''
    p = msg[0]
    for c in msg[1:]:
        d = ord(c) - ord(p)
        h += HXDIGIT[d % 16]
        p = c
    return h

def chk_pass(password):
    password += "salty"
    HASH = "3a59d6f51730eb85"
    return hexhash(password) == HASH

print("Content-type: text/html\n")
if string is None:
    print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Lightly Salted</title>
</head>
<body>
    <h1>Sean and Siobhan's Salty Seafood Spectacular</h1>
    <h3>Where we put the <i>Sea</i>n in <i>Sea</i>nfood!</h3>
    <p>This page is currently under construction. A password is needed to access:</p>
    <form method="post" id="form">
        <input type="text" name="input" value="" autofocus/>
        <button type="submit" form="form">Login</button>
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
    <title>Lightly Salted</title>
</head>
<body>
    <h1>Sean and Siobhan's Salty Seafood Spectacular</h1>
    <h3>Where we put the <i>Sea</i>n in <i>Sea</i>nfood!</h3>""")
    if correct:
        print(f"""
    <p>Welcome, Sean. Here is your weekly agenda:</p>
    <ul>
        <li>Hire new kitchenhand</li>
        <li>Consider adding {flag} to the menu</li>
        <li>Remove rotting squid from freezer</li>
        <li>Deal with rat problem before those health inspector bastards get here</li>
        <li>Paint over black mold in a lighter color so it's less dangerous</li>
    </ul>""")
    else:
        hsh = hexhash(string + "salty")
        print(f"""
    <p>InvalidPasswordException: "{hsh}" does not match expected hash "3a59d6f51730eb85".</p>
    <form method="post" id="form">
        <input type="text" name="input" value="{string}" autofocus/>
        <button type="submit" form="form">Go</button>
    </form>""")
    print(f"""
</body>
</html>
    """)
