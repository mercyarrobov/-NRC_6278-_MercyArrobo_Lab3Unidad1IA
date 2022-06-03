#Importar Queue
from queue import Queue

class Grafo:  
    
    """
    Una clase para representar a un grafo

    ...

    Atributos
    ----------
    m_num_de_nodos : int
        número de nodos
    m_nodos : int
        rango de nodos
    m_directo : boolean
        directo o no directo 
    m_list_ady : mutable
        Defino el diccionario para implementar la lista adyacencia

    Métodos
    -------
    agregar_aristas(self, nodo1, nodo2, peso=1):
        Añadir aristas al grafo
    imprimir_lista_de_ady(self):
        Imprime la representación del grafo
    dfs(self, comienzo, objetivo, camino=[], nodo_visitado=set()):
        Método recursivo para implementar dfs.
    """
    
    def __init__(self, numeros_de_nodos, directo=True):
        
        '''
        Constructor inicializador de la clase grafo.

            Parameters:
                m_num_de_nodos : int
                    número de nodos
                m_nodos : int
                    rango de nodos
                m_directo : boolean
                    directo o no directo 
                m_list_ady : mutable
                    Defino el diccionario para implementar la lista adyacencia
        '''
    #Número de aristas
        self.m_num_of_nodes = numeros_de_nodos   
        #Inicializa el rango de los nodos
        self.m_nodos = range(self.m_num_of_nodes)
        #Definir el tipo de un grafo dirigido o no dirigido
        self.m_directo = directo 
        # Lista de adyacencia usando diccionario
        self.m_lista_ady = {nodo: set() for nodo in self.m_nodos}
        	
    def agregar_aristas(self, nodo1, nodo2, peso=1):
        
        """
        Función que agrega una arista al grafo

        Parámetros
        ----------
        nodo1 : int
            nodo de partida
        nodo2 : int
            nodo de llegada
        peso : int
            peso del nodo
            
        """
        #Añade la arista del nodo1 al nodo2"""
        self.m_lista_ady[nodo1].add((nodo2, peso))

        #Si un grafo es no dirigido, añade la misma arista
        if not self.m_directo:
            #Pero también en la dirección opuesta
            self.m_lista_ady[nodo2].add((nodo1, peso))
            
    def imprimir_lista_de_ady(self):
        """ Función que imprimir la representación del grafo
        """
         #Agrega clave y recorre las listas adyacentes
        for key in self.m_lista_ady.keys():
             #Imprimi la lista de nodos con su clave
            print("nodo:    ", key, ": ", self.m_lista_ady[key])
            
    def dfs(self, inicio, objetivo, camino=[], nodo_visitado=set()):
        
        """
        Método recursivo para encontrar el camino más corto desde un nodo de inicio hasta un nodo de destino.

        Parámetros
        ----------
        comienzo : int
            nodo de partida
        objetivo : int
            nodo de llegada
        peso : int
            peso del nodo
        
        retorna: El nodo que contiene el valor de destino o null si no existe.
            
        """
        #Agregar nuevos elementos a la lista.
        camino.append(inicio)
        #Marcamos como visitado agregándolo a un conjunto de nodos visitados
        nodo_visitado.add(inicio)
        # Si el inicio es igual al objetivo
        if inicio == objetivo:
            # retorna a inicio
            return camino

        # Recorrer todas las ramas vecinas que no son visitadas de la lista adyacencia
        for (nodos_no_visitados, peso) in self.m_lista_ady[inicio]:

            #comprobar si un nodo no visitado no está en la lista
            if nodos_no_visitados not in nodo_visitado:
                # Guardamos una referencia al resultado si un elemento no está presente en una lista.
                resultado = self.dfs(nodos_no_visitados,
                                     objetivo, camino, nodo_visitado)
                # Se envia a los nodos no visitado, objetivo, camino y nodo visitado.
                if resultado is not None:  # Si la llamada recursiva no regresa, eso significa que hemos encontrado nuestro nodo objetivo
                    #Devolvemos la ruta transversal como resultado
                    return resultado
                
        #Eliminamos el nodo actual de la ruta 
        camino.pop()
        #Regresamos como resultado
        return None
    #main del programa
if __name__ == "__main__":
    
    #PRUEBA 1
    print("Grafo 1")
    #Se crea o instancia el grafo con 5 nodos y no dirigido
    print("Agregando aristas al grafo")
    #Agregar las aristas
    grafo1= Grafo(5, directo=False)  
    
    # Agregar al grafo las aristas con un peso
    
    grafo1.agregar_aristas(0, 1)
    grafo1.agregar_aristas(0, 2)
    grafo1.agregar_aristas(0, 4)
    grafo1.agregar_aristas(1, 4)
    grafo1.agregar_aristas(1, 3)

    
    #Almacenamiento interno del grafo a la clase
    grafo1.imprimir_lista_de_ady() #Imprime las lista de adyacencia del nodo con su nodo y peso
    #Se almacena en una lista el camino transversal
    camino_transversal = [] 
    # Ruta para hallar desde el nodo 0 al nodo 3
    camino_transversal = grafo1.dfs(0, 3) 
    print(f" El camino transversal del nodo 0 al nodo 3 es:{camino_transversal}" )
   
    
    #PRUEBA 2
    print("\n\nGrafo 2")
    #Se crea o instancia el grafo con 7 nodos y no dirigido
    print("Agregando aristas al grafo")
    #Agregar las aristas
    grafo2= Grafo(7, directo=False)  
    
    # Agregar al grafo las aristas con un peso
    
    grafo2.agregar_aristas(0, 1)
    grafo2.agregar_aristas(0, 2)
    grafo2.agregar_aristas(1, 4)
    grafo2.agregar_aristas(4, 5)
    grafo2.agregar_aristas(1, 3)
    grafo2.agregar_aristas(2, 6)
    
     #Almacenamiento interno del grafo a la clase
    grafo2.imprimir_lista_de_ady() #Imprime las lista de adyacencia del nodo con su nodo y peso
    #Se almacena en una lista el camino transversal
    camino_transversal = [] 
    # Ruta para hallar desde el nodo 0 al nodo 3
    camino_transversal = grafo2.dfs(0, 4) 
    print(f" El camino transversal del nodo 0 al nodo 4 es:{camino_transversal}" )
    
    
    #PRUEBA 3
    print("\n\nGrafo 3")
    #Se crea o instancia el grafo con 5 nodos y no dirigido
    print("Agregando aristas al grafo")
    #Agregar las aristas
    grafo3= Grafo(5, directo=False)  
    
    # Agregar al grafo las aristas con un peso
    
    grafo3.agregar_aristas(0, 1)
    grafo3.agregar_aristas(1, 2)
    grafo3.agregar_aristas(0, 3)
    grafo3.agregar_aristas(0, 2)
    grafo3.agregar_aristas(2, 4)
    
    #Almacenamiento interno del grafo a la clase
    grafo3.imprimir_lista_de_ady() #Imprime las lista de adyacencia del nodo con su nodo y peso
    #Se almacena en una lista el camino transversal
    camino_transversal = [] 
    # Ruta para hallar desde el nodo 0 al nodo 3
    camino_transversal = grafo3.dfs(0, 3) 
    print(f" El camino transversal del nodo 0 al nodo 3 es:{camino_transversal}" )