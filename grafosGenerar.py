from grafos_library import *

grafo_malla30 = grafoMalla(6,5)
grafo_malla30.guardar_grafo_graphviz("malla30.gv")
print("Grafo generado y guardado con éxito en malla30.gv")

grafo_malla30 = grafoMalla(10,10)
grafo_malla30.guardar_grafo_graphviz("malla100.gv")
print("Grafo generado y guardado con éxito en malla100.gv")

grafo_malla30 = grafoMalla(25,20)
grafo_malla30.guardar_grafo_graphviz("malla500.gv")
print("Grafo generado y guardado con éxito en malla500.gv")

grafo_erdos30 = grafoErdosRenyi(30,100)
grafo_erdos30.guardar_grafo_graphviz("erdos30.gv")
print("Grafo generado y guardado con éxito en erdos30.gv")

grafo_erdos100 = grafoErdosRenyi(100,350)
grafo_erdos100.guardar_grafo_graphviz("erdos100.gv")
print("Grafo generado y guardado con éxito en erdos100.gv")

grafo_erdos500 = grafoErdosRenyi(500,1800)
grafo_erdos500.guardar_grafo_graphviz("erdos500.gv")
print("Grafo generado y guardado con éxito en erdos500.gv")

grafo_gilbert30 = grafoGilbert(30,0.20)
grafo_gilbert30.guardar_grafo_graphviz("gilbert30.gv")
print("Grafo generado y guardado con éxito en gilbert30.gv")

grafo_gilbert100 = grafoGilbert(100,0.20)
grafo_gilbert100.guardar_grafo_graphviz("gilbert100.gv")
print("Grafo generado y guardado con éxito en gilbert100.gv")

grafo_gilbert500 = grafoGilbert(500,0.03)
grafo_gilbert500.guardar_grafo_graphviz("gilbert500.gv")
print("Grafo generado y guardado con éxito en gilbert500.gv")

grafo_geo30 = grafoGeografico(30,0.10)
grafo_geo30.guardar_grafo_graphviz("geo30.gv")
print("Grafo generado y guardado con éxito en geo30.gv")

grafo_geo100 = grafoGeografico(100,0.08)
grafo_geo100.guardar_grafo_graphviz("geo100.gv")
print("Grafo generado y guardado con éxito en geo100.gv")

grafo_geo500 = grafoGeografico(500,0.01)
grafo_geo500.guardar_grafo_graphviz("geo500.gv")
print("Grafo generado y guardado con éxito en geo500.gv")

grafo_barabasi30 = grafoBarabasiAlbert(30,2)
grafo_barabasi30.guardar_grafo_graphviz("barabasi30.gv")
print("Grafo generado y guardado con éxito en barabasi30.gv")

grafo_barabasi100 = grafoBarabasiAlbert(100,2)
grafo_barabasi100.guardar_grafo_graphviz("barabasi100.gv")
print("Grafo generado y guardado con éxito en barabasi100.gv")

grafo_barabasi500 = grafoBarabasiAlbert(500,2)
grafo_barabasi500.guardar_grafo_graphviz("barabasi500.gv")
print("Grafo generado y guardado con éxito en barabasi500.gv")

grafo_Dorogov30 = grafoDorogovtsevMendes(30)
grafo_Dorogov30.guardar_grafo_graphviz("dorogovMend30.gv")
print("Grafo generado y guardado con éxito en dorogovMend30.gv")

grafo_Dorogov100 = grafoDorogovtsevMendes(100)
grafo_Dorogov100.guardar_grafo_graphviz("dorogovMend100.gv")
print("Grafo generado y guardado con éxito en dorogovMend100.gv")

grafo_Dorogov500 = grafoDorogovtsevMendes(500)
grafo_Dorogov500.guardar_grafo_graphviz("dorogovMend500.gv")
print("Grafo generado y guardado con éxito en dorogovMend500.gv")