#Dylan Rojas
# --- Configuración y Constantes ---
N = 8  # Define el tamaño del tablero (8x8)
# 8 posibles movimientos del caballo (dFila, dColumna)
MOVS = [
    (2, 1), (1, 2), (-1, 2), (-2, 1), 
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def es_valido(f, c):
    """Verifica si la posición está en el tablero."""
    return 0 <= f < N and 0 <= c < N

def contar_opciones(tab, f, c):
    """Cuenta movimientos NO visitados desde (f, c) para la optimización de Warnsdorff."""
    conteo = 0
    for df, dc in MOVS:
        f_sig, c_sig = f + df, c + dc
        if es_valido(f_sig, c_sig) and tab[f_sig][c_sig] == 0:
            conteo += 1
    return conteo

def obtener_movimientos_ordenados(tab, f, c):
    """Genera y ordena los movimientos posibles (Warnsdorff: menor conteo primero)."""
    opciones = []
    for df, dc in MOVS:
        f_sig, c_sig = f + df, c + dc
        if es_valido(f_sig, c_sig) and tab[f_sig][c_sig] == 0:
            opciones_futuras = contar_opciones(tab, f_sig, c_sig)
            opciones.append((opciones_futuras, f_sig, c_sig))
            
    opciones.sort() # Ordenar por el conteo (la heurística de Warnsdorff)
    return opciones

def buscar_una_solucion(tablero, f_actual, c_actual, paso):
    """
    Función de Backtracking (recursiva) para encontrar SOLO la primera solución.
    Retorna True al encontrarla, deteniendo la búsqueda.
    """
    tablero[f_actual][c_actual] = paso

    if paso == N * N:
        # Base de la Recursión: ¡Éxito! Tour completo.
        return True 

    # Optimización: Obtener y probar los movimientos en el orden de Warnsdorff
    movs_ordenados = obtener_movimientos_ordenados(tablero, f_actual, c_actual)
    
    for _, f_sig, c_sig in movs_ordenados:
        
        # Llamada Recursiva: Si encuentra la solución en una rama, propagar el éxito
        if buscar_una_solucion(tablero, f_sig, c_sig, paso + 1):
            return True

        # Vuelta Atrás (Backtrack): Si la rama falló, la casilla debe desmarcarse
        # para que otras ramas la puedan usar.
        # No es necesario aquí, ya que el desmarcado final de la función lo cubre.
        
    # Si todos los caminos fallaron desde esta posición, desmarcarla
    # (Excepto si es la casilla de inicio)
    if paso > 1:
        tablero[f_actual][c_actual] = 0
        
    return False # No se encontró una solución en esta rama

# --- Ejecución y Resultado ---
tablero_resultado = [[0] * N for _ in range(N)]
f_inicio, c_inicio = 0, 0 

# Iniciar la búsqueda
exito = buscar_una_solucion(tablero_resultado, f_inicio, c_inicio, 1)

# Mostrar el resultado
print("---------------------------------------")
print(f"✅ Búsqueda Garantizada (Backtracking): {'Éxito' if exito else 'Fallo'}")
print("---------------------------------------")
for fila in tablero_resultado:
    print(" | ".join(f"{num:02d}" for num in fila))
print("---------------------------------------")