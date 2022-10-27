import parametros as p
from collections import deque
from condominio import Casa
class ProtagonistaDisfrazado: 

    def __init__(self, nombre):
        self.nombre = nombre
    
    def recuperar_casas_DFS_recursivo(self, casa_actual:Casa, distancia_actual:int = 0)->list:
        ''' añade a una lista diccionarios de la forma {"casa": Casa , "distancia":int} 
        recorriendo el grafo con el algoritmo DFS de forma recursiva para finalmente
        retornaresta lista creada [dic,dic,...,dic]'''
        #COMPLETAR
        pass
    
    def recuperar_casas_DFS_iterativo(self, casa_inicial: Casa )->list:
        ''' añade a una lista diccionarios de la forma {"casa": Casa , "distancia":int} 
        recorriendo el grafo con el algoritmo DFS de forma iterativa para finalmente
        retornar esta lista creada [dic,dic,...,dic]'''
        #COMPLETAR
        pass

    def recuperar_casas_BFS_iterativo(self, casa_inicial: Casa)-> list:
        ''' añade a una lista diccionarios de la forma {"casa": Casa , "distancia":int} 
        recorriendo el grafo con el algoritmo BFS de forma iterativa para finalmente
        retornaresta lista creada [dic,dic,...,dic]'''
        #COMPLETAR
        pass

    def filtrar_casas(self, listado_casas:list)->list:
        '''filtra la lista de casas manteniendo solo aquellas que posean la decoración deseada,
        calcula un puntaje para cada una añadiendolas a una nueva lista como una tupla de la forma
        (Casa, puntaje) para finalmente retornar la mejor casa'''
        posibles_candidatos = []
        for dic_casa in listado_casas:
            if dic_casa["casa"].decoracion >= p.EXPECTATIVAS_DECORACION:
                puntaje = p.PONDERADOR_DECORACION*dic_casa["casa"].decoracion -\
                p.PONDERADOR_DISTANCIA*dic_casa["distancia"]
                posibles_candidatos.append((dic_casa["casa"], puntaje))
        mejor_casa = self.elegir_mejor_casa(posibles_candidatos)
        return mejor_casa
        
    def elegir_mejor_casa(self, lista_casas:list)->Casa:
        '''selecciona la casa con mayor puntaje entre la lista y la retorna'''
        puntaje_max, casa_escogida = 0, None
        for casa, puntaje in lista_casas:
            if puntaje > puntaje_max:
                casa_escogida,puntaje_max = casa,puntaje
    
        return casa_escogida    