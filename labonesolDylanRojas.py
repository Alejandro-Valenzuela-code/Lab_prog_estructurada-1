def mostrar(T):
    """Muestra el resultado final."""
    for fila in T:
        print(" ".join(f"{c:2}" for c in fila))

def jugar(T, x, y, p):
    """Busca la ruta con Ensayo y Error."""
    N = len(T)
    
    # 1. ¿Ganamos? (Llegar al final con todos los pasos hechos)
    if x == N-1 and y == N-1 and p == N*N:
        T[x][y] = p
        return True
    
    # 2. ¿La casilla es válida? (Dentro y Vacía)
    if 0 <= x < N and 0 <= y < N and T[x][y] == 0:
        T[x][y] = p # Dejar una marca (el número de paso)
        
        # 3. Probar Abajo, Derecha, Arriba, Izquierda. Si una ruta funciona, ¡listo!
        if (jugar(T, x+1, y, p+1) or
            jugar(T, x, y+1, p+1) or
            jugar(T, x-1, y, p+1) or
            jugar(T, x, y-1, p+1)):
            return True
        
        # 4. Si fallan las 4: Borrar la marca y retroceder
        T[x][y] = 0
        return False

# --- Empezar el Juego ---
try:
    N = int(input("Tamaño del tablero (ej. 4): "))
    if N <= 0: raise ValueError
except:
    N = 3
    print("Usaremos N=3.")

T = [[0] * N for _ in range(N)] # Crear tablero vacío (T)

print(f"\nBuscando ruta en {N}x{N}...")

# Empezar en (0, 0) con el paso 1
if jugar(T, 0, 0, 1):
    print("\n¡Ruta Encontrada!")
    mostrar(T)
else:
    print("\nNo hay ruta posible que visite todas las casillas.")