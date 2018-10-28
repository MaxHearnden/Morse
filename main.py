import encode,importlib
state="ask com mod"
com_module="main"
io=None
while True:
    if state=="ask com mod":
        com_module=input("enter com module name")
        if com_module:
            io=importlib.import_module(com_module)
            state="ask callsign"
            continue
        else:
            state="m encode"
            continue
    elif state=="ask callsign":
        own_sign=input("enter own callsign, leave blank for emergancy transmittion mode")
        if not own_sign:
            state="e encode"
        else:
            t_sign=input("enter target callsign")
            state="call"
    elif state=="m encode":#main.py encode
        if input("do you want to convert from morse or text ")=="text":
            text=input("enter text ")
            output=encode.encode(text)
            print(output)
        else:
            morse=input("enter morse ")
            output=encode.decode(morse)
            print(output)
    elif state=="e encode":
        io.output(encode.encode(input("please enter text")))
        try:
            print(io.listen())
        except KeyboardInterrupt:
            pass
    elif state=="call":
        call=own_sign+"de"+t_sign+"k"
        io.output(encode.encode(call))
        try:
            reply=encode.decode(io.listen())
            de_loc=reply.find("de")
            rep=reply[de_loc+2:-1]+"de"+reply[:de_loc]+reply[-1]
            while rep!=call:
                print("invalid reply "+reply)
                reply=encode.decode(io.listen())
                de_loc=reply.find("de")
                rep=reply[de_loc+2:-1]+"de"+reply[:de_loc]+reply[-1]
        except KeyboardInterrupt:
            state="send"
            continue
        print("valid callsign recieved")
        state="send"
        continue
    elif state=="send":
        message=input("enter message")
        io.output(encode.encode(message))
        if message[-2:]=="+k":
            state="recieve"
    elif state=="recieve":
        message=encode.decode(io.listen())
        print(message)
        if message[-2:]=="+k":
            state="send"
