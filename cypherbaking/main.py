import base64


def menu():
    print("*********************************************************************")
    print("""
                       _               _           _    _             
                      | |             | |         | |  (_)            
       ___ _   _ _ __ | |__   ___ _ __| |__   __ _| | ___ _ __   __ _ 
      / __| | | | '_ \| '_ \ / _ \ '__| '_ \ / _` | |/ / | '_ \ / _` |
     | (__| |_| | |_) | | | |  __/ |  | |_) | (_| |   <| | | | | (_| |
      \___|\__, | .__/|_| |_|\___|_|  |_.__/ \__,_|_|\_\_|_| |_|\__, |
            __/ | |                                              __/ |
           |___/|_|                                             |___/ 

    """)
    print("  CypherBaking v1.0")
    print("  La Panaderia")
    print("  https://github.com/carloscast1llo/CypherBaking")
    print("*********************************************************************")
    print("Welcome to Cyberbaking")
    menu = True

    while menu:
        print("1) Encrypt message")
        print("2) Decrypt message")
        print("3) Exit")

        opcion = input()

        if opcion == "1":
            encryptMessage()
            menu = False

        elif opcion == "2":
            decryptMessage()
            menu = False

        elif opcion == "3":
            menu = False

        else:
            print("Invalid input")


def toBase64():
    text = input("Write the text you want to encrypt: ")
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')
    print(base64_text)
    cont = input("Press ENTER to continue")
    menu()


def fromBase64():
    base64_text = input("Write the text you want to decrypt: ")
    base64_bytes = base64_text.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    decrypted_text = text_bytes.decode('ascii')
    print(decrypted_text)
    cont = input("Press ENTER to continue")
    menu()


def encryptMessage():
    print("Which type of encryption you want to use: ")
    print("1. Base 64")
    option = input()

    if option == "1":
        toBase64()


def decryptMessage():
    print("Which type of encryption you want to use: ")
    print("1. Base 64")
    option = input()

    if option == "1":
        fromBase64()


menu()
