class Prodotto:

    aliquota_iva = 0.22 # variabile di classe

    def __init__(self, name: str, price: float, quantity: float, supplier: str):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore_netto(self):
        return self.price * self.quantity

    def valore_lordo(self):
        netto = self.valore_netto()
        lordo = netto * (1 + self.aliquota_iva)
        return lordo

    @classmethod
    def costruttore_con_quantità_uno(cls, name: str, price: float, supplier: str):
        return cls(name, price, 1, supplier)

    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo * (1 - percentuale)

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione, il prezzo non può essere negativo.")
        self.price = valore

myProduct1 = Prodotto(name = "Laptop", price = 1200.0, quantity = 12, supplier = "ABC")

print(f"Nome prodotto: {myProduct1.name} - prezzo: {myProduct1.price}")

print(f"Il totale lordo di myProduct1 è {myProduct1.valore_lordo()}")
p3 = Prodotto.costruttore_con_quantità_uno(name = "Auricolari", price = 200.0, supplier = "DEF")
print(f"Prezzo scontato di myProduct1 {Prodotto.applica_sconto(myProduct1.price, 0.22)}")

myProduct2 = Prodotto(name = "Mouse", price = 10, quantity = 25, supplier = "CDE")
print(f"Nome prodotto: {myProduct2.name} - prezzo: {myProduct2.price}")


class Cliente:
    def __init__(self, nome: str, mail: str, categoria: str):
        self.nome = nome
        self.mail = mail
        self.categoria = categoria

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.mail}"

c1 = Cliente(nome = "Mario Bianchi", mail = "mario.bianchi@polito.it", categoria = "Gold")
print(c1.descrizione())