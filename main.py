from machine import Pin
from time import sleep
import dht 

# Configuración del sensor DHT22 (o DHT11)
sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))  # Descomenta esta línea si usas un DHT11

# Configuración del pin del ventilador
ventilador = Pin(4, Pin.OUT)


while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        
        print('Temperature: %3.1f C' % temp)
        print('Temperature: %3.1f F' % temp_f)
        print('Humidity: %3.1f %%' % hum)
        
        # Control del ventilador basado en la temperatura
        if temp >= 28.8:
            ventilador.off()  # Encender el ventilador
            print("Ventilador encendido")
        else :
            ventilador.off()   # Apagar el ventilador
            print("Ventilador apagado")
            
    except OSError as e:
        print('Failed to read sensor:', e)
