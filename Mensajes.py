import Juego
from Ataques.Ataques import Ataque

class Mensaje():

    @staticmethod
    def estado(juego: Juego):
        """Muestra por pantalla el estado del juego en el momento actual.

        :param juego: Para obtener el estado de dicho juego
        """
        print("---------ESTADO ACTUAL---------")
        print("             NIVEL ", juego.nivelActual);
        print();
        print("Jugador");
        print("   -Vida: ", juego.usuario.vida, " puntos")
        print("   -Hechizos: ", juego.usuario.hechizos);
        print("   -Flechas: ", juego.usuario.flechas);
        print("   -Estado: ", juego.usuario.strEstado())
        print("Enemigo");
        print("   -Vida: ", juego.enemigo.vida, " puntos")
        print();

    @staticmethod
    def bienvenida():
        """Muestra por pantalla un mensaje de bienvenida al jugador de la aplicación.

        """
        print("Bienvenido a MUD!!!")
        print("-------------------")
        print("Intenta derrotar a tu enemigo usando tus distintos ataques.")
        print("Cada vez que lo derrotes, superarás el nivel y te enfrentarás a otro más fuerte que el anterior.")
        print("-------------------------------------------------------------------------------------------------")
        print();
        print("Para mostrar los posibles ataques escriba:")
        print("     << ayuda")
        print("")
        print("COMIENZA LA BATALLA!!!")
        print();

    @staticmethod
    def despedida(juego:Juego):
        """Muestra por pantalla un despedida al jugador.

        :param juego: para obtener la duración de la partida
        """
        print("Gracias por jugar.")
        print("TIEMPO JUGADO: ")
        print(juego.mostrarTiempos())
        print("Hasta la próxima!!!")

    @staticmethod
    def usuarioMuerto():
        """Muestra por pantalla al jugador que ha muerto.

        """
        print("GAME  OVER !!!")
        print("El usuario ha sido vencido.")
        print();
        print("Estado final de la partida:")

    @staticmethod
    def enemigoMuerto():
        """Muestra por pantalla al jugador que el enemigo ha muerto.

        """
        print("El enemigo ha sido eliminado");
        print("Avanzas al siguiente nivel.")

    @staticmethod
    def ayuda():
        """Muestra por pantalla al jugador el manual de ayuda de la aplicación, el cuál contiene todas las órdenes.

        """
        print();
        print();
        print("--------------------------------------------------MANUAL DE AYUDA--------------------------------------------------");
        print("  ATAQUES:")

        for orden in Ataque.ataques:
            print(Ataque.getAtaque(orden));
            print()

        print("  OTROS COMANDOS:");
        print("\t<<ayuda")
        print("\t\tMuestra la ventana de ayuda del juego.");
        print();
        print("\t<<fin")
        print("\t\tFinzaliza la partida del juego.")
        print("-------------------------------------------------------------------------------------------------------------------");
        print();
        print();

    @staticmethod
    def modoFuncionamiento():
        """Muestra por pantalla los distintos modos de funcionamiento que tiene la aplicación.

        """
        print("Seleccione un modo de funcionamiento: ");
        print("   Modo interactivo --> 0");
        print("   Modo fichero --> 1")
        print();
