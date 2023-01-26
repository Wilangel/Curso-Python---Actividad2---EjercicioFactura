from factura import *


class Pago:
    def __init__(self, factura, monto):
        self.factura = factura
        self._monto = monto

    def get_numero_factura(self):
        return self.factura

    def set_monto(self, monto):
        self._monto = monto

    def get_monto(self):
        return self._monto

    def mostrar_pago_base(self):
        print(
            f"Pago realizado por la factura {self.factura}. Monto: {self._monto}")


class PagoDebito(Pago):
    def __init__(self, factura, monto):
        super().__init__(factura, monto)
        self._numero_tarjeta_debito = ""

    def set_numero_tarjeta_debito(self, numero):
        self._numero_tarjeta_debito = numero

    def get_numero_tarjeta_debito(self):
        return self._numero_tarjeta_debito

    def mostrar_pago(self):
        print(
            f"Pago con tarjeta de débito. Número de tarjeta: {self._numero_tarjeta_debito}. Monto: {super().get_monto()}")


class PagoCredito(Pago):
    def __init__(self, factura, monto):
        super().__init__(factura, monto)
        self._numero_tarjeta_credito = ""
        self._numero_cuotas = 0
        self._codigo_verificacion = ""

    def set_numero_tarjeta_credito(self, numero):
        self._numero_tarjeta_credito = numero

    def get_numero_tarjeta_credito(self):
        return self._numero_tarjeta_credito

    def set_numero_cuotas(self, cuotas):
        self._numero_cuotas = cuotas

    def get_numero_cuotas(self):
        return self._numero_cuotas

    def set_codigo_verificacion(self, codigo):
        self._codigo_verificacion = codigo

    def get_codigo_verificacion(self):
        return self._codigo_verificacion

    def mostrar_pago(self):
        print(
            f"Pago con tarjeta de crédito. Número de tarjeta: {self._numero_tarjeta_credito}. Número de cuotas: {self._numero_cuotas}. Código de verificación: {self._codigo_verificacion}. Monto: {super().get_monto()}")


class PagoEfectivo(Pago):
    def __init__(self, factura, monto):
        super().__init__(factura, monto)
    
    def mostrar_pago(self):
        print(
            f"Pago en Efectivo realizado por la factura {super().get_numero_factura()}. Monto: {super().get_monto()}")
