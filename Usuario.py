import Enemigo
import random

class Usuario():

    def __init__(self):
        """Constructor del usuario de la apliación

        Se configura con 60 puntos de vida, 3 hechizos y 7 flechas
        """
        self.vida : int = 60;
        self.hechizos : int = 3;
        self.flechas : int = 7;

    def execute(self, orden, enemigo: Enemigo):
        """Ejecuta la orden que se le pasa sobre el enemigo

        :param orden: Ataque que el usuario lanza al enemigo
        :param enemigo: enemigo sobre el que se lanza el ataque
        """
        orden.execute(enemigo, self);

    def muerto(self):
        """Comprueba si el usuario está muerto o no

        :return: True en caso de que esté muerto, false en caso contrario
        """
        if self.vida <= 0:
            return True;
        return False;

class UsuarioNormal(Usuario):

    def compruebaEstado(self):
        """Comprueba las vidas del jugador para cambiar dinámicamente de estado

        """
        if (self.vida < 40):
            self.__class__ = UsuarioDesatado
        else:
            pass

    def generarBonus(self):
        """A lo largo de la partida, se genera un bonus aleatorio para el usuario

        El tipo de bonus puede ser 10 puntos más de vida, 2 hechizos más o 5 nuevas flechas.
        El bonus depende del aleatorio que se genere.
        """
        numero = random.randint(1, 5);
        if(numero == 1):
            self.vida += 10;
            print("*****  El jugador ha obtenido un bonus de 10 puntos de vida.  *****")
        elif(numero == 2):
            self.hechizos += 2;
            print("*****  El jugador ha obtenido un bonus de 2 hechizos más.  *****")
        elif(numero == 5):
            self.flechas += 5;
            print("*****  El jugador ha obtenido un bonus de 5 flechas más.  *****")
        else:
            pass

    def strEstado(self):
        """Devuelve el nombre del estado del jugador

        :return: el nombre del estado del jugador
        """
        return "USUARIO NORMAL";

class UsuarioDesatado(Usuario):

    def compruebaEstado(self):
        """Comprueba las vidas del jugador para cambiar dinámicamente de estado

        """
        if (self.vida > 40):
            self.__class__ = UsuarioNormal
        else:
            pass

    def generarBonus(self):
        """A lo largo de la partida, se genera un bonus aleatorio para el usuario

        En el estado desatado, se genera más de elementos que en estado normal
        El tipo de bonus puede ser 10 puntos más de vida, 2 hechizos más o 5 nuevas flechas.
        El bonus depende del aleatorio que se genere.
        """
        numero = random.randint(1, 5);
        if (numero == 1):
            self.vida += 25;
            print();
            print("*****  El jugador ha obtenido un bonus de 25 puntos de vida.  *****")
            print();
        elif (numero == 2):
            self.hechizos += 5;
            print();
            print("*****  El jugador ha obtenido un bonus de 5 hechizos más.  *****")
            print();
        elif (numero == 5):
            self.flechas += 15;
            print();
            print("*****  El jugador ha obtenido un bonus de 15 flechas más.  *****")
            print();
        else:
            pass

    def strEstado(self):
        """Devuelve el nombre del estado del jugador

        :return: el nombre del estado del jugador
        """
        return "USUARIO DESATADO";
