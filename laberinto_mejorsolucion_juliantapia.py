import math
# Dimensión del tablero
MAX = 10
# Definir listas donde se guardaran los nodos candidatos y los ya probados
lista_abierta = []
lista_cerrada = []
# Definir grafo como una matriz de 0

# Estructura de un nodo: nodo = {'coordenadas':(x,y), 'g':numero, 'h':numero, 'f':h+g, 'padre':(x_o,y_o)}

def definir_nodo(coordenadas,g,h,padre):
    nodo = {'coordenadas':coordenadas, 'g':g, 'h':h, 'f':h+g, 'padre':padre}
    return nodo

def distancia_entre_dos_nodos(coordenada_1,coordenada_2):
    x_1,y_1 = coordenada_1
    x_2,y_2 = coordenada_2
    delta_x = abs(x_1 - x_2)
    delta_y = abs(y_1 - y_2)
    n_1 = abs(delta_x - delta_y)
    n_2 = (abs(delta_x + delta_y) - n_1)/2
    distancia = 10*n_1 + 14*n_2
    return distancia

def encontrar_camino_mas_corto(nodo_meta,inicio):
    lista_camino_mas_corto = []
    nodo_actual = nodo_meta
    while nodo_actual != inicio:
        lista_camino_mas_corto.append(nodo_actual['coordenadas'])
        for nodo in lista_cerrada:
            if nodo_actual['padre'] == nodo['coordenadas']:
                nodo_actual = nodo
                break
    lista_camino_mas_corto.append(inicio['coordenadas'])
    return lista_camino_mas_corto

def costo_mas_bajo():
    lista_f = []
    lista_h = []
    candidatos_f = []
    for elemento in lista_abierta:
        lista_f.append(elemento['f'])
    menor_f = min(lista_f)
    for elemento in lista_abierta:
        if menor_f == elemento['f']:
            candidatos_f.append(elemento)
    for elemento in candidatos_f:
        lista_h.append(elemento['h'])
    menor_h = min(lista_h)
    for elemento in candidatos_f:
        if elemento['h'] == menor_h:
            return elemento

def verificar_nodo_en_lista(lista,coordenadas_nodo):
    for nodo in lista:
        if nodo['coordenadas'] == coordenadas_nodo:
            return True
    return False

def crear_nodos_vecinos(coordenadas_padre):
    lista = []
    x,y = coordenadas_padre
    mov_x = [0,1,1,1,0,-1,-1,-1]
    mov_y = [1,1,0,-1,-1,-1,0,1]
    for i in range(8):
        nueva_x = x + mov_x[i]; nueva_y = y + mov_y[i]
        if 0<=nueva_x<MAX and 0<=nueva_y<MAX:
            lista.append((nueva_x,nueva_y))
    return lista

def encontrar_nodo_por_coordenada(lista,coordenada):
    for nodo in lista:
        if nodo['coordenadas'] == coordenada:
            return nodo

def agregar_obstaculos(grafo,lista_obstaculos):
    for elemento in lista_obstaculos:
        x,y = elemento
        grafo[x][y] = '▩'
    
    
lista_camino = []

# Main

inicio = definir_nodo((0,0),0,0,(0,0))

lista_abierta.append(inicio)

final = (9,9)

grafo = [['◻' for i in range(0,10)] for j in range(0,10)]

agregar_obstaculos(grafo,[(0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 5), (1, 6), (1, 8), (2, 1), (2, 3),
                    (2, 8), (3, 1), (3, 3), (3, 4), (3, 5), (3, 6), (3, 8), (4, 1), (4, 6), (4, 8),
                    (5, 3), (5, 4), (5, 6), (5, 8), (6, 1), (6, 2), (6, 3), (6, 4), (6, 6), (6, 8),
                    (7, 1), (7, 8), (8, 1), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8), (9, 3), (9, 4)])

while lista_abierta != [] and lista_camino == []:
    
    nodo_actual = costo_mas_bajo()
    lista_abierta.remove(nodo_actual)
    lista_cerrada.append(nodo_actual)
    
    if nodo_actual['coordenadas'] == final:
        lista_camino = encontrar_camino_mas_corto(nodo_actual,inicio)
        
    lista_nodos_vecinos = crear_nodos_vecinos(nodo_actual['coordenadas'])
    
    for vecino in lista_nodos_vecinos:
        x,y = vecino
        
        if grafo[x][y] != '◻' or verificar_nodo_en_lista(lista_cerrada,vecino):
            continue
        else:
            vecino_g = nodo_actual['g'] + distancia_entre_dos_nodos(vecino,nodo_actual['coordenadas'])
            vecino_h = distancia_entre_dos_nodos(vecino,final)
            vecino_f = vecino_g + vecino_h

            if not(verificar_nodo_en_lista(lista_abierta,vecino)):
                pass
            else:
                vecino_gemelo = encontrar_nodo_por_coordenada(lista_abierta,vecino)
                if vecino_g >= vecino_gemelo['g']:
                    continue
                else:
                    lista_abierta.remove(vecino_gemelo)
                
            nodo_vecino = definir_nodo(vecino,vecino_g,vecino_h,nodo_actual['coordenadas'])
            lista_abierta.append(nodo_vecino)
print('Coordenadas recorrido:')
print(lista_camino,'\n')
if lista_camino !=[]:
    for coordenada in lista_camino:
        x,y = coordenada
        grafo[x][y] = '◼'
    grafo[final[0]][final[1]] = 'x'
    for fila in grafo:
        suma = ''
        for elemento in fila:
            suma += str(elemento) + '  '
        print(suma)
