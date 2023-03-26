from Class.Outputs import *
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from phonenumbers import carrier, timezone
from selenium import webdriver
from time import sleep
import platform
import phonenumbers
import random
import arabic_reshaper
import bidi.algorithm

# Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[31m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'
print(BOLD)


class Main():

    def deepscan(self):

        # Identify OS verion
        version = platform.version()

        # Create log file for Deep scan
        log = open(f"Outputs/{self}-Results/DeepSCAN.txt",
                   "w", encoding="utf-8")

        # Print the Logo
        Outputs.logo()

        # open userAgent file and take random agent
        with open('Files/userAgent.txt', 'r') as file:
            user_agents = file.read().splitlines()
        randomAgent = random.choice(user_agents)

        # Adding argumnets to the broswer
        options = Options()
        options.add_argument(f'user-agent={randomAgent}')
        options.add_argument('--headless')

        # Check if it Ubuntu system
        if platform.system() == 'Linux' and 'ubuntu' in version.lower():
            # Using Firefox driver
            driver = webdriver.Firefox(options=options)
            # Get the domain
            driver.get("https://storage.googleapis.com/ksa-n/index.html")

        # Any other system
        else:
            # Using Firefox driver
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

            # Get the domain
            driver.get("https://storage.googleapis.com/ksa-n/index.html")
        # Print the Logo
        Outputs.logo()

        # Print sacnning type
        print(f"\n{RED}[{YELLOW}PROGRESS{RED}] {WHITE}Starting Deep scan \U0001F525")
        log.write("[PROGRESS] Starting Deep scan\n\n")

        # Find output
        find = driver.find_element
        find(By.ID, 'snumber').send_keys(self)
        find(By.ID, 'sbutton').click()

        # Value Condtion to stop the loop
        FLAG = True

        # Sleep Value
        x = 1
        sleep(5)

        # Loop to the body, Adding sleep(x+1) each attempt
        while FLAG == True:
            try:
                output = find(By.ID, 'tf_body').text
                name = output.split("\n")
                if len(name) != 0:
                    FLAG = False
            except:
                x += 1
                sleep(x)
        sleep(1)
        print(f"\n{RED}[{GREEN}INFO{RED}] {WHITE}Possible names for this number {RED}[ {YELLOW}{self}{WHITE} {RED}]{WHITE}")
        log.write(f"[INFO] Possible names for this number [ {self} ]\n")
        sleep(1)

        print(f"\n{RED}[{GREEN}INFO{RED}] {WHITE}Hacking Phone Number \U0001F480 \n")
        log.write("[INFO] Hacking Phone Number\n\n")

        sleep(1)
        if name != ['']:
            # Print The names
            for x, Fullname in enumerate(name):

                # Change the format to arabic
                reshaped_text = arabic_reshaper.reshape(Fullname)
                bidi_text = bidi.algorithm.get_display(reshaped_text)

                # Check block status
                if bidi_text == "تم حجب النتائج عنك مؤقتا":
                    print(f"{RED}[{YELLOW}BLOCKED{RED}]{WHITE} Your have been {YELLOW}Blocked{WHITE}, {GREEN}Please try after {YELLOW}10 Min{WHITE}\n\n")
                    exit()
                # Continue the loop and print the available names
                else:
                    print(f"\n{RED}[{YELLOW}INFO{RED}]{WHITE} Victim {RED}{x+1}{WHITE}: {bidi_text}")
                    sleep(1)
                    log.write(f"[INFO] Victim {x+1}: {Fullname}\n")

            sleep(1)
            print(f"\n\n{RED}[{YELLOW}FINISHED{RED}] {WHITE}Deep scan Done \n")
            log.write(f"[FINISHED] Deep scan Done.\n")

        else:
            sleep(1)
            print(f"{RED}[{YELLOW}ERR{RED}]{WHITE} There are no names found! \n")
            log.write(f"[ERR] There are no names found!\n")
        driver.close()

    def basicscan(self):

        # Create file for Basic sacn
        log = open(f"Outputs/{self}-Results/BasicSCAN.txt", "w")

        # Phone Number Function
        phoneInfo = phonenumbers.parse(self)
        Region = timezone.time_zones_for_number(phoneInfo)[0]
        Region = Region.split("/")

        # Phone number Filtering
        ISP = carrier.name_for_number(phoneInfo, "en")
        PHONENUMBER = str(phoneInfo.national_number)
        CITY = Region[1]

        # Start Basic Scan
        print(f"\n{RED}[{YELLOW}PROGRESS{RED}] {WHITE}Starting basic scan \U0001F9BD")
        log.write(f"[PROGRESS] Starting Basic scan\n\n")
        sleep(3)

        # Info for starting
        print(f"\n{RED}[{GREEN}INFO{RED}] {WHITE}Victim number you search for {RED}[ {YELLOW}{self}{RED} ]{WHITE}")
        log.write(f"[INFO] Victim number you search for [ {self} ]\n")
        sleep(3)

        print(f"\n{RED}[{GREEN}INFO{RED}] {WHITE}Gathring info for this number \U0001F50E")
        log.write("[INFO] Gathring info for this number\n\n")
        sleep(3)

        # Declare Basic sac output
        if PHONENUMBER != "":
            print(f"\n{RED}[{YELLOW}RESULT{RED}]{WHITE} National Number = {WHITE}0{PHONENUMBER}")
            log.write(f"[RESULT] National Number = 0{PHONENUMBER}\n")
        else:
            print(f"\n{YELLOW}[{RED}EMPTY{YELLOW}]{WHITE} National Number = {YELLOW}NA{WHITE}")
            log.write("[RESULT] National Number = NA\n")
        sleep(2)
        if ISP != "":
            print(f"\n{RED}[{YELLOW}RESULT{RED}]{WHITE} ISP = {WHITE}{ISP}")
            log.write(f"[RESULT] ISP = {ISP}\n")
        else:
            print(f"\n{YELLOW}[{RED}EMPTY{YELLOW}]{WHITE} ISP = {YELLOW}NA{WHITE}")
            log.write("[RESULT] ISP = NA\n")

        sleep(2)
        if CITY != "" and CITY != "Unknown":
            print(f"\n{RED}[{YELLOW}RESULT{RED}]{WHITE} City = {WHITE}{CITY}")
            log.write(f"[RESULT] City = {CITY}\n\n")
        else:
            print(f"\n{YELLOW}[{RED}EMPTY{YELLOW}]{WHITE} City = {YELLOW}NA{WHITE}\n\n")
            log.write("[RESULT] City = NA\n\n")

        sleep(2)
        print(f"\n{RED}[{YELLOW}FINISHED{RED}]{WHITE} Basic scan Done. \n")
        log.write("[FINISHED] Basic scan Done.")
        log.close()
        sleep(2)
