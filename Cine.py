import csv

def registrar_funcion():
    codigo = input("Código de la función: ")
    pelicula = input("Nombre de la película: ")
    sala = input("Sala: ")
    hora = input("Hora (12h): ")
    precio = 10000
    boletos = int(input("Cantidad máxima de boletos: "))

    with open("funciones.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([codigo, pelicula, sala, hora, precio, boletos])
    print("Función registrada.\n")


def listar_funciones():
    print("\n--- FUNCIONES DISPONIBLES ---")
    try:
        with open("funciones.csv", "r") as f:
            reader = csv.reader(f)
            for fila in reader:
                print(f"Código: {fila[0]}, Película: {fila[1]}, Sala: {fila[2]}, Hora: {fila[3]}, Precio: ${fila[4]}, Boletos: {fila[5]}")
    except FileNotFoundError:
        print("No hay funciones registradas aún.")
    print()


def vender_boletos():
    codigo = input("Ingrese el código de la función: ")
    cantidad = int(input("Cantidad de boletos: "))
    nuevas_funciones = []
    encontrada = False

    try:
        with open("funciones.csv", "r") as f:
            reader = csv.reader(f)
            for fila in reader:
                if fila[0] == codigo:
                    encontrada = True
                    pelicula = fila[1]
                    precio = int(fila[4])
                    boletos_disp = int(fila[5])

                    if cantidad <= 0 or cantidad > boletos_disp:
                        print("Cantidad inválida o insuficiente.")
                    else:
                        total = cantidad * precio
                        print(f"Total a pagar: ${total}")
                        confirmar = input("¿Confirmar venta? (s/n): ")
                        if confirmar.lower() == "s":
                            fila[5] = str(boletos_disp - cantidad)
                            with open("ventas.csv", "a", newline="") as v:
                                writer = csv.writer(v)
                                writer.writerow([codigo, pelicula, cantidad, total])
                            print("Venta realizada.")
                nuevas_funciones.append(fila)
    except FileNotFoundError:
        print("No hay funciones registradas.\n")
        return

    if not encontrada:
        print("Función no encontrada.\n")
    else:
        with open("funciones.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(nuevas_funciones)


def resumen_ventas():
    total_boletos = 0
    total_dinero = 0
    try:
        with open("ventas.csv", "r") as f:
            reader = csv.reader(f)
            print("\n--- RESUMEN DE VENTAS ---")
            for fila in reader:
                print(f"Película: {fila[1]}, Boletos: {fila[2]}, Total: ${fila[3]}")
                total_boletos += int(fila[2])
                total_dinero += int(fila[3])
        print(f"Boletos vendidos: {total_boletos}")
        print(f"Dinero recaudado: ${total_dinero}\n")
    except FileNotFoundError:
        print("No hay ventas registradas.\n")


def menu():
    while True:
        print("=== CINE MOVIETIME ===")
        print("1. Registrar función")
        print("2. Listar funciones")
        print("3. Vender boletos")
        print("4. Resumen de ventas")
        print("5. Salir")

        op = input("Elija una opción: ")

        if op == "1":
            registrar_funcion()
        elif op == "2":
            listar_funciones()
        elif op == "3":
            vender_boletos()
        elif op == "4":
            resumen_ventas()
        elif op == "5":
            print("Gracias por usar MovieTime.")
            break
        else:
            print("Opción no válida.\n")

menu()
