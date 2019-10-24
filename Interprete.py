from Ataques.Ataques import Ataque
from Enemigo import Enemigo
from Juego import Juego
from Reader import Reader
from Usuario import UsuarioNormal
from Mensajes import Mensaje

reader = Reader();

#Programa principal
def interprete():
    """Programa principal de la aplicación

    Se lanza la aplicación a partir de esta función
    """
    modo = modoFuncionamiento();
    if (modo == "1"):
        reader.load_lines(".\\comandos.txt")

    usuario = UsuarioNormal();
    enemigo = Enemigo(1);
    juego = Juego(usuario, enemigo);
    Mensaje.bienvenida();
    while True:
        Mensaje.estado(juego);
        atq = accionUsuario(usuario, enemigo, modo);
        if atq == False:
            juego.nivelSuperado();
            Mensaje.despedida(juego);
            break;
        if enemigo.muerto() == True:
            juego.nivelSuperado();
            juego.nivelActual += 1;
            enemigo = Enemigo(juego.nivelActual);
            juego.enemigo = enemigo;
            Mensaje.enemigoMuerto()
        else:
            enemigo.lanzarAtaque(usuario);
        if(usuario.muerto() == True):
            Mensaje.usuarioMuerto();
            Mensaje.estado(juego);
            juego.nivelSuperado();
            Mensaje.despedida(juego);
            break;
        else:
            usuario.generarBonus();
        usuario.compruebaEstado();

def modoFuncionamiento():
    """Devuelve el modo funcionamiento de la aplicación.

    Si el usuario introduce un modo distinto de 0 o 1, el sistema se lo volverá a pedir
    :return: El modo de funcionamiento
    """
    Mensaje.modoFuncionamiento();
    m = input();
    while m != "0" and m != "1":
        print("Modo incorrecto. Inténtelo de nuevo:")
        m = input();
    return m;

def accionUsuario(usuario: UsuarioNormal, enemigo: Enemigo, modo:str):
    """Ejecuta la acción del usuario sobre el enemigo, o la ayuda y salida de la aplicación

    :param usuario: el usuario que lanza el ataque
    :param enemigo: el enemigo sobre el que se lanza el ataque
    :param modo: el modo en el que se juega para saber si la orden la mete el jugador o está en un fichero
    :return: False, si el usuario sale del juego o True en caso contrario
    """
    print("Es tu turno, lance un ataque:")
    accion = pedirAccion(modo);
    ataque = Ataque.getAtaque(accion)
    while(ataque == None):
        if(accion == "ayuda"):
            Mensaje.ayuda();
        elif (accion == "fin"):
            return False;
        else:
            print("Ataque desconocido, inténtelo de nuevo")
        accion = pedirAccion(modo);
        ataque =  Ataque.getAtaque(accion);
    usuario.execute(ataque, enemigo);
    return True;

def pedirAccion(modo: str):
    """Pide la acción a ejecutar al usuario o la lee del fichero

    :param modo: modo en el que se está jugando para saber si la acción se la pide al usuario o está en un fichero
    :return: la acción a ejecutar
    """
    if modo == "0":
        accion = input();
        return accion;
    else:
        return reader.getComando();


if __name__ == "__main__":
    interprete();