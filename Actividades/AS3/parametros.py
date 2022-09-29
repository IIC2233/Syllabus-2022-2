import os

# Teclas
TECLA_DERECHA = "a"
TECLA_IZQUIERDA = "d"
TECLA_CHEATCODE_KO = "k"

# Ventana juego
LIMITE_IZQUIERDA = 0
LIMITE_DERECHA = 800
LIMITE_ARRIBA = 161
LIMITE_ABAJO = 750
LIMITE_VIDA = 740

# Plataforma
ANCHO_PLATAFORMA = 181
ALTO_PLATAFORMA = 31
POS_INICIAL_X_PLATAFORMA = 310
POS_INICIAL_Y_PLATAFORMA = 650
VELOCIDAD_PLATAFORMA = 15

# Pelota
ANCHO_PELOTA = 41
ALTO_PELOTA = 41
POS_INICIAL_X_PELOTA = 380
POS_INICIAL_Y_PELOTA = 600
VELOCIDAD_PELOTA = [10, -10]
ACTUALIZAR_PELOTA = 50

# Bloques
ANCHO_BLOQUE = 156
ALTO_BLOQUE = 40
POS_INICIAL_X_BLOQUE = 10
POS_INICIAL_Y_BLOQUE = 170
NUM_BLOQUES = 25

# Rutas
# sprites
RUTA_LOGO = os.path.join('frontend', 'assets', 'sprites', 'logo.png')
RUTA_PELOTA = os.path.join('frontend', 'assets', 'sprites' 'pelota.png')
RUTA_GAMEOVER = os.path.join('frontend', 'assets', 'sprites', 'game_over.png')

# ui files
RUTA_UI_VENTANA_JUEGO = os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_juego.ui'
)
RUTA_UI_VENTANA_POSTJUEGO = os.path.join(
    'frontend', 'assets', 'ui files', 'ventana_postjuego.ui'
)

# Parámetros juego
PUNTAJE_INICIAL = 0
PUNTAJE_BLOQUE = 100
PUNTAJE_VIDA = 300
VIDAS = 3
TIEMPO_JUEGO = 90 * 1000  # en milisegundos
TIEMPO_RETRASO = 200
ACTUALIZAR_JUEGO = 10

# contraseñas prohibidas
CONTRASENAS_PROHIBIDAS = ['1234', 'contraseña', 'ladesiempre',
                          'porotos2001','calcomanía', 'blankibeibi',
                          'vivirana', '69420nice', 'micumpleaños',
                          'aguantela2020', 'HernanLover4ever', 'mec0m0un4oll4',
                          'pinguino2', 'b4d.bunny.b31b3']
