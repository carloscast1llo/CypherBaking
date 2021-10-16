def menu():
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


def encryptMessage():
    print("Encrypt")


def decryptMessage():
    print("Decrypt")


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

menu()
