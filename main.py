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
            if t_sign:
                state="call"
            else:
                state="clisten"
    elif state=="clisten":#listen for callsign
        reply=encode.decode(io.listen())
        state="reply"
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
            print(encode.decode(io.listen()))
        except KeyboardInterrupt:
            pass
    elif state=="call":
        call=t_sign+"de"+own_sign+"k"
        io.output(encode.encode(call))
        try:
            reply=encode.decode(io.listen())
            de_loc=reply.find("de")
            rep=reply[de_loc+2:-1]+"de"+reply[:de_loc]+reply[-1]
            while rep!=call:
                if reply[:de_loc]==own_sign:
                    if input("call from "+reply[de_loc+2:-1]+" accept? ")=="yes":
                        state="listen"
                        continue
                else:
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
    elif state=="reply":
        de_loc=reply.find("de")
        rep=reply[de_loc+2:-1]+"de"+reply[:de_loc]+reply[-1]
        io.output(encode.encode(rep))
        state="recieve"
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
