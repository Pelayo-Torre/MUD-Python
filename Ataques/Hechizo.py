import Enemigo
from Usuario import UsuarioNormal

class Hechizo():

    def execute(self, enemigo:Enemigo, usuario: UsuarioNormal):
        """Orden del patrón COMMAND. Se ejecuta sobre el enemigo.

        :param enemigo: enemigo sobre el que se lanza el ataque
        :param usuario: usuario que lanza el ataque

        """
        if(usuario.hechizos == 0):
            print();
            print("No tienes más hechizos.");
            print();
        else:
            if enemigo.enPiedra():
                print("El enemigo ya se encuentra en piedra.");
            else:
                usuario.hechizos -= 1;
                enemigo.piedra = True;
                print("Hechizo invocado!")

    def __str__(self):
        """Descripción de la orden.

                Se explica la orden en profundidad.
        """
        return "\t<<hechizo\n\t\tLanza un hechizo sobre el enemigo que lo convierte en piedra y no puede atacar durante 3 turnos."