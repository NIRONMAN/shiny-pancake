alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    newtext=""
    for i in range(0,len(text)):
        if (alphabet.index(text[i])+shift)>25:
            newtext+=alphabet[alphabet.index(text[i])+shift-26]
        else:    
            newtext+=alphabet[alphabet.index(text[i])+shift]
    print(newtext)  
encrypt(text,shift)
