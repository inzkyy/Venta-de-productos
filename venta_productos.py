bodega=[]
def eliminar_producto(bodega,codigo):
    posicion= buscar_producto(bodega, codigo)
    if posicion !=-1:
            print(f"¿El producto que desea eliminar es {bodega[posicion]["nombre"]}?")
            opcion=int(input("1.Si 2.No\n"))
            if opcion == 1:
                bodega.pop(posicion)
                print("Producto eliminado con exito")
            else:
                print("Asegurese de escribir bien el codigo del producto")
    else:
            print("operacion cancelada, asegurese de poner bien el codigo del producto")
def mostrar_productos(bodega):
    print("==PRODUCTOS==")
    for producto in bodega:
        print("-"*20)
        print(f"Nombre: {producto["nombre"]}\nCodigo: {producto["codigo"]}\nPrecio: {producto["precio"]}\nStock: {producto["stock"]}")
        print("-"*20)
def vender_producto(bodega, codigo):
    posicion=buscar_producto(bodega, codigo)
    if posicion !=-1:
        print(f"¿El producto que desea comprar es {bodega[posicion]["nombre"]}?")
        opcion=int(input("1.Si 2.No\n"))
        if opcion==1:
            if bodega[posicion]["stock"]== 0:
                print("Lo siento no nos queda stock")
            else:
                bodega[posicion]["stock"]-=1
                print("Compra realizada con exito")
        else:
            print("Compra cancelada")
def buscar_producto(bodega, codigo):
    for i in range(len(bodega)):
        if bodega[i]["codigo"]== codigo:
            return i
    return -1
def validar_stock(stock):
    if stock >0:
        return True
    else:
        return False
def agregar_productos(bodega):
        print("==AGREGAR PRODUCTOS==")
        nombre= input("Ingresa nombre del producto: ")
        codigo=int(input("Ingresa codigo del producto: "))
        precio=float(input("Ingresa precio del producto: "))
        validar_precio(precio)
        stock=int(input("Ingresa stock del producto: "))
        validar_stock(stock)
        if validar_precio(precio)== True and validar_stock(stock) == True:
            producto={
                "nombre":nombre,
                "codigo":codigo,
                "precio":precio,
                "stock":stock
            }
            bodega.append(producto)
            print("Producto agregado con exito")
        else:
            print("Lo siento comprueba que todo este en orden para agregar un producto")
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False
def opcion():
    opcion=int(input("Ingresa una opcion:"))
    return opcion
def menu():
    while True:
        try:
            print("1. Agregar producto\n2. Buscar producto\n3. Vender producto\n4. Eliminar producto\n5. Mostrar productos\n6. Salir")
            match opcion():
                case 1:
                    agregar_productos(bodega)
                case 2:
                    print("==BUSCAR PRODUCTOS==")
                    codigo=int(input("Ingerse codigo a buscar: "))
                    posicion=buscar_producto(bodega, codigo)
                    if posicion !=-1:
                        print(f"Nombre: {bodega[posicion]["nombre"]}\nCodigo: {bodega[posicion]["codigo"]}\nValor: {bodega[posicion]["precio"]}\nStock: {bodega[posicion]["stock"]}")
                    else:
                        print("Producto no encontrado o lista vacia")
                case 3:
                    print("==VENDER PRODUCTOS==")
                    codigo= int(input("Ingrese codigo de producto a vender: "))
                    vender_producto(bodega, codigo)
                case 4:
                    print("==ELIMINAR PRODUCTO==")
                    codigo= int(input("Ingrese codigo de producto a eliminar: "))
                    eliminar_producto(bodega, codigo)
                case 5:
                    mostrar_productos(bodega)
                case 6:
                    print("Has salido de la tienda")
                    break
                case _:
                    print("Ingresa una opcion valida")
        except ValueError:
            print("Tipo de dato no valido")
def main():
    menu()

main()