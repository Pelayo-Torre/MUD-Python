import Enemigo
from Usuario import UsuarioNormal
import time


class Juego:
    '''
    En esta clase se almacenarían datos generales de la partida, como diferentes estadísticas, por ejemplo.

    '''

    def __init__(self, usuario: UsuarioNormal, enemigo: Enemigo):
        """Constructor de la clase juego.

        Se configura con un usuario y un enemigo. También se almacena el nivel actual de la partida así como el tiempo
        en el que comenzó dicha partida
        :param usuario: el usuario que lanza el ataque
        :param enemigo: el enemigo sobre el que se lanza el ataque
        """
        self.usuario = usuario;
        self.enemigo = enemigo;
        self.nivelActual : int = 1;
        self.estadisticasNivel = dict();
        self.tiempo = time.time();

    def nivelSuperado(self):
        '''Almacena el tiempo dedicado a cada nivel de la partida

        '''
        self.estadisticasNivel[self.nivelActual] = round((time.time() - self.tiempo) / 60,2);
        self.tiempo = time.time();

    def mostrarTiempos(self):
        cadena : str = "";
        total = 0
        for clave, valor in self.estadisticasNivel.items():
            cadena += "Nivel " + str(clave) + ": " + str(valor) + " minutos.\n";
            total += valor;
        cadena += "\nTIEMPO TOTAL: " + str(round(total, 2)) + " minutos.";
        return cadena;





