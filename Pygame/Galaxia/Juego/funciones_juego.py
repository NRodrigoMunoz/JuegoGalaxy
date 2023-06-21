import pygame
import sqlite3
def crear_enemigos(enemigo_fila,enemigo_columna,clases,distancia_fila,enemigos_grupos):
    """
    Utilizamos 2 for para iterar las filas y el otro las columnas
    por cada fila crea 5 enemigos y les paso los parametros de x e y
    para su ubicación
    """
    for fila in range(enemigo_fila):
        for columna in range(enemigo_columna):
            """
            Explicacion del parametro: 100 es la posicion de cada enemigo en (X)
            sumado a la columna y eso lo multiplicas por 100 para distanciar los enemigos
            segundo parametro 300 la ubicacion en (Y) lo sumas a la fila y multiplicas por 70
            para distanciar las filas mientras el valor sea mas elevado de la multiplicacion
            mas se aleja de lo contrario se juntan. 
            """
            enemigo = clases(100 + columna *100, distancia_fila + fila * 70)
            enemigos_grupos.add(enemigo)
            
def muestra_texto(pantalla,fuente,texto,color, dimensiones, x, y):
	tipo_letra = pygame.font.Font(fuente,dimensiones)
	superficie = tipo_letra.render(texto,True, color)
	rectangulo = superficie.get_rect()
	rectangulo.center = (x, y)
	pantalla.blit(superficie,rectangulo)
 
def crear_puntajes(nombre,puntuacion):
    with sqlite3.connect("bd_puntaje.db") as conexion:
                try:
                    sentencia = ''' create  table personajes
                    (
                    id integer primary key autoincrement,
                    nombre text,
                    puntaje real
                    )
                    '''
                    conexion.execute(sentencia)
                    print("Se creo la tabla personajes")                       
                except sqlite3.OperationalError:
                    print("La tabla personajes ya existe")

                #INSERT:

                try:
                    conexion.execute("insert into personajes(nombre,puntaje) values (?,?\n)", (nombre,puntuacion))
                    conexion.commit()# Actualiza los datos realmente en la tabla
                except:
                    print("Error")
