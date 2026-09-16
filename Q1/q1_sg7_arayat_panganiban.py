'''

25 / Louise Cassidy D. Panganiban
9 - Arayat
SG7 Activity

'''
class Glassware:
    def __init__(self, material = "glass"):
        self.material = material
        
class Beaker(Glassware):
    def __init__(self, material = "borosilicate glass"):
        super().__init__(material = material)
        
class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]
        
tray = Tray()

print(f'The tray contains {len(tray.beakers)} beakers made of {tray.beakers[0].material}.')

del tray
