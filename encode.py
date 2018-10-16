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
      " ":" "}
while True:
    string=input("please enter text")
    output=""#initalise output
    for i in string:#for every character
        try:
            output+=code[i]+"   "#find character in lookup table and add gap between character
        except IndexError:#if the character isn't in table
            print(i)#print it for debugging purposes
    print(output.strip(" "))#print the encoded text and strip any trailing spaces
