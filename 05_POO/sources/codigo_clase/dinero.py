class Dinero:
    MONEDAS = {
    1: "$",
    2: "USD",
    3: "EUR"
    }

    def __init__(self, monto, moneda):
        if moneda not in self.MONEDAS.values():
           return  f"Moneda no válida: {moneda}"
    
        self.monto = monto
    
        if moneda == "$":
            self.moneda = 1
        elif moneda == "USD":
            self.moneda = 2
        elif moneda == "EUR":
            self.moneda = 3 
    
    def __str__(self):
        return f"{self.monto}{self.MONEDAS[self.moneda]}"
    
    def __repr__(self):
        return f"Dinero({self.monto}, '{self.MONEDAS[self.moneda]}')"

    def __add__(self, otro):

        if isinstance(otro, Dinero):
            if self.moneda == otro.moneda:
                return Dinero(self.monto + otro.monto,
                              self.MONEDAS[self.moneda])
            else:
                print("Las monedas son distintas")
        else:
            print("Solo se puede sumar dinero con dinero")

    def __radd__(self, otro):
        self.__add__(otro)

    def __sub__(self, otro):

        if self.moneda == otro.moneda:
            return Dinero(self.monto - otro.monto,
                          self.MONEDAS[self.moneda])
        else:
            print("Las monedas son distintas")


a = Dinero(100, "$")
b = Dinero(100, "$")

#__add__(a,b)
c = a + b
c = a.__add__(b)
