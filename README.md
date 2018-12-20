# cryptograph-file
(Python 3.7.0) Vigenere Cipher to cryptograph files throught command line<br/>
    * What does that do ?<br/>
        This is a code that will open a file and encrypt its content also you can open a encrypted file and decrypt it<br/>
        The cryptograph method is Vigenere Cypher among other things<br/>
    
    * Instructions :
        * Command line run
    
        * ENCRYPTION:

            * -e for encryption, followed by -i inputfile -o ouputfile
            * EXAMPLE:
                - py algorithm.py -e -i content.txt -o cryptographed__content.txt

        * DECRYPTION:

            * -d for decryption, followed by -i inputfile and -o outputfile(optional)
            * NOTE: If decryption doesnt have an outputfile it will print at consoles window
            * EXAMPLE:
            (with output) - python algorithm.py -d -i cryptographed__content.txt -o decoded_content.txt
            (without output) - python algorithm.py -d -i cryptographed__content.txt
