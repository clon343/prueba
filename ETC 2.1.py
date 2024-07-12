import random
import csv
import math

# Lista de empleados con nombre y cargo
trabajadores = [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"}
]

# Asignación de sueldos aleatorios
sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados aleatoriamente.")

def clasificar_sueldos():
    print("Sueldos menores a $800.000 TOTAL:", len([s for s in sueldos if s < 800000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000 TOTAL:", len([s for s in sueldos if s > 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo: ${sueldo}")
    
    print("\nTOTAL SUELDOS:", sum(sueldos))

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${sueldo_promedio:.2f}")
    print(f"Media geométrica de sueldos: ${sueldo_geom:.2f}")

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Cargo", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], trabajador["cargo"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"Nombre empleado: {trabajador['nombre']} Cargo: {trabajador['cargo']} Sueldo Base: ${sueldo} Descuento Salud: ${descuento_salud:.2f} Descuento AFP: ${descuento_afp:.2f} Sueldo Líquido: ${sueldo_liquido:.2f}")

def salir_programa():
    print("Finalizando programa…")
    print("Desarrollado por [Su Nombre]")
    print("RUT [Su RUT]")

def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            asignar_sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos()
        elif opcion == 3:
            ver_estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
