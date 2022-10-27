import time
import random
import parametros as p

class Casa:

    def __init__(self, id, id_padre, distancia, nivel_decoracion, posicion):
        '''
        Inicializa el nodo de el grafo condominio
        '''
        self.id = id
        self.id_padre = id_padre    
        self.decoracion = nivel_decoracion
        self.distancia = distancia
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.posicion = posicion

    def actualizar_cola(self, protagonista)->None:
        '''
        genera la actualización de la cola al momento de correr el codigo
        '''
        
        atendido = None
        while atendido != protagonista:
            time.sleep(p.TIEMPO)
            if random.random() > p.PROB_COLARSE:
                self.cola_dulces.tot_se_cola()
                print("Se logró colar alguien")
            
            time.sleep(p.TIEMPO)
            atendido = self.cola_dulces.atender_tot()
            print("La cola ha avanzado un puesto. Tu posición es de")
        print("Has conseguido sacar los mejores dulces!")
    
    def __str__(self)-> str:
        '''retorna el id de la casa'''
        return str(self.id)


class Condominio:
    """
    Representa el arbol binario del condominio,
    donde cada instancia de Casa corresponde a los nodos
    """

    def __init__(self, dict_casas) -> None:
        
        self.casa_protagonista = None #Raiz
        self.dict_casas = dict_casas 
        self.poblado = False
        self.dict_casas_final = dict() 
        self.protagonista = False

    def identificar_protagonista(self):
        """"

        Identificamos al protagonita, quien tendrá id = 0, 
        inicializamos su instancia de casa y la guardamos en self.casa_protagonista. 
        Una vez identificado, self.protagonista = True.

        """

        for id in self.dict_casas.keys():
            if id == 0:
                att = self.dict_casas[id]
                protagonista = Casa(id, *att)
                self.casa_protagonista = protagonista
                self.protagonista = True

    
    def poblar_condominio(self):
        """"

        El protagonista ya debe haber sido identificado para usar poblar_condominio().
        Hacemos la inicializacion de cada casa, con sus respectivos hijos. Para ello utilizamos 
        lista_padre, con ella identificamos que casas nos faltan por inicializar y el diccionario 
        self.dict_casas para tener la informacion para inicializacion.

        """


        if self.protagonista:
            lista_padre = [[self.casa_protagonista.id, self.casa_protagonista]]
            self.dict_casas_final[self.casa_protagonista.id] = self.casa_protagonista

            while len(lista_padre) > 0:
                padre = lista_padre.pop(0)
                id_padre = padre[0]
                nodo_padre = padre[1]
                for id, att in self.dict_casas.items():
                    if att[0] == id_padre:
                        nodo_casa = Casa(id, *att)
                        self.asignar_ubicacion(nodo_padre, nodo_casa)
                        agregar = [id, nodo_casa]
                        lista_padre.append(agregar)
                        self.dict_casas_final[id] = nodo_casa
            
            self.poblado = True
        
        else:
            print("Primero debes identificar al protagonista!")

    def asignar_ubicacion(self, nodo_padre, nodo_hijo):
        """"

        Dependiendo la posicion del nodo hijo, se le guarda en la instancia de 
        nodo_padre, como hijo derecho o hijo izquierdo.

        """

        if nodo_hijo.posicion == 0: 
            nodo_padre.hijo_izquierdo = nodo_hijo #Si es 0 es hijo izquierdo

        elif nodo_hijo.posicion == 1:                  
            nodo_padre.hijo_derecho = nodo_hijo #Si es 1 es hijo derecho


    def mostrar_arbol(self):
        """"
        
        El árbol ya debe estar poblado para utilizar mostrar_arbol().
        Un nodo podrá o tener los uno, dos o ningún hijo. Para mostrar el árbol, deberás fijarte 
        que sus nodos hijos sean distintos de None.
       
        """

        if self.poblado == True:
            cantidad_casas = len(self.dict_casas_final)
            for x in range(0, cantidad_casas):
                for id, casa in self.dict_casas_final.items():
                    if id == x and casa.hijo_derecho != None and casa.hijo_izquierdo == None:

                        print(f"Casa de id:{casa.id} --> hijo derecho Casa de id:{casa.hijo_derecho.id}")
                    
                    elif id == x and casa.hijo_derecho == None and casa.hijo_izquierdo != None:
                        
                        print(f"Casa de id:{casa.id} --> hijo izquierdo Casa de id:"\
                            f"{casa.hijo_izquierdo.id}")

                    elif id == x and casa.hijo_derecho != None and casa.hijo_izquierdo != None:
                        
                        print(f"Casa de id:{casa.id} --> hijo izquierdo Casa de id:"\
                            f"{casa.hijo_izquierdo.id} --> hijo derecho Casa de id:{casa.hijo_derecho.id}")

        else:
            print("Primero debes poblar el grafo!")

