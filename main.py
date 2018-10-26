import encode
state="ask callsign"
com_module="main"
while True:
    if state=="ask callsign":
        own_sign=input("enter own callsign, leave blank for emergancy transmittion mode")
        if not own_sign:
            if com_module!="main":
                state="e_encode"
            else:
                state="encode"
            continue
        else:
            t_callsign=input("enter target callsign")
    elif state=="encode":
        if input("do you want to convert from morse or text ")=="text":
            text=input("enter text ")
            output=encode.encode(text)
            print(output)
        else:
            morse=input("enter morse ")
            output=encode.decode(morse)
            print(output)
