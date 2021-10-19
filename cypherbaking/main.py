import base64
from cryptography.fernet import Fernet

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
        print("1) Encrypt message/file")
        print("2) Decrypt message/file")
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

def toFernet():
    # generacion de la clave
    key = Fernet.generate_key()

    # Se genera un archivo llamado filekey.key. La idea es que el archivo       
    # contenga una linea, que será un string, es decir, la clave.
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    # lectura de la clave
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # se guarda en variable la clave generada
    fernet = Fernet(key)

    # seleccionamos el archivo a encriptar
    print("Selecciona el archivo a encriptar: (Recuerda que si el archivo no está en esta carpeta, debes definir su 'path'): ")
    archivo = input()

    # lectura del archivo para encriptar
    with open(archivo, 'rb') as file:
        original = file.read()
    
    # función para encriptar el archivo
    encrypted = fernet.encrypt(original)

    # se abre el archivo en modo escritura y
    # se escribe el dato encriptado
    with open(archivo, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def fromFernet():
    # lectura de la clave
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    # seleccionamos el archivo a encriptar
    print("Selecciona el archivo a descriptar: (Recuerda que si el archivo no está en esta carpeta, debes definir su 'path'): ")
    archivo2 = input()

    # lecura del archivo encriptado
    with open(archivo2, 'rb') as enc_file:
	    encrypted = enc_file.read()

    # decriptacion del archivo encriptado
    decrypted = fernet.decrypt(encrypted)

    # abrir el archivo encriptado en modo escritura
    with open(archivo2, 'wb') as dec_file:
	    dec_file.write(decrypted)    


def encryptMessage():
    print("Which type of encryption you want to use: ")
    print("1. Base 64")
    print("2. Fernet (AES in CBC Mode:")
    option = input()

    if option == "1":
        toBase64()
    else: 
        toFernet()


def decryptMessage():
    print("Which type of decryption you want to use: ")
    print("1. Base 64")
    print("2. Fernet (AES in CBC Mode:")

    option = input()

    if option == "1":
        fromBase64()
    else:
        fromFernet()    

menu()
