import os


# Rutas archivos
RUTA_USUARIOS = os.path.join("datos", "usuarios.csv")
RUTA_CANCIONES = os.path.join("datos", "canciones.csv")

# Rutas arte
RUTAS_ARTE = {
    "Pop": os.path.join("images", "indie.txt"),
    "Rock": os.path.join("images", "rock.txt"),
    "Kpop": os.path.join("images", "kpop.txt"),
    "Reggaeton": os.path.join("images", "metal.txt"),
    "Electronica": os.path.join("images", "pop.txt"),
    "Rap": os.path.join("images", "nueva_cancion.txt"),
    "Indie": os.path.join("images", "indie.txt")
}

# Categorias peliculas
CATEGORIAS = (
    "Pop",
    "Rock",
    "Kpop",
    "Reggaeton",
    "Electronica",
    "Rap",
    "Indie"
)

# Constantes adicionales
LARGO_LISTA_REPRODUCCION = 20
TIEMPO_REPRODUCCION = 0.3
