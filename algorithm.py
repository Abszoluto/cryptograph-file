"""
    * Author: Abszoluto
    * Code made with Python 3.7.0
    * What does that do ?
        This is a code that will open a file and cryptograph its content
        The cryptograph method is Vigenere Cypher
        
    * Version 4.0
        Main menu not working
        Terminal commands improved with -i input and -o output
    * Version 3.0
        Terminal commands added
    * Version 2.0
        Added more safe inverting the array wich contains the characters cryptographed (after using Vigenere Cypher)
        
    * Instructions:
      * Command line run
	    * ENCRYPTION:

		* -e for encryption, followed by -i inputfile -o ouputfile
		* EXAMPLE:
		    - py cryptography.py -e -i content.txt -o cryptographed__content.txt

	    * DECRYPTION:

		* -d for decryption, followed by -i inputfile and -o outputfile(optional)
		* NOTE: If decryption doesnt have an outputfile it will print at consoles window
		* EXAMPLE:
		(with output) - python cryptography.py -d -i cryptographed__content.txt -o decoded_content.txt
		(without output) - python cryptography.py -d -i cryptographed__content.txt
      
      Main Menu (not working): 
         Code:  cryptograph a file (filename)
         Decode: decrypt a file with the name of the inputfile
         Anything else: Stop running the code
"""

import io
import sys

key = "0DB20660AFDE446C5722CCF2F5256999" # I am using a hash to use as the key for Vigenere Cypher

#    Application Methods:

def code(filename):
    """
        * This method will open a file, cryptograph its content and save it in a file
    """
    
    characterAtKey = 0
    content = []
    file = open(filename,"r", encoding="utf-8")
    with open(outputfile, "w", encoding="utf-8") as file2:
        while True:
                result = file.read(1)   # If there isnt something to read, result will be 0
                if (not result):
                    content = content[::-1] # Inverting the array with the cryptographed content
                    for character in content:
                        file2.write(chr(character)) # Write every single character at the file "filename"
                    print(f"File coded sucessfully as {outputfile}.. \n")
                    file.close()
                    break;
                content.append(ord(result)+ord(key[characterAtKey]))
                # adding the cryptographed character(value of (character) + value of (key[position]) ) at the array content
                characterAtKey = (characterAtKey + 1)%len(key)
                # next character at the key, the mod will go back at the first character when there isnt more characters to use
        

def decode(output=None):
    """
        * This method will open a file cryptographed, decipher its content
          and print it at the console or in a file (if output specified)
    """
    
    decode = ""
    characterAtKey = 0
    with open(inputfile, "r", encoding="utf-8") as file:
        print("\DECRYPTING... \n")
        result = file.read() # reading the whole file
        result = result[::-1] # reversing the file content
        for charactere in result:
            decode = decode + (chr((ord(charactere)-ord(key[characterAtKey]))))  # Concatenating the string decode with the character decypher
            characterAtKey = (characterAtKey + 1)%len(key)
    if output is None:
        print("FILE SUCESSFULLY DECRYPTED: \n")
        print(decode)
    else:
        print(f"FILE SUCESSFULLY DECRYPTED AT {output}: \n")
        with open(output, "w", encoding="utf-8") as outputfile:
            outputfile.write(decode)
            
def mainMenu():
    while True:
        """
            * Main Menu (not working atm)
            * Type Code for code a file with the name content.txt
            * Type decode to decode a file with the name of "cryptcontent.txt"
            * Type anything else to leave
        """
        option = input("Do you wanna 'encrypt', 'decrypt' or 'leave' ? ")
        if option.lower() == "encrypt":
            inputfile = input("What is the name of the file that you want to encrypt ? ")
            outputfile = input("What name do you want for the output file (encrypted content) ? ")
            code(inputfile,outputfile)
        elif option.lower() == "decrypt":
            inputfile = input("What is the name of the file that you want to decrypt ? ")
            decode(inputfile)
        else:
            break
        input("Press any button to continue...")



#    Application Start

if len(sys.argv) > 2:
    """
    * Command line run
    
    * ENCRYPTION:
        
        * -e for encryption, followed by -i inputfile -o ouputfile
        * EXAMPLE:
            - py cryptography.py -e -i content.txt -o cryptographed__content.txt

    * DECRYPTION:
        
        * -d for decryption, followed by -i inputfile and -o outputfile(optional)
        * NOTE: If decryption doesnt have an outputfile it will print at consoles window
        * EXAMPLE:
        (with output) - python cryptography.py -d -i cryptographed__content.txt -o decoded_content.txt
        (without output) - python cryptography.py -d -i cryptographed__content.txt
    """
    try:
        inputfile = sys.argv[sys.argv.index('-i') + 1]
        if ('-o' in sys.argv):
            outputExistance = sys.argv.index('-o')
            outputfile = sys.argv[outputExistance + 1]
        else:
            outputfile = "__encrypted__"+inputfile
        if (sys.argv[1] == '-e'):
            code(inputfile)
        elif (sys.argv[1] == '-d'):
            if ('-o' in sys.argv):
                decode(outputfile)
            else:
                decode()
    except:
        print("An error has ocurred...\n")
        print("Check the input and output arguments: ")
        print("* EXAMPLE ENCRYPT:")
        print("python code.py -e -i inputfile -o outputfile")
        print("* EXAMPLE DECRYPT:")
        print("python code.py -d -i inputfile -o outputfile")
