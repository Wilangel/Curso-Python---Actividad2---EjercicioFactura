

class Factura:
    def __init__(self, numero_factura, nit, razon_social, cliente):
        self.numero_factura = numero_factura
        self.nit = nit
        self.razon_social = razon_social
        self.cliente = cliente
        self.detalles = []

    def add_detalle(self, detalle):
        self.detalles.append(detalle)

    def get_numero_factura(self):
        return self.numero_factura

    def get_total(self):
        total = 0
        for detalle in self.detalles:
            total += detalle.subtotal
        return total

