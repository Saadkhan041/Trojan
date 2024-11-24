import os
from files.colors import r , g , w , c , y

logo = f"""
 ▄█     █▄   ▄█  ███▄▄▄▄   ████████▄   ▄██████▄   ▄█     █▄     ▄████████ 
███     ███ ███  ███▀▀▀██▄ ███   ▀███ ███    ███ ███     ███   ███    ███ 
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███   ███    █▀  
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███   ███        
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███ ▀███████████ 
███     ███ ███  ███   ███ ███    ███ ███    ███ ███     ███          ███ 
███ ▄█▄ ███ ███  ███   ███ ███   ▄███ ███    ███ ███ ▄█▄ ███    ▄█    ███ 
 ▀███▀███▀  █▀    ▀█   █▀  ████████▀   ▀██████▀   ▀███▀███▀   ▄████████▀  
                                                                          
    ███        ▄████████  ▄██████▄       ▄█    ▄████████ ███▄▄▄▄          
▀█████████▄   ███    ███ ███    ███     ███   ███    ███ ███▀▀▀██▄        
   ▀███▀▀██   ███    ███ ███    ███     ███   ███    ███ ███   ███        
    ███   ▀  ▄███▄▄▄▄██▀ ███    ███     ███   ███    ███ ███   ███        
    ███     ▀▀███▀▀▀▀▀   ███    ███     ███ ▀███████████ ███   ███        
    ███     ▀███████████ ███    ███     ███   ███    ███ ███   ███        
    ███       ███    ███ ███    ███     ███   ███    ███ ███   ███        
   ▄████▀     ███    ███  ▀██████▀  █▄ ▄███   ███    █▀   ▀█   █▀         
              ███    ███            ▀▀▀▀▀▀                                                                 
"""

lololo = f"""
    ███        ▄████████  ▄██████▄       ▄█    ▄████████ ███▄▄▄▄                      
▀█████████▄   ███    ███ ███    ███     ███   ███    ███ ███▀▀▀██▄                    
   ▀███▀▀██   ███    ███ ███    ███     ███   ███    ███ ███   ███                    
    ███   ▀  ▄███▄▄▄▄██▀ ███    ███     ███   ███    ███ ███   ███                    
    ███     ▀▀███▀▀▀▀▀   ███    ███     ███ ▀███████████ ███   ███                    
    ███     ▀███████████ ███    ███     ███   ███    ███ ███   ███                    
    ███       ███    ███ ███    ███     ███   ███    ███ ███   ███                    
   ▄████▀     ███    ███  ▀██████▀  █▄ ▄███   ███    █▀   ▀█   █▀                     
              ███    ███            ▀▀▀▀▀▀                                            
            {y}<{w}/{y}> {c}Author: {w}Saad Khan {g}| {w}Cyber-Dioxide   
            {y}<{w}/{y}> {c}Website: {w}www.cyox2.com  
"""
from files.colors import *


def banner():
    print(ran + lololo)
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Instagram @cyber_dioxide ", "- " * 4 + ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX,  "- " * 4, " [+] Coding Instagram @coding_memz ", "- " * 4+ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+ran + "|")


def banner2():

    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Instagram @cyber_dioxide ", "- " * 4 + ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX,  "- " * 4, " [+] Coding Instagram @coding_memz ", "- " * 4+ran + "|")
    print(ran +"\n", "|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+ran + "|")


def clear():
    os.system("clear")
