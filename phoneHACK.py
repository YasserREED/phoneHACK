from Class.Outputs import *
from Class.Main import *
import os

# Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
print('\033[1m')

Outputs.logo()

phonenumber = str(input(f"{RED}[REQ] {WHITE} Please Enter Phone Number Ex => [ {YELLOW}+966{RED}XXXXXXXXX{WHITE} ] : "))

# Check if not euql 13
if len(phonenumber) != 13:
    print(f"\n{RED}[{YELLOW}ERR{RED}]{WHITE} Please make sure its {YELLOW}10{WHITE} Digits {RED}Ex: {YELLOW}+9665123456789{WHITE} \n")
    quit()

# Check if not start with +966
elif phonenumber.startswith('+966') == False:
    print(f"\n{RED}[{YELLOW}ERR{RED}]{WHITE} Please make sure start with {YELLOW}+966{WHITE} \n")
    quit()

# run The code normally
else:
    # Make new file
    try:
        os.makedirs(f"Outputs/{phonenumber}-Results")
    # Countinue same file name
    except:
        sleep(1)
        print(f"\n{RED}[{YELLOW}INFO{RED}]{WHITE} The Directory already exists!")
        sleep(2)
        print(f"\n{RED}[{YELLOW}INFO{RED}]{WHITE} Scan will run with the same folder{RED}[ Outputs/{YELLOW}{phonenumber}-Results {RED}]{WHITE}")
        sleep(2)
    Main.basicscan(phonenumber)
    Main.deepscan(phonenumber)

print(f"{RED}[{YELLOW}FINISHED{RED}]{WHITE} Scan Finished chcek this folder {RED}[ Outputs/{YELLOW}{phonenumber}-Results {RED}]{WHITE}\n")