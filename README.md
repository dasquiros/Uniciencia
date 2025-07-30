# Procesador de Operaciones Matemáticas desde CSV

Este proyecto en Python permite leer un archivo `.csv` con operaciones matemáticas (como suma, resta, multiplicación, etc.), procesarlas automáticamente y guardar los resultados en el mismo archivo.

## ¿Cómo funciona?

El script realiza lo siguiente:

1. Lee un archivo CSV (`math_operations.csv`) que contiene operaciones a realizar.
2. Interpreta cada fila como una operación entre dos operandos.
3. Ejecuta la operación matemática correspondiente.
4. Añade el resultado a la misma fila.
5. Guarda los resultados en el mismo archivo.

## Estructura esperada del archivo `math_operations.csv`

### Formato del archivo CSV

```csv
operand_1,operand_2,operation
5,3,SUMA
10,2,DIV
4,0,DIV
2,3,POW
El delimitador predeterminado es una coma ,.

Las operaciones válidas son:

SUMA (suma)

SUB (resta)

MUL (multiplicación)

DIV (división)

POW (potencia)

Funciones soportadas
| Código de operación | Función matemática                 |
| ------------------- | ---------------------------------- |
| SUMA                | a + b                              |
| SUB                 | a - b                              |
| MUL                 | a \* b                             |
| DIV                 | a / b (controla división por cero) |
| POW                 | a \*\* b                           |

python nombre_del_archivo.py
