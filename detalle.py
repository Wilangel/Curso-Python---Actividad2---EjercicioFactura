class Detalle:
    def __init__(self, codigo_producto, descripcion, cantidad, valor_unitario):
        self.codigo_producto = codigo_producto
        self.descripcion = descripcion
        self.cantidad=cantidad
        self.valor_unitario = valor_unitario
        self.subtotal = valor_unitario*cantidad