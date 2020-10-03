import dht
import machine
import time

    

beta = dht.DHT11(machine.Pin(2))

while True:

    d.measure()
    print(d.temperature())
    

    response.close()    
    time.sleep(20)