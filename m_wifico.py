# Outils pour la conexion WIFI
# Mon tout premier module pour Micropyton

from time import sleep,sleep_ms

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

from machine import Pin,Signal
led_inversed = Pin(2, Pin.OUT)
led = Signal(led_inversed, invert=True)
led.off()

import ujson

def lireF(file):
    f =open(file,'r')
    string =  f.read()
    f.close()
    return str(string)

def checkSSID(dict):
#voir pour se connecter au wifi instencier la carte wlan.
    scanWifi = []
    for i in wlan.scan():
        scanWifi.append(i[0].decode('utf8').strip())

    for ap in dict:
        for i in scanWifi:
            if (ap == i):
                return(i)

def blink(n):
	for i in range(int(n)):
		led.on()
		sleep_ms(200)
		led.off()

def myNetworks():
    mySSIDs = lireF('/utils/ssid_password.txt') # json en str()
    return ujson.loads(mySSIDs) # dictionnaire de tout ce qu'on connais comme AP!

def infoWifi(ssid):
    if(wlan.isconnected() == True):
        ip = wlan.ifconfig()[0]
    else:
        ip = "_.__"
    infos = {"ssid" : ssid, "ip" : wlan.ifconfig()[0]}
    return infos

def wifiConnect(tryCo):
    countr=0
    ssidFound = checkSSID(myNetworks()) # ssid scanné connu (suivant lieu) 

    if wlan.isconnected() == True: # Nous avons une ip connecte
        infos = infoWifi(ssidFound)
        print("Deja connecté. " + infos["ip"])
        blink(10)
        return infos 
    else:
        led.off()

    wlan.connect(ssidFound, myNetworks()[ssidFound])

    while (wlan.isconnected() == False): # Tant que pas connecté
        sleep(1)
        countr+=1

        if (countr > tryCo): # Abandonne si on dépasse le nombre d'essais
            print("N'est pas connecté au Wifi apres " + str(tryCo) + "  tentatives.")
     	    return 1
        else:
            pass # Fait recommencer la boucle
            # Continue ci-dessous si enfin connecté au wifi

    # A partir d'ici, le Wifi est forcement connecté
    infos = infoWifi(ssidFound)
    print("")
    print("Tentative(s) de connexion : " + str(countr))
    print("IP :" + infos["ip"])
    blink(10)

    return infos

def rssi():
    if(wlan.isconnected() == True):
        return wlan.status('rssi')

if __name__ == '__main__':
    from time import sleep

    wifiConnect()
