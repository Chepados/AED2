from AmigosETSISI import AmigosETSISI
from Generator import Generator
from Persona import Persona
import networkx as nx
import matplotlib.pyplot as plt

contactos = []
number_contacts = 18
number_relations = 3
#gdor = Generator(number_contacts,number_relations)

contactos.append(Persona("Juan","123456", "Castellana"))
contactos.append(Persona("Jose","471953", "Gaztambide"))
contactos.append(Persona("Eva","967495", "Gran Vía"))
contactos.append(Persona("Alicia","174834", "Princesa"))
contactos.append(Persona("Ernesto","183598", "Gran Vía"))
contactos.append(Persona("Guillermo","479320", "Fuencarral"))
contactos.append(Persona("Alberto","357293", "La estrella de los goles"))
contactos.append(Persona("Lucas","120742", "Glorieta de mis huevos"))
contactos.append(Persona("Paula","118533","El patio"))
contactos.append(Persona("Clara","529258", "Castellana"))
contactos.append(Persona("Jacobo","276032", "Serrano"))
contactos.append(Persona("Pablo","192414", "Pozo del Tio Raimundo"))
contactos.append(Persona("Lucia","164363", "Paraíso"))
contactos.append(Persona("Perro","146246", "Mi casa"))
contactos.append(Persona("Jonny","934673", "Calculadora"))
contactos.append(Persona("Hector","167364", "Camion Rojo"))
contactos.append(Persona("Pedrito","436893", "Perdido"))
contactos.append(Persona("MILOCOFAV","249634", "Corazon"))

#contactos = gdor.get_list_of_contacts()
miRed = AmigosETSISI(number_contacts, contactos)
#gdor.insert_relations(miRed)


conexiones = [(0,1),(0,2),(1,2),(2,3),(4,5),(6,3),(8,1),(13,17),(16,2),(4,10),(3,14),(0,9),(8,15),(3,11),(9,10)]

for o,d in conexiones:
    miRed.insertaRelacion(o,d)

"""
miRed.insertaRelacion(0,1)
miRed.insertaRelacion(0,2)
miRed.insertaRelacion(2,3)
miRed.insertaRelacion(6,3)
miRed.insertaRelacion(4,5)
miRed.insertaRelacion(8,1)
miRed.insertaRelacion(1,2)
miRed.insertaRelacion(13,17)
miRed.insertaRelacion(16,2)
miRed.insertaRelacion(4,10)
miRed.insertaRelacion(3,14)
miRed.insertaRelacion(0,9)
miRed.insertaRelacion(8,15)
miRed.insertaRelacion(3,11)
miRed.insertaRelacion(2,3)
miRed.insertaRelacion(9,10)"""



diccionario = {k:v.getNombre() for k, v in zip(range(len(contactos)),contactos)}
print(diccionario)

G = nx.Graph()

for contacto in contactos:
    G.add_node(contacto.getNombre())

fig, ax = plt.subplots(figsize=(1,1))
nx.draw(G, with_labels=True, ax=ax)

for origen, destino in conexiones:
    G.add_edge(diccionario[origen],diccionario[destino])

print(f"Nodos del grafo: {G.nodes}")
print(f"Ejes del grafo: {G.edges}")






miRed.mostrarRed()

sep = "-"*100
print("Apartado 2.2.1. Número de grupos")
print(f"\nHay {miRed.contarGrupos()} grupos")
print(sep)
print("Apartado 2.2.2. Mostrar amigos directos")
print(miRed.mostrarAmigos("Jose"))
print(sep)
a = 10
b = 14
if miRed.sonDelMismoGrupo(contactos[a], contactos[b]):
    print(f"{contactos[a].getNombre()} es del mismo grupo que {contactos[b].getNombre()}")
else:
    print(f"{contactos[a].getNombre()} no es del mismo grupo que {contactos[b].getNombre()}")

print("Apartado 2.2.4. Mostrar amigos mismo Grupo de Amistad")

miRed.mostrarMiembrosGrupo(contactos[10])

