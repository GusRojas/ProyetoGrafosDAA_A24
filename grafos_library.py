import random

class Nodo:
    def __init__(self, id):
        self.id = id

class Arista:
    def __init__(self, origen, destino, dirigido=False):
        self.origen = origen
        self.destino = destino
        self.dirigido = dirigido

class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = []
        self.aristas = []
        self.dirigido = dirigido

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def agregar_arista(self, arista):
        self.aristas.append(arista)

    def guardar_grafo_graphviz(self, filename):
        with open(filename, 'w') as f:
            f.write('digraph {\n')
            for nodo in self.nodos:
                f.write(f'  {nodo.id};\n')
            for arista in self.aristas:
                if arista.dirigido or self.dirigido:
                    f.write(f'  {arista.origen.id} -> {arista.destino.id};\n')
                else:
                    f.write(f'  {arista.origen.id} -- {arista.destino.id};\n')
            f.write('}')

def grafoMalla(m, n, dirigido=False):
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)
    nodos = [[None] * n for _ in range(m)]

    # Crear nodos
    for i in range(m):
        for j in range(n):
            nodo = Nodo(f'{i}_{j}')
            grafo.agregar_nodo(nodo)
            nodos[i][j] = nodo

    # Crear aristas
    for i in range(m):
        for j in range(n):
            if i + 1 < m:
                grafo.agregar_arista(Arista(nodos[i][j], nodos[i+1][j], dirigido))
            if j + 1 < n:
                grafo.agregar_arista(Arista(nodos[i][j], nodos[i][j+1], dirigido))

    return grafo

def grafoErdosRenyi(n, m, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)
    nodos = [Nodo(str(i)) for i in range(n)]
    grafo.nodos = nodos

    if m < n - 1:
        raise ValueError("El número de aristas no puede ser menor que n - 1")

    aristas_disponibles = []
    for i in range(n):
        for j in range(i + 1, n):
            aristas_disponibles.append((i, j))

    aristas_elegidas = random.sample(aristas_disponibles, m)
    for arista in aristas_elegidas:
        origen, destino = arista
        grafo.agregar_arista(Arista(nodos[origen], nodos[destino], dirigido))

    return grafo

def grafoGilbert(n, p, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)
    nodos = [Nodo(str(i)) for i in range(n)]
    grafo.nodos = nodos

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                grafo.agregar_arista(Arista(nodos[i], nodos[j], dirigido))

    return grafo

def grafoGeografico(n, r, dirigido=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    grafo = Grafo(dirigido)
    nodos = [Nodo(str(i)) for i in range(n)]
    grafo.nodos = nodos

    for i in range(n):
        for j in range(i + 1, n):
            # Simplemente se asume que las coordenadas de los nodos son valores entre 0 y 1
            distancia = random.uniform(0, 1)
            if distancia <= r:
                grafo.agregar_arista(Arista(nodos[i], nodos[j], dirigido))

    return grafo

def grafoBarabasiAlbert(n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if d < 1:
        raise ValueError("El grado máximo esperado debe ser al menos 1")

    grafo = Grafo(dirigido)
    nodos = [Nodo(str(i)) for i in range(n)]
    grafo.nodos = nodos

    # Conectar los primeros d nodos con todos los demás
    for i in range(d):
        for j in range(i + 1, n):
            grafo.agregar_arista(Arista(nodos[i], nodos[j], dirigido))

    # Añadir nodos uno por uno
    for i in range(d, n):
        conexiones = random.choices(nodos[:i], k=d)
        for nodo in conexiones:
            grafo.agregar_arista(Arista(nodos[i], nodo, dirigido))

    return grafo

def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Dorogovtsev-Mendes
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    if n < 3:
        raise ValueError("El número de nodos debe ser al menos 3")

    grafo = Grafo(dirigido)
    nodos = [Nodo(str(i)) for i in range(3)]
    grafo.nodos = nodos

    # Crear triángulo inicial
    grafo.agregar_arista(Arista(nodos[0], nodos[1], dirigido))
    grafo.agregar_arista(Arista(nodos[1], nodos[2], dirigido))
    grafo.agregar_arista(Arista(nodos[2], nodos[0], dirigido))

    # Añadir nodos y conectarlos a una arista al azar
    for i in range(3, n):
        arista_seleccionada = random.choice(grafo.aristas)
        nuevo_nodo = Nodo(str(i))
        grafo.agregar_nodo(nuevo_nodo)
        grafo.agregar_arista(Arista(nuevo_nodo, arista_seleccionada.origen, dirigido))
        grafo.agregar_arista(Arista(nuevo_nodo, arista_seleccionada.destino, dirigido))
        # Eliminar la arista seleccionada
        grafo.aristas.remove(arista_seleccionada)

    return grafo
