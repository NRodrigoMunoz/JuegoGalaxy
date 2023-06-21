from funciones_juego import *
from contantes import *
from pygame.locals import *
from personajes import *
import pygame
import random
#*******************************************FUENTE E IMAGENES******************************
texto = pygame.font.match_font("consolas")
imagen1 = pygame.image.load("Pygame\Galaxia\Imagenes\Enemigo1.png")
imagen2 = pygame.image.load("Pygame\Galaxia\Imagenes\Enemigo2.png")
imagen3 = pygame.image.load("Pygame\Galaxia\Imagenes\Enemigo3.png")
vida = pygame.image.load("Pygame\Galaxia\Imagenes\Jugador.png")
muerte = pygame.image.load("Pygame\Galaxia\Imagenes\Muerte.png")
#*******************************************SONIDO AMBIENTE*********************************
pygame.mixer.init()
ambiente = pygame.mixer.Sound("Pygame\Galaxia\Sonidos\musicajuego.mp3")
ambiente.set_volume(0.5)
ambiente.play(-1)
#***************************************PANTALLA********************************************
pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
fondo_juego = pygame.image.load("Pygame\Galaxia\Imagenes\GalaxiaFondo.jpg")
intro_juego = pygame.image.load("Pygame\Galaxia\Imagenes\PantallaInicio.jpg")
final_juego = pygame.image.load("Pygame\Galaxia\Imagenes\GalaxiaFondo.jpg")
reloj = pygame.time.Clock()
X = 0
Y = 0
#*************************ICONOS Y TITULO DEL JUEGO*****************************************
icono = pygame.image.load("Pygame\Galaxia\Imagenes\icono.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("GalaxyDeluxe")
#*******************************TIEMPO TRANSCURRIDO*****************************************
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)
fuente_básica = pygame.font.Font(None,40)
user_text = ""
input_rect = pygame.Rect(300,350,200,40)
color_txt = pygame.Color("lightskyblue3")
#*******************************INICIO DEL JUEGO********************************************
repetir = True
flag_intro = True
while repetir:
    crear_enemigos(4,5,Enemigos,300,enemigos_grupo1)#400 puntos total 20 c/u
    crear_enemigos(1,5,EnemigosDos,200,enemigos_grupo2)#300 puntos total 60 c/u
    crear_enemigos(1,5,EnemigosTres,100,enemigos_grupo3)#500 puntos total 100 c/u
    jugador = Jugador()
    sprites.add(jugador)
    while flag_intro:
        reloj.tick(FPS)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                quit()
            if evento.type == pygame.KEYDOWN:
                if len(user_text)<=9:
                    if evento.key == pygame.K_BACKSPACE:
                            user_text = user_text[0:-1]
                    else:
                        user_text += evento.unicode
                elif evento.key == pygame.K_BACKSPACE and len(user_text)>=9:
                        user_text = user_text[0:-1]
        tecla = pygame.key.get_pressed()
        if tecla [pygame.K_9]:
            flag_intro = False
            flag_final = False
            flag_jugar = True
            user_text = user_text[0:-1]
        if tecla [pygame.K_0] and PRIMER_LUGAR == True:
            flag_intro = False
            flag_jugar = False
            flag_final = True
            user_text = user_text[0:-1]
        if tecla [pygame.K_0] and PRIMER_LUGAR == False:
            user_text = user_text[0:-1]
            pass
        text_surface = fuente_básica.render(user_text,True,COLOR_TEXTO)
        pantalla.blit(intro_juego,FONDO_JUEGO)
        pantalla.blit(text_surface,(input_rect.x+5,input_rect.y+10))
        pygame.draw.rect(pantalla,color_txt,input_rect,2)
        pygame.display.update()

    while flag_jugar:
        PRIMER_LUGAR = True
        reloj.tick(FPS)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                quit()
            if evento.type == pygame.USEREVENT:   
                if evento.type == timer_segundos:
                    MINUTOS -= RESTA_POR_SEGUNDO
                    if MINUTOS == 1.0099999999999996:
                         MINUTOS = 0.60
                    if MINUTOS <= 0:
                        jugador.vidas = 3
                        jugador.puntos_de_vida = 100
                        flag_jugar = False
                        flag_final = True
                        resultado = crear_puntajes(user_text.capitalize(),puntuacion)
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_SPACE]:
            """
            Calculamos el tiempo de disparo obteniendo el tiempo actual de disparo
            menos el tiempo almacenado en  ultimo disparo y si es mayor que cadencia
            osea mayor a 750 milisegundos dispara de nuevo  despues de cumplirse la condicion
            ultimo disparo obtiene el tiempo de ahora 
            """
            ahora = pygame.time.get_ticks()
            if ahora - jugador.ultimo_disparo > jugador.cadencia:
                jugador.disparo()
                jugador.ultimo_disparo = ahora
                sonido_disparo = pygame.mixer.Sound("Pygame\Galaxia\Sonidos\misil.mp3")
                sonido_disparo.set_volume(VOLUMEN_JUEGO)
                sonido_disparo.play()
    #*****************************DISPARO DE LOS ENEMIGOS****************************************
        tiempo_ahora = pygame.time.get_ticks()
        tiempo_ahora_dos = pygame.time.get_ticks()
        tiempo_ahora_tres = pygame.time.get_ticks()

        """
        Adiquirimos el tiempo de disparo actual lo restamos al ultimo disparo y que eso sea
        mayor a tiempo de disparo que los enemigos que disparen sean menor a 7 
        el ataque_enemigo elije de forma aleatoria el que ataca 
        centramos el disparo enemigo y add a enemigos misiles los disparos 
        por ultimo igualamos el ultimo disparo enemigo a tiempo_ahora
        """
        if (tiempo_ahora - ULTIMO_DISPARO_ENEMIGO > TIEMPO_DISPARO_ENEMIGO 
            and len(enemigos_misiles) < 10 and len(enemigos_grupo1) > 0):
            ataque_enemigo = random.choice(enemigos_grupo1.sprites())
            disparo_enemigo = DisparosEnemigo(ataque_enemigo.rect.centerx,ataque_enemigo.rect.bottom)
            enemigos_misiles.add(disparo_enemigo)
            ULTIMO_DISPARO_ENEMIGO = tiempo_ahora
        
        if (tiempo_ahora_dos - ULTIMO_DISPARO_ENEMIGO_DOS > TIEMPO_DISPARO_ENEMIGO_DOS 
            and len(enemigos_misiles) < 10 and len(enemigos_grupo2) > 0):
            ataque_enemigo_dos = random.choice(enemigos_grupo2.sprites())
            disparo_enemigo_dos = DisparosEnemigo(ataque_enemigo_dos.rect.centerx,ataque_enemigo_dos.rect.bottom)
            enemigos_misiles.add(disparo_enemigo_dos)
            ULTIMO_DISPARO_ENEMIGO_DOS = tiempo_ahora_dos
        
        if (tiempo_ahora_tres - ULTIMO_DISPARO_ENEMIGO_TRES > TIEMPO_DISPARO_ENEMIGO_TRES 
            and len(enemigos_misiles) < 10 and len(enemigos_grupo3) > 0):
            ataque_enemigo_tres = random.choice(enemigos_grupo3.sprites())
            disparo_enemigo_tres = DisparosEnemigo(ataque_enemigo_tres.rect.centerx,ataque_enemigo_tres.rect.bottom)
            enemigos_misiles.add(disparo_enemigo_tres)
            ULTIMO_DISPARO_ENEMIGO_TRES = tiempo_ahora_tres
    #*******************************************MOVIMIENTO PANTALLA VERTICAL***********************************
        """
        Los valores de x e y son 0 
        y_relativo es igual a y % fondo para que me devuelva el resto de la altura
        lo muentro en la pantalla con x valor en 0 para que horizontalmente este fija
        y en valor de y de forma vertical me reste y_relativa con el rectangulo de la altura
        del fondo del juego en cada vuelta del while a y le sumo 2 es el movimiento del fondo
        y para que entre en bucle y_relativa tiene que ser menor al alto de la pantalla osea 800
        
        """
        y_relativa = Y % fondo_juego.get_rect().height
        pantalla.blit(fondo_juego,(X,y_relativa-fondo_juego.get_rect().height))
        Y += 2
        if y_relativa < ALTO:
            pantalla.blit(fondo_juego,(X,y_relativa))
    #*******************************************ACTUALIZACION DE SPRITES****************************************
        sprites.update()
        enemigos_grupo1.update()
        enemigos_grupo2.update()
        enemigos_grupo3.update()
        misiles.update()
        enemigos_misiles.update()
        explosiones_grupo.update()
    #*******************************************COLISIONES******************************************************
        colision = pygame.sprite.spritecollide(jugador,enemigos_misiles,False,pygame.sprite.collide_circle)
        BANDERA_COLISION = True
        if colision:
            sonido_explosion = pygame.mixer.Sound("Pygame\Galaxia\Sonidos\ExplosionAvion.mp3")
            sonido_explosion.set_volume(VOLUMEN_JUEGO)
            sonido_explosion.play()
            explosion = Explosion(jugador.rect.center)
            explosiones_grupo.add(explosion)
            jugador.puntos_de_vida -= 100
            if puntuacion >= 0 and BANDERA_COLISION == True:
                puntuacion += -200
                BANDERA_COLISION = False
                if puntuacion < 0 and BANDERA_COLISION == False:
                    puntuacion = 0  
        
        pantalla.blit(vida,POSICION_VIDA_MUERTE_UNO)
        pantalla.blit(vida,POSICION_VIDA_MUERTE_DOS)
        pantalla.blit(vida,POSICION_VIDA_MUERTE_TRES)
        
        if jugador.puntos_de_vida <= 0 and jugador.vidas == 3:
            jugador.kill()
            enemigos_misiles.empty()
            misiles.empty()
            jugador = Jugador()
            sprites.add(jugador)
            jugador.vidas = 2
            
        if jugador.vidas == 2:
            if jugador.puntos_de_vida <= 0:
                jugador.kill()
                enemigos_misiles.empty()
                misiles.empty()
                jugador = Jugador()
                sprites.add(jugador)
                jugador.vidas = 1
            pantalla.blit(muerte,POSICION_VIDA_MUERTE_UNO)
        
        if jugador.vidas == 1:
            pantalla.blit(muerte,POSICION_VIDA_MUERTE_UNO)
            pantalla.blit(muerte,POSICION_VIDA_MUERTE_DOS)
            if jugador.puntos_de_vida <= 0:
                jugador.vidas = 3
                jugador.puntos_de_vida = 100
                flag_jugar = False
                flag_final = True
                resultado = crear_puntajes(user_text.capitalize(),puntuacion)
                
        colision_uno = pygame.sprite.groupcollide(misiles,enemigos_grupo1,True,True,pygame.sprite.collide_circle)
        if colision_uno:
            for colision in colision_uno:
                explosion = Explosion(colision.rect.center)
                explosiones_grupo.add(explosion)
                sonido_explosion = pygame.mixer.Sound("Pygame\Galaxia\Sonidos\ExplosionAvion.mp3")
                sonido_explosion.set_volume(VOLUMEN_JUEGO)
                sonido_explosion.play()
                if puntuacion >= 0:
                    puntuacion += 20
                    if puntuacion < 0:
                        puntuacion = 0
                    
        colision_dos = pygame.sprite.groupcollide(enemigos_grupo2,misiles,True,True,pygame.sprite.collide_circle)
        if colision_dos:
            for colision in colision_dos:
                explosion = Explosion(colision.rect.center)
                explosiones_grupo.add(explosion)
                sonido_explosion = pygame.mixer.Sound("Pygame\Galaxia\Sonidos\ExplosionAvion.mp3")
                sonido_explosion.set_volume(VOLUMEN_JUEGO)
                sonido_explosion.play()
                if puntuacion >= 0:
                    puntuacion += 60
                    if puntuacion < 0:
                        puntuacion = 0 
                    
        colision_tres = pygame.sprite.groupcollide(enemigos_grupo3,misiles,True,True,pygame.sprite.collide_circle)
        if colision_tres:
            for colision in colision_tres:
                explosion = Explosion(colision.rect.center)
                explosiones_grupo.add(explosion)
                sonido_explosion = pygame.mixer.Sound("Pygame\Galaxia\Sonidos\ExplosionAvion.mp3")
                sonido_explosion.set_volume(VOLUMEN_JUEGO)
                sonido_explosion.play()
                if puntuacion >= 0:
                    puntuacion += 100
                    if puntuacion < 0:
                        puntuacion = 0
        if len(enemigos_grupo1) <= 0 and len(enemigos_grupo2) <= 0 and len(enemigos_grupo3) <= 0:
            if jugador.vidas == 3 and BANDERA_VIDA == True:
                puntuacion += 1000
                puntuacion += (MINUTOS*1000.0)
                BANDERA_VIDA = False
                jugador.vidas = 3
                jugador.puntos_de_vida = 100
            if jugador.vidas == 2 and BANDERA_VIDA == True:
                puntuacion += 700
                puntuacion += (MINUTOS*1000.0)
                BANDERA_VIDA = False
                jugador.vidas = 3
                jugador.puntos_de_vida = 100
            if jugador.vidas == 1 and BANDERA_VIDA == True:
                puntuacion += 300
                puntuacion += (MINUTOS*1000.0)
                BANDERA_VIDA = False
                jugador.vidas = 3
                jugador.puntos_de_vida = 100
            flag_jugar = False 
            flag_final = True
            resultado = crear_puntajes(user_text.capitalize(),puntuacion)
    #*******************************************DIBUJAMOS EN LA PANTALLA LOS GRUPOS*****************************
        sprites.draw(pantalla)
        misiles.draw(pantalla)
        enemigos_misiles.draw(pantalla) 
        enemigos_grupo1.draw(pantalla)
        enemigos_grupo2.draw(pantalla)
        enemigos_grupo3.draw(pantalla)
        explosiones_grupo.draw(pantalla)
    #*******************************************TEXTO Y IMAGENES************************************************
        muestra_texto(pantalla,texto,str(f"{MINUTOS:.3} Minutos",),COLOR_TEXTO,20,70,30)
        muestra_texto(pantalla,texto,str(puntuacion).zfill(7),COLOR_TEXTO,40,POSICION_X_MOSTRAR_TEXTO,120)
        muestra_texto(pantalla,texto,"PUNTAJE",COLOR_TEXTO,40,POSICION_X_MOSTRAR_TEXTO,80)
        muestra_texto(pantalla,texto,"X100",COLOR_TEXTO,25,POSICION_X_MOSTRAR_TEXTO,180)
        pantalla.blit(imagen3,(650,200))
        muestra_texto(pantalla,texto,"X60",COLOR_TEXTO,25,POSICION_X_MOSTRAR_TEXTO,290)
        pantalla.blit(imagen2,(670,310))
        muestra_texto(pantalla,texto,"X20",COLOR_TEXTO,25,POSICION_X_MOSTRAR_TEXTO,420)
        pantalla.blit(imagen1,(670,450))
        pygame.display.flip()
    
    while flag_final:
        reloj.tick(FPS)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                quit()
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_r]:
            repetir = True
            flag_final = False
            flag_intro = True
            flag_jugar = False
            MINUTOS = 1.60
            puntuacion = 0
            sprites.empty()
            enemigos_grupo1.empty()
            enemigos_grupo2.empty()
            enemigos_grupo3.empty()
            enemigos_misiles.empty()
            explosiones_grupo.empty()
            user_text = ""
            BANDERA_VIDA = True
        if tecla[pygame.K_RETURN]:
            quit()
        pantalla.blit(final_juego,FONDO_JUEGO)
        with sqlite3.connect("bd_puntaje.db") as conexion:
            cursor=conexion.execute("SELECT * FROM personajes ORDER BY puntaje DESC")
            for i,lista in enumerate(cursor):
                fuente_nombre = pygame.font.SysFont(texto,40)
                texto_nombre = fuente_nombre.render(str(lista[1]),True,COLOR_TEXTO)
                pantalla.blit(texto_nombre,(200,180+i*100))
                
                fuente_puntaje = pygame.font.SysFont(texto,40)
                texto_puntaje = fuente_nombre.render(str(lista[2]),True,COLOR_TEXTO)
                pantalla.blit(texto_puntaje,(550,180+i*100))
        
        muestra_texto(pantalla,texto,"PUNTAJE",COLOR_TEXTO,100,400,50)
        muestra_texto(pantalla,texto,"NOMBRE     PUNTAJE",COLOR_TEXTO,50,400,150)
        muestra_texto(pantalla,texto,"Presionar R para repetir juego o Enter para cerrar",COLOR_TEXTO,20,400,100)
        pygame.display.update()  
pygame.quit()
