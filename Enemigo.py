import random
from Usuario import UsuarioNormal, Usuario


class Enemigo:

    #Un enemigo tiene un usuario contra el que lucha
    def __init__(self, nivel:int):
        """Constructor de un Enemigo. Se inicializa a un nivel dado.

        :param nivel: nivel del enemigo contra el que se quiere luchar
        Dependiendo del nivel del enemigo, tendrá mñás fuerza de ataque, más resistencia y más vida
        """
        self.vida : int = 30 + nivel * 3;
        self.nivel : int = nivel;
        self.ataque : int = 5 + nivel * 2;
        self.defensa : int = 5 + nivel;
        self.piedra : bool = False;
        self.turnosEnPiedra : int = 0;

    def curar(self):
        """Restaura vida del enemigo a partir de su defensa

        :return: la vida total del enemigo una vez restaurada
        """
        print("El enemigo se ha curado ", self.defensa , " puntos.");
        self.vida += self.defensa;

    def ataqueCuerpoACuerpo(self):
        """Un ataque cuerpo a cuerpo del enemigo

        :return: la cantidad de daño que le puede hacer al usuario
        """
        print("El enemigo ha hecho un ataque cuerpo a cuerpo. Puntos restados: ", self.ataque + 2);
        return self.ataque + 2;

    def ataqueChino(self):
        """Un ataque chino que hace el enemigo

        :return: la cantidad de daño que le puede hacer al usuario
        """
        print("El enemigo ha hecho un ataque chino. Puntos restados: ", self.ataque + 4);
        return self.ataque + 4;

    def enPiedra(self):
        return self.piedra;

    def lanzarAtaque(self, usuario: Usuario):
        """A paritr de un método aleatorio, se lanzará alguno de los ataques del enemigo (cuerpo a cuerpo, chino o curar)

        :param usuario: usuario al que se le va a lanzar el ataque
        Para lanzar el ataque, se debe comprobar que el enemigo no se encuentra en estado piedra.
        """
        self.enemigoCumplioTurnos();
        if(self.enPiedra()):
            print("Enemigo en piedra, no puede realizar ningún ataque.");
            return;
        numero = random.randint(1,3);
        if(numero == 1):
            self.curar();
        elif(numero == 2):
            usuario.vida -= self.ataqueChino();
        else:
            usuario.vida -= self.ataqueCuerpoACuerpo();

    def enemigoCumplioTurnos(self):
        '''Comprueba si el enemigo ya cumplió sus 3 turnos de estar en piedra.

        :return: True si los cumplió, False en caso contrario
        '''
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(self.turnosEnPiedra);
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        if(self.enPiedra() == True):
            if(self.turnosEnPiedra >= 3):
                self.turnosEnPiedra = 0;
                self.piedra = False;
                print("El enemigo ya no se encuentra en piedra!!!");
            else:
                self.turnosEnPiedra += 1;
        else:
            pass

    def muerto(self):
        """Se utiliza para saber si el enemigo está muerto o no

        :return: True en caso de que el enemigo esté muerto, False en caso contrario
        """
        if self.vida <= 0:
            return True;
        return False;