import random
from cliente import Cliente
from detalle import Detalle
from factura import Factura
import pago
cliente = Cliente("001", "Juan Perez", "Calle 123", "555-5555", "Fisica")
# Crear una instancia de la clase Factura
factura = Factura("00001", "123456789", "Empresa S.A.", cliente)
# Crear instancias de la clase Detalle y agregarlas a la factura
detalle1 = Detalle("C001", "arroz", 2, 2000)
factura.add_detalle(detalle1)
detalle2 = Detalle("C002", "Carne", 4, 3000 )
factura.add_detalle(detalle2)
detalle3 = Detalle("C003", "leche", 2, 2500)
factura.add_detalle(detalle3)
# Obtener el total de la factura
print("El monto a pagar es: ",factura.get_total())
print("Se procede a pago.")

# realizar pago

pg=pago.Pago(factura.get_numero_factura(), factura.get_total())

option=int(input("Como desea pagar?\n1) Efectivo\n2) Debito\n3) Credito\n"))
match option:
    case 1:
        pgEfec=pago.PagoEfectivo(factura.get_numero_factura(), pg.get_monto())
        pgEfec.mostrar_pago()
    
    case 2:
        pgDeb=pago.PagoDebito(factura.get_numero_factura(), pg.get_monto())
        pgDeb.set_numero_tarjeta_debito(random.randint(323000000, 323999999))
        pgDeb.mostrar_pago()
        pgDeb.mostrar_pago_base()

    case 3:
        pgCred=pago.PagoCredito(factura.get_numero_factura(), pg.get_monto())
        pgCred.set_numero_cuotas(random.randint(0,6))
        pgCred.set_numero_tarjeta_credito(random.randint(323000000, 323999999))
        pgCred.set_codigo_verificacion(random.randint(100,999))
        pgCred.mostrar_pago()
        pgCred.mostrar_pago_base()
    
    case default:
        exit()


'''
#imprimir Factura
print(
    "Factura: ", factura.numero_factura ,"      ","NIT: ", factura.nit,"        ","Razon Social: ", 
)
'''