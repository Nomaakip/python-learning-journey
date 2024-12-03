import requests

def codea():
    command = input()
    if (command == "help"):
        print("1. help")
        print("shows all commands")
        print("2. freakybob")
        print("prints freakybob(credit : freakybob-team)")
        codea()
    else:
        print(command, "is invalid.Please enter a valid command to continue.")
        codea()
def code():
    print("Welcome to swagcmd. enter a command to continue")
    command = input()
    if (command == "help"):
        print("1. help")
        print("shows all commands")
        codea()
    if (command == "swag"):
        print("freakybob")
        url = 'https://github.com/Freakybob-Team/lb/blob/main/freakybob.txt?raw=true'
        response = requests.get(url)
        file_Path = 'freakybob.txt'
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
        fb = open("freakybob.txt", "r")
        print(fb.read())
        fb.close()
    print('Failed to download file')
    if (command == "greg"):
        print("greg")
    else:
       print(command, "is invalid.Please enter a valid command to continue.")
       codea()
code()       
