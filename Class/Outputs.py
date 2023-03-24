from datetime import datetime
from os import system, name

# Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[31m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'

class Outputs():

    def logo():
        Outputs.clear()
        print(f"""{WHITE}{BOLD}

██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██████╔╝███████║██║░░██║██╔██╗██║█████╗░░███████║███████║██║░░╚═╝█████═╝░
██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░██╔══██║██╔══██║██║░░██╗██╔═██╗░
██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
                
                        {BLUE}Twitter{WHITE}:{YELLOW} @YasserREED {WHITE}
        
        {WHITE}""")

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')