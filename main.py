productos = {}
class Producto:
    
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = 0


    def calcular_precio_venta(self):
        if self.margen_de_venta < 1:
            self.precio_de_venta = self.costo / (1 - self.margen_de_venta)
        else:
            print("Error: El margen de venta debe ser menor a 1.")

    def registrar_producto(self):
        self.calcular_precio_venta()
        if self.id in productos:
            print(f"El producto con el id '{self.id}' ya existe")
        if not self.id in productos:
            producto = {
                'ID': self.id,
                'Nombre': self.nombre,
                'Descripción': self.descripcion,
                'Costo': self.costo,
                'Cantidad': self.cantidad,
                'Precio de Venta': self.precio_de_venta
            }
            productos[self.id] = producto
            print( "Registro exitoso")
def ver():
    if not productos:
        print("\nNo hay productos registrados.")
    else:
        print("\nListado de Productos:")
        for id, producto in productos.items():
            print(f'Producto {id}: {producto}')
def run():
    op = ""
    while op != '3':
        menu() 
        op= input("\nEscoga una opcion\n")
        if op == "1":
            try:
                id = int(input("ingrese el id ---> "))
                nombre = input("ingrese el nombre ---> ")
                descripcion = input("Ingrese la descripcion ---> ")
                costo = int(input("ingrese el costo ---> "))
                cantidad = int (input("Ingrese la cantida ---> "))
                margenventa = float(input("ingrese el margen de venta ---> "))
                producto = Producto(id,nombre,descripcion,costo,cantidad,margenventa)
                producto.registrar_producto()
            except Exception as e:
                print("Error",e)
        if op == "2":
            ver()
            

def menu():
    print("\nBienvenido al Registro de Productos")
    print("1. Registrar un nuevo producto")
    print("2. Mostrar listado de productos")
    print("3. Salir")
run()