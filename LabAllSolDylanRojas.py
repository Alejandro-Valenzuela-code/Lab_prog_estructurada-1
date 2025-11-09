def ver(T):
    """Muestra el tablero."""
    for f in T:
        print(" ".join(f"{c:2}" for c in f))

def buscar_todo(T, x, y, p, L):
    """Busca todas las rutas posibles."""
    N = len(T)
    
    # Detenerse si fuera de limites O ya visitada
    if x < 0 or x >= N or y < 0 or y >= N or T[x][y] != 0:
        return

    T[x][y] = p # Marcar la casilla actual
    
    # ÉXITO: Si llegamos al final (N*N pasos)
    if x == N-1 and y == N-1 and p == N*N:
        L.append([f.copy() for f in T]) # Guardar ruta
    else:
        # Probar los 4 caminos. ¡Siempre probamos todos!
        buscar_todo(T, x+1, y, p+1, L) 
        buscar_todo(T, x, y+1, p+1, L) 
        buscar_todo(T, x-1, y, p+1, L) 
        buscar_todo(T, x, y-1, p+1, L) 
        
    T[x][y] = 0 # Deshacer la marca (Retroceder)

# --- INICIO ---
N = int(input("Tamaño (ej. 4): "))
T = [[0] * N for _ in range(N)] 
RUTAS = [] 

print(f"\nBuscando todas las rutas en {N}x{N}...")
buscar_todo(T, 0, 0, 1, RUTAS)

if RUTAS:
    print(f"\n¡Se encontraron {len(RUTAS)} rutas totales!")
    print("Mostrando la primera:")
    ver(RUTAS[0])
else:
    print("\nNo hay rutas posibles.")