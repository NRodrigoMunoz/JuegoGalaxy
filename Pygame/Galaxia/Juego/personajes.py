import pygame
from contantes import *
#*******************************************CLASES******************************************
class Jugador(pygame.sprite.Sprite):
    #El jugador tiene herencia en el modulo sprite de pygame en concreto de la clase Sprite
    #Sprite del jugador
    def __init__(self,) -> None:
        #Heredamos el init de la clase Sprite de pygame
        super().__init__()
        self.image = pygame.image.load("Pygame\Galaxia\Imagenes\Jugador.png")
        self.image.set_colorkey(COLOR_NEGRO)
        self.rect = self.image.get_rect()
        self.radius = 6
        self.rect.center = POSICION_JUGADOR
        self.velocidad_x = 0
        self.cadencia = 750 
        self.ultimo_disparo = pygame.time.get_ticks()
        self.puntos_de_vida = 100
        self.vidas = 3
        
    def update(self) -> None:#Heredado de la clase Sprite
        self.velocidad_x = 0
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:
            self.velocidad_x = -5
        if teclas[pygame.K_d]:
            self.velocidad_x = 5
            
        self.rect.x += self.velocidad_x
           
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > 600:
            self.rect.right = 600
            
    def disparo(self):
        """
        Creamos el metodo disparos
        el segundo parametro indicamos que el misil se centra en medio del jugador
        y el tercer parametro la posicion de arriba colocamos un +20 pixeles
        para que se hacerque mas a la imagen de lo contrario se alejaria
        """
        misil = Disparos(self.rect.centerx, self.rect.top+20)
        misiles.add(misil)
   
class Enemigos(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.image.load("Pygame\Galaxia\Imagenes\Enemigo1.png")
        self.rect = self.image.get_rect()
        self.radius = 3
        self.rect.center = [x,y]
        self.contador_movimiento = 0
        self.velocidad_x = 1
        Disparos
        self.cadencia = 1000
        self.ultimo_disparo = pygame.time.get_ticks()
        
    def update(self) -> None:
        self.rect.x += self.velocidad_x
        self.contador_movimiento += 1
        """
        Colocamos el contador para que sume 1 en cada vuelta del bucle
        al llegar a 75 entra en la condicion y velocidad_x de ser 1 pasa a realizar 
        su movimiento en -1 el self contador se transforma en -76 sumando 1 cada interacion del bucle
        de 76 baja a 0 su posicion original asta 75 vuelve a entrar en la condicion velocidad_x pasa a tener un valor de 1
        y contador movimiento a tener un valor negativo de nuevo
        la funcion abs calcula el valor absoluto
        """
        if abs(self.contador_movimiento) > 75:
            self.velocidad_x *= -1
            self.contador_movimiento *= self.velocidad_x
          
    def disparo(self):
        misil = DisparosEnemigo(self.rect.centerx, self.rect.top+20)
        misiles.add(misil)
   
class EnemigosDos(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.image.load("Pygame\Galaxia\Imagenes\Enemigo2.png")
        self.rect = self.image.get_rect()
        self.radius = 4
        self.rect.center = [x,y]
        self.velocidad_x = 1
        self.contador_movimiento = 0
        Disparos
        self.cadencia = 800 
        self.ultimo_disparo = pygame.time.get_ticks()

    def update(self) -> None:
        self.rect.x += self.velocidad_x
        self.contador_movimiento += 1
        if abs(self.contador_movimiento) > 75:
            self.velocidad_x *= -1
            self.contador_movimiento *= self.velocidad_x
    
    def disparo(self):
        misil = DisparosEnemigo(self.rect.centerx, self.rect.top+20)
        misiles.add(misil)
            
class EnemigosTres(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.image.load("Pygame\Galaxia\Imagenes\Enemigo3.png")
        self.rect = self.image.get_rect()
        self.radius = 6
        self.rect.center = [x,y]
        self.velocidad_x = 1
        self.contador_movimiento = 0
        Disparos
        self.cadencia = 500
        self.ultimo_disparo = pygame.time.get_ticks()
        
    def update(self) -> None:
        self.rect.x += self.velocidad_x
        self.contador_movimiento += 1
        if abs(self.contador_movimiento) > 75:
            self.velocidad_x *= -1
            self.contador_movimiento *= self.velocidad_x
        

    def disparo(self):
        misil = DisparosEnemigo(self.rect.centerx, self.rect.top+20)
        misiles.add(misil)
    
class Disparos(pygame.sprite.Sprite):
    """
    Los parametros x e y es para indicar la posicion
    se carga la imagen en image con el set_colorkey se le quita el color de fondo
    obtenemos el rectangulo de la imagen con get_rect()
    se le indica la parte superior al rectangulo y se centra su posicion  
    """
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.image.load("Pygame\Galaxia\Imagenes\Misil.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self) -> None:
        """
        Obtenemos el rectangulo del misil y le colocamos la velocidad
        despues creamos la condicion de que si el rectangulo del misil
        llegue a ser menor a 0 que el misil se elimine
        """
        self.rect.y -= 20
        if self.rect.bottom < 0:
            self.kill()

class DisparosEnemigo(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.image.load("Pygame\Galaxia\Imagenes\MisilEnemigo.png")
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x

    def update(self) -> None:
        self.rect.y -= -7
        if self.rect.top > 800:
            self.kill()         

class Explosion(pygame.sprite.Sprite):
	def __init__(self,center):
		super().__init__()
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"Pygame\Galaxia\Imagenes\egularExplosion0{num}.png")
			img = pygame.transform.scale(img, (60, 60))
			self.images.append(img)
		self.indice = 0
		self.image = self.images[self.indice]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.contador = 0

	def update(self):
		velocidad_explosion = 4
		self.contador += 1
		if self.contador >= velocidad_explosion and self.indice < len(self.images) - 1:
			self.contador = 0
			self.indice += 1
			self.image = self.images[self.indice]
        #cuando se completa la animacion la resetea
		if self.indice >= len(self.images) - 1 and self.contador >= velocidad_explosion:
			self.kill()
#***********************GRUPO DE SPRITES Y INICIACION DE OBJETOS****************************
"""
Tenemos un grupo creado de sprite lo hacemos con la clase Group()
del modulo sprite de pygame con esto agrupamos los sprite que queramos
para que trabajen en un conjunto y se almacene en la variable sprites
realizamos lo mismo con la variable  misiles 
despues instanciamos al jugador y al grupo le añado el jugador
"""
sprites = pygame.sprite.Group()
enemigos_grupo1 = pygame.sprite.Group()
enemigos_grupo2 = pygame.sprite.Group()
enemigos_grupo3 = pygame.sprite.Group()
misiles = pygame.sprite.Group()
enemigos_misiles = pygame.sprite.Group()
explosiones_grupo = pygame.sprite.Group()
