import Adafruit_DHT
import time

senzor = Adafruit_DHT.DHT11             #Senzory pre vyuzitie(DHT_11/22)
#senzor = Adafruit_DHT.DHT22
senzor_pin = 4                      #DHT data pin pripojeny na GPIO4
cyklus = True                       #premenna pre while cyklus
dataList = []

while cyklus:                       #nekonecny while cyklus

    try:
        vlh, tep = Adafruit_DHT.read_retry(senzor, senzor_pin) #nacitanie hodnot zo senzora do premennych 
        tep_f = tep * 9/5.0 + 32                #teplota_f prevedena na fahrenheity
        
        dataDict = {
        "t": time.strftime('%H:%M:%S %d/%m/%Y'),
        "x": tep,
        "y": tep_f,
        "z": vlh,}
        dataList.append(dataDict)

        if vlh is not None and tep is not None and len(dataList)>0:         #podmienky pre premenne k 0
            print('TEPLOTA = ' + str(tep) +' *C,'+ 'TEPLOTA Fahrenheit = ' + str(tep_f) +' F,' + 'VLHKOST = ' + str(vlh) +' %.')    #vypisanie hodnot
            hod = str(dataList).replace("'","\"")   
            fo = open("hodnoty.txt","w")    
            fo.write("%s\r\n" %hod)             #ukladanie premennych do subora
            time.sleep(1800) 
        
            # if len(dataList)>0:
                  

        else:
            print('CHYBA! Skus znova!')
            time.sleep(1)

    except KeyboardInterrupt:                           #zastavenie cyklusu klavesou CTRL+C 
        print ('Program zastaveny!')                        #ako ked koncime server v termialy 
        cyklus = False
        fo.close()
        dataList = [];

