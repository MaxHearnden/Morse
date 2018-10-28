#coding: utf-8
#allowed code to be run outside of idle
code={"a":".-",
      "b":"-...",
      "c":"-.-.",
      "d":"-..",
      "e":".",
      "é":".._..",
      "f":"..-.",
      "g":"--.",
      "h":"....",
      "i":"..",
      "j":".---",
      "k":"-.-",
      "l":".-..",
      "m":"--",
      "n":"-.",
      "o":"---",
      "p":".--.",
      "q":"--.-",
      "r":".-.",
      "s":"...",
      "t":"-",
      "u":"..-",
      "v":"...-",
      "w":".--",
      "x":"-..-",
      "y":"-.--",
      "z":"--..",
      " ":" ",#space uses the 3 spaces either side of the 1 space, timing is Rec. ITU-R M.1677-1 2 compliant
      "1":".----",
      "2":"..---",
      "3":"...--",
      "4":"....-",
      "5":".....",
      "6":"-....",
      "7":"--...",
      "8":"---..",
      "9":"----.",
      "0":"-----",
      ".":".-.-.-",
      ",":"--..--",
      ":":"---...",
      "?":"..--..",
      "'":".----.",
      "-":"-....-",
      "/":"-..-.",
      "(":"-.--.",
      ")":"-.--.-",
      '"':".-..-.",
      "=":"-...-",
      "+":".-.-.",
      "@":".--.-."}#Rec. ITU-R M.1677-1 1.1.2 and 1.1.3 compliant morse code characters
dcode=dict(zip(code.values(),code.keys()))#create another dictionary, but this time the values are the keys and the keys are the values
def encode(string):
    output=""#initalise output
    for i in string.lower():#for every character(converted to lower case)
        try:
            output+=code[i]+"   "#find character in lookup table and add gap between character
        except KeyError:#if the character isn't in table
            print(i)#print it for debugging purposes
    return output.strip(" ")#return the encoded text and strip any trailing spaces
def decode(string):
    output=""
    spaces=0
    character=""
    for i in string:
        if i ==" ":
            spaces+=1
            if spaces==3:
                try:
                    output+=dcode[character]
                except KeyError:
                    print(character)
                character=""
        else:
            if spaces==7:#space
                output+=" "
            spaces=0
            character+=i
    if spaces<3:
        output+=dcode[character]
    elif spaces==7:
        output+=" "
    return output
if __name__ == "__main__":
    while True:
        if input("from morse or text")=="text":
            string=input("please enter text")
            print(encode(string))
        else:
            string=input("please enter morse")
            print(decode(string))
