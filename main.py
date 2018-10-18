import encode
while True:
    if input("do you want to convert from morse or text ")=="text":
        text=input("enter text ")
        output=encode.encode(text)
        print(output)
    else:
        morse=input("enter morse ")
        output=encode.decode(morse)
        print(output)
