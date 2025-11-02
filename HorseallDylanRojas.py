# --- 1. CONFIGURACIÓN E INICIO ---
def obtener_N():
    """Solicita y valida el tamaño N del tablero al usuario."""
    while True:
        try:
            N_val = int(input("Ingrese el tamaño del lado del tablero (N): "))
            return N_val
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

N = obtener_N()
MOVS = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
soluciones_encontradas = 0

# --- 2. FUNCIONES DE OPTIMIZACIÓN Y VALIDACIÓN ---
def es_valido(f, c):
    """Verifica si la posición (f, c) está dentro de los límites del tablero N x N."""
    return 0 <= f < N and 0 <= c < N

def contar_opciones(tab, f, c):
    """Cuenta cuántos saltos no visitados hay desde (f, c) (Heurística de Warnsdorff)."""
    conteo = 0
    for df, dc in MOVS:
        f_sig, c_sig = f + df, c + dc
        if es_valido(f_sig, c_sig) and tab[f_sig][c_sig] == 0:
            conteo += 1
    return conteo

def obtener_movimientos_ordenados(tab, f, c):
    """Genera y ordena los movimientos posibles, poniendo primero la opción con menos salidas futuras."""
    opciones = []
    for df, dc in MOVS:
        f_sig, c_sig = f + df, c + dc
        if es_valido(f_sig, c_sig) and tab[f_sig][c_sig] == 0:
            opciones.append((contar_opciones(tab, f_sig, c_sig), f_sig, c_sig))
            
    opciones.sort() # Ordena por el conteo (Warnsdorff)
    return opciones

def imprimir_solucion(tablero):
    """Muestra el tablero cuando se encuentra un tour completo y actualiza el contador global."""
    global soluciones_encontradas
    soluciones_encontradas += 1
    print(f"\n======== SOLUCIÓN #{soluciones_encontradas} ========")
    for fila in tablero:
        print(" | ".join(f"{num:02d}" for num in fila))
    print("=================================================")

# --- 3. ALGORITMO DE BACKTRACKING ---
def buscar_soluciones(tablero, f_act, c_act, paso):
    """Función recursiva de Backtracking: busca y reporta todas las soluciones, usando Warnsdorff para optimizar el orden."""
    tablero[f_act][c_act] = paso # Marcar la casilla con el paso actual

    if paso == N * N:
        imprimir_solucion(tablero) # Caso base: Solución encontrada
    else:
        # Usar movimientos ordenados (optimización)
        movs_ordenados = obtener_movimientos_ordenados(tablero, f_act, c_act)

        for _, f_sig, c_sig in movs_ordenados:
            
            buscar_soluciones(tablero, f_sig, c_sig, paso + 1) # Llamada recursiva
            
            tablero[f_sig][c_sig] = 0 # Vuelta Atrás: Desmarcar casilla

    # Desmarcar la casilla actual al terminar la exploración de sus ramas
    if paso > 1:
        tablero[f_act][c_act] = 0

# --- 4. EJECUCIÓN ---
tablero_inicial = [[0] * N for _ in range(N)]
f_inicio, c_inicio = 0, 0 

print(f"\nIniciando búsqueda optimizada en un tablero de {N}x{N}...")
buscar_soluciones(tablero_inicial, f_inicio, c_inicio, 1)

# --- 5. RESUMEN FINAL ---
print("\n=================================================")
print("             ✨ BÚSQUEDA FINALIZADA ✨")
print(f"Total de Soluciones Encontradas: {soluciones_encontradas}")
print("=================================================")