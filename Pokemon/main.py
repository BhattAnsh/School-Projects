import handlingUserData
import time


login = True
user = ""
def print_animation(text, delay=0.003):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def display_starting_message():
    print_animation(r"""                    
                    
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
                    """)
    print_animation("----------------------------------------------------------")
    print_animation("Welcome to the Text-based Pokemon Adventure!")
    print_animation("-------------------------------------------------")
    print_animation("Your journey in the world of Pokemon begins now.")
    print_animation("Get ready to catch 'em all and become a Pokemon Master!")
    print_animation("-------------------------------------------------")
    registration()

def registration():
    l_or_s = input("Are you new in this game? y/n: ")
    if l_or_s == 'y':
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        userHandler = handlingUserData.UserDataHandler(name, password)
        userHandler.signUp()
        login = True
        user = name
        game()

    else:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        userHandler = handlingUserData.UserDataHandler(name, password)
        userHandler.login()
        game()

def game():
    print(f"Welcome {user} in the pokemon world")
    print('------------------------------------------------')
    
def main():
    display_starting_message()



if __name__ == "__main__":
    main()
