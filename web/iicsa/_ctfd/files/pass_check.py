
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

