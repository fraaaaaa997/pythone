""" realizzare un classe SodaCan che rappresenti una lattina di bibit, quindi, di forma cilindrica,
dotata dei metodi:

getSurfaceArea() e getVolume(), che restituiscono rispettivamente:
la superficie totale e il volume della lattina

Il costruttore riceve come argomenti il raggio della base e l'altezza della lattina. """

import math

class SodaCan:
    def __init__(self, raggio, altezza):
        self.raggio = raggio
        self.altezza = altezza

    def getSurfaceArea(self):
        area_laterale = 2 * math.pi * self.raggio * self.altezza
        area_basi = 2 * math.pi * self.raggio ** 2
        return area_laterale + area_basi

    def getVolume(self):
        return math.pi * self.raggio ** 2 * self.altezza


if __name__ == "__main__":
  
    lattina = SodaCan(5, 10)

    superficie = lattina.getSurfaceArea()
    volume = lattina.getVolume()

    print(f"Superficie: {superficie:.2f} cm²")
    print(f"Volume: {volume:.2f} cm³")



    