- El código fuente
- Archivos GV generados, 3 por cada modelo; uno con 30, otro con 100 y el tercero con 500 nodos.
- Imágenes creadas con los grafos generados, 18 en total. Se sugiere utilizar Gephi (https://gephi.org/).

## Modelo Gm,n de malla

Crear m*n nodos. Para el nodo ni,j crear una arista con el nodo ni+1,j y otra con el nodo ni,j+1, para i<m y j<n

def grafoMalla(m, n, dirigido=False):
  """
  Genera grafo de malla
  :param m: número de columnas (> 1)
  :param n: número de filas (> 1)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """


Malla con 30 nodos:
![Malla de  30 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/malla30.png)

Malla con 100 nodos:
![Malla de  100 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/malla100.png)

Malla con 500 nodos:
![Malla de  500 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/malla500.png)

## Modelo Gn,m de Erdös y Rényi

Crear n nodos y elegir uniformemente al azar m distintos pares de distintos vértices.

def grafoErdosRenyi(n, m, dirigido=False):
  """
  Genera grafo aleatorio con el modelo Erdos-Renyi
  :param n: número de nodos (> 0)
  :param m: número de aristas (>= n-1)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """

Con 30 nodos: 
![Erdos de  30 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/erdos30.png)

Con 100 nodos: 
![Erdos de  100 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/erdos100.png)

Con 500 nodos: 
![Erdos de  500 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/erdos500.png)

## Modelo Gn,p de Gilbert

Crear n nodos y poner una arista entre cada par independiente y uniformemente con probabilidad p.

def grafoGilbert(n, p, dirigido=False):
 """
  Genera grafo aleatorio con el modelo Gilbert
  :param n: número de nodos (> 0)
  :param p: probabilidad de crear una arista (0, 1)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """

Con 30 nodos: 
![Gilbert de  30 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/gilbet30.png)

Con 100 nodos: 
![Gilbert de  100 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/gilbet100.png)

Con 500 nodos: 
![Gilbert de  500 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/gilbet500.png)

## Modelo Gn,r geográfico simple.

Colocar n nodos en un rectángulo unitario con coordenadas uniformes (o normales) y colocar una arista entre cada par que queda en distancia r o menor.

def grafoGeografico(n, r, dirigido=False):
  """
  Genera grafo aleatorio con el modelo geográfico simple
  :param n: número de nodos (> 0)
  :param r: distancia máxima para crear un nodo (0, 1)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """

Con 30 nodos: 
![Geografico de  30 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/geo30.png)

Con 100 nodos: 
![Geografico de  100 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/geo100.png)

Con 500 nodos: 
![Geografico de  500 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/geo500.png)

## Variante del modelo Gn,d Barabási-Albert.

Colocar n nodos uno por uno, asignando a cada uno d aristas a vértices distintos de tal manera que la probabilidad de que el vértice nuevo se conecte a un vértice existente v es proporcional a la cantidad de aristas que v tiene actualmente - los primeros d vértices se conecta todos a todos.

def grafoBarabasiAlbert(n, d, dirigido=False):
  """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (> 0)
  :param d: grado máximo esperado por cada nodo (> 1)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """

Con 30 nodos: 
![Barabási de  30 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/barabasi30.png)

Con 100 nodos: 
![Barabási de  100 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/barabasi100.png)

Con 500 nodos: 
![Barabási de  500 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/barabasi500.png)


## Modelo Gn Dorogovtsev-Mendes.

Crear 3 nodos y 3 aristas formando un triángulo. Después, para cada nodo adicional, se selecciona una arista al azar y se crean aristas entre el nodo nuevo y los extremos de la arista seleccionada.

def grafoDorogovtsevMendes(n, dirigido=False):
  """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (≥ 3)
  :param dirigido: el grafo es dirigido?
  :return: grafo generado
  """

Con 30 nodos: 
![Dorogov-Mendes de  30 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/dorogovMend30.png)

Con 100 nodos: 
![Dorogov-Mendes de  100 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/dorogovMend100.png)

Con 500 nodos: 
![Dorogov-Mendes de  500 nodos](https://github.com/GusRojas/ProyetoGrafosDAA_A24/blob/main/Imagenes/dorogovMend500.png)

