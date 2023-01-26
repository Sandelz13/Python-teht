print("Anna käyttäjäniimi ja salasana")
count = 0

username = ""
password = ""


while password!='rules' and username!='python' and count < 3:

    username = input("Anna käyttäjänimi: ")
    password = input("Anna salasana: ")

    if password=='rules' and username=='python':
     # if match, grand and break
     print("Tervetuloa")
     break

    else:
        print("Väärä käyttäjätunnus tai salasana")
        count+=1
    if count ==3:
        print("Pääsy evätty")
