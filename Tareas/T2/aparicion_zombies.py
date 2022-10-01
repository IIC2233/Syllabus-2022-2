import math

'''
Para la corrección de esta tarea, se considerará el archivo original, entregado en el syllabus
'''

def intervalo_aparicion(ronda: int, ponderador: int) -> float:
    y_min = 0.1
    height = 0.7 * ponderador # el valor y maximo sera (y_min + height)
    decay_factor = 0.0273 # mientras mas grande mas rapido decae el valor y por ende con menos rondas el intervalo se acercara al minimo
    return y_min + (height * (math.e ** (-(ronda ** 2) * decay_factor)))

'''
Si vas a editar los valores de la funcion anterior con fines de debuggeo y quieres ver como
se comporta, puedes ejecutar este archivo, se mostrará un gráfico hasta de hasta 15 rondas.
Para poder ejecutarlo debes tener instaladas las librerias matplotlib y numpy usando los comandos
pip install matplotlib
pip install numpy
'''

if __name__ == '__main__':
    import time
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("No tienes instalada una alguna de las librerias.\nPara instalarlas ejecuta los siguientes comandos:")
        print("pip install matplotlib")
        print("pip install numpy")
        time.sleep(3)
        quit()
        
    max_rounds = 15
    x_values = np.arange(0, max_rounds, 1)
    ponderador = 1 # este valor seria de parametros.py
    plt.plot(x_values, intervalo_aparicion(x_values, ponderador))
    plt.plot(x_values, intervalo_aparicion(x_values, ponderador), ".")
    plt.xlabel("Rondas")
    plt.ylabel("Intervalo de aparicion en segundos")
    plt.show()