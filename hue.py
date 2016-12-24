import requests
import time
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

username = 'hrllicfRo-pAYdPbCLZDm6vwEmLMpiG8l-6Sc5kz'
IP = '10.0.0.5'

kitchen = [1,2]
room = [3,4]
living = [5,6]

if __name__ == '__main__':

    mode = raw_input(bcolors.OKBLUE + "Is your name Tori Fry? " + bcolors.ENDC)

    if mode.upper() == 'YES':
    
        chill_spot = raw_input(bcolors.OKBLUE + "Would you like to hang in the Igloo, the Discotequa Kitchen, or the Chliving Room? " + bcolors.ENDC)

        if chill_spot.upper() == 'IGLOO':
            for i in room:
                requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "sat":255, "bri":10,"hue":46920})
                print 'Light '+str(i)+' illuminated.'
                time.sleep(0.1)

        elif chill_spot.upper() == "DISCOTEQUA KITCHEN":
            while 1>0:
                saturation = random.randint(230,255)
                brightness = random.randint(0,255)
                color = random.randint(0,65280)

                for i in room:
                    requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "sat":saturation, "bri":brightness,"hue":color})
                    print 'Light '+str(i)+' illuminated.'
                    time.sleep(0.2)
    
                for i in kitchen:
                        requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "sat":saturation, "bri":brightness,"hue":color})
                        print 'Light '+str(i)+' illuminated.'
                        time.sleep(0.2)
    
                for i in living:
                        requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "sat":saturation, "bri":brightness,"hue":color})
                        print 'Light '+str(i)+' illuminated.'
                        time.sleep(0.2)

        elif chill_spot.upper() == "CHLIVING ROOM":
            for i in living:
                #requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "sat":50, "bri":100,"hue":10000})
                #requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "xy":[0.7,0.3]})
                requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "bri":100, "ct":400})
                print 'Light '+str(i)+' illuminated.'
            for i in kitchen:
                #requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "sat":50, "bri":100,"hue":10000})
                requests.put('http://'+IP+'/api/'+username+'/lights/'+str(i)+'/state', json = {"on":"true", "bri":50, "ct":400})
                print 'Light '+str(i)+' illuminated.'

        else:
            print bcolors.FAIL + "Not an option, homie." + bcolors.ENDC

        print bcolors.OKBLUE + "Success." + bcolors.ENDC

    else:
        print bcolors.FAIL + "Sorry, this program is not for you..." + bcolors.ENDC
