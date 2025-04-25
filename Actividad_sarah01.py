#sistema de validacion de productos

print("Buenos dias, bienvenido a nuestra tienda")
nombre_producto = input("Ingrese el nombre del producto: ")
while True:
    try: 
        precio_unitario = float(input("ingrese el precio unitario: "))
        if precio_unitario <= 0:
          print("el precio ingresado debe ser en numero positivo: ")
        else:
            break
    except ValueError:
     print("dato invalido, debe ingresar un numero valido" )

#validar cantidad
while True:
    try:
        cantidad = int(input("ingrese la cantidad de productos adquiridos: "))
        if cantidad <= 0:
         print("la cantidad debe ser un numero positivo.intente nuevamente ")
        else:
            break
    except ValueError:
         print("dato invalido,debe ingresar un numero entero valido ")

        #validar porcentaje de descuento
while True:
    try:
        descuento = float(input("ingrese el porcentaje de descuento (o a 100): "))
        if descuento < 0 or descuento > 100:
         print("el descuento debe estar entre 0 y 100%. intente nuevamente ") 
        else:
           break
    except ValueError:
     print("dato invalido,debe ingresar un numero valido")

#calculos 
subtotal = precio_unitario * cantidad
descuento_aplicado = subtotal *(descuento/100)
total_final = subtotal - descuento_aplicado

#salida de datos
print("resumen de compra")
print(f" producto: {nombre_producto}")
print(f"total sin descuento: $ {subtotal:.2f}")
print(f"descuento aplicado: $ {descuento_aplicado:.2f}")
print(f"total a pagar: ${total_final:.2f}")