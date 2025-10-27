#CABALLO

MAX = 5  # tamaño del tablero, solucion en 5x5, 8x8

mov_x = [2, 1, -1, -2, -2, -1, 1, 2] #movimientos posibles para el caballo
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

def valida(tablero, x, y): #verifica que la posición esté libre y en el tablero
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == -1

def final(tablero): 
    for i in range(MAX): #True si todos los espacios estan usados
        for j in range(MAX):
            if tablero[i][j] == -1:
                return False
    return True

def mostrar_tablero(tablero): #presenta tablero en pantalla
    for fila in tablero:
        print(" ".join(f"{c:2d}" for c in fila))
    print()

# backtracking
def solucion(tablero, x, y, paso):
    if paso == MAX * MAX:
        return True

    for i in range(8): #prueba movimientos posibles del caballo
        nx = x + mov_x[i]
        ny = y + mov_y[i]
        if valida(tablero, nx, ny):
            tablero[nx][ny] = paso
            if solucion(tablero, nx, ny, paso + 1): 
                return True
            tablero[nx][ny] = -1  #si no funciona, retrocede
    return False

def main():
    tablero = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    tablero[0][0] = 0  #inicio

    if solucion(tablero, 0, 0, 1):
        print(f"\nRecorrido completo del caballo en tablero {MAX}x{MAX}:\n")
        mostrar_tablero(tablero)
    else:
        print("No hay solución.")

main() #ejecutar, no me funcionaba sin esto