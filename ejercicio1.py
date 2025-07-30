import csv
import os

#  Ruta al archivo CSV
DATA_DIR = r'C:\Users\orlin\Documents\Visual Studio Code\Uniciencia\data'
CSV_FILE = os.path.join(DATA_DIR, 'math_operations.csv')

#  Diccionario que asocia operaciones con funciones
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return a / b if b != 0 else 'Error: División por cero'
def potencia(a, b): return a ** b

OPERACIONES = {
    'SUMA': sumar,
    'SUB': restar,
    'MUL': multiplicar,
    'DIV': dividir,
    'POW': potencia
}

#  Leer operaciones desde el archivo CSV con delimitador ;
def leer_operaciones(ruta_archivo):
    with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)  # No especificar delimiter, por defecto es coma
        operaciones = []
        for fila in lector:
            print(f"DEBUG fila leída: {fila}")
            operaciones.append(fila)
    return operaciones

#  Ejecutar las operaciones y añadir resultados
def procesar_operaciones(operaciones):
    for fila in operaciones:
        operacion = fila['operation'].strip().upper()
        op1 = float(fila['operand_1'])
        op2 = float(fila['operand_2'])

        if operacion in OPERACIONES:
            resultado = OPERACIONES[operacion](op1, op2)
        else:
            resultado = 'Operación inválida'

        fila['result'] = resultado
    return operaciones

#  Guardar resultados en el archivo CSV actualizado
def guardar_operaciones(ruta_archivo, operaciones):
    campos = list(operaciones[0].keys())
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(operaciones)

#  Función principal
def main():
    if not os.path.exists(CSV_FILE):
        print(f' El archivo {CSV_FILE} no existe.')
        return

    print(' Leyendo archivo...')
    operaciones = leer_operaciones(CSV_FILE)

    print(' Procesando operaciones...')
    operaciones_procesadas = procesar_operaciones(operaciones)

    print(' Guardando archivo actualizado...')
    guardar_operaciones(CSV_FILE, operaciones_procesadas)

    print('✅ Proceso completado. Revisa el archivo actualizado en data/math_operations.csv')

if __name__ == '__main__':
    main()
