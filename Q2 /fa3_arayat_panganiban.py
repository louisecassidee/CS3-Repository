'''

25 / Louise Cassidy D. Panganiban
9 - Arayat
Q2 - FA3

'''
from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass
    
class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH"
        
class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

phsensor = PHSensor()
tempsensor = TempSensor()

print("--- Lab Inventory System ---")
print("[pH Sensor] Reading:", phsensor.get_reading(), "(Neutral)")
print("[Temperature Sensor] Reading:", tempsensor.get_reading())
print("----------------------------")
