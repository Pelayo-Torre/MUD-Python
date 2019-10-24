from collections import deque

class Reader():

    def __init__(self):
        """Constructor del lector de las órdenes del fichero de texto

        Se configura con una COLA, para ir sacando las órdenes leídas del fichero de izquierda a derecha.
        """
        self.comandos = [];
        self.deque = None;

    def load_lines(self, file:str):
        """Lee las órdenes del fichero de texto y las almacena en la COLA.

        :param file: nombre del fichero a leer las órdenes
        """
        with open(file) as lines:
            for i in lines:
                l = i.strip('\n')
                self.comandos.append(l)
            self.deque = deque(self.comandos)

    def getComando(self):
        """Devuelve la siguiente órden a ejecutarse del fichero.

        Lanza una excepción en caso de que el fichero venga vacío.
        :return: la siguiente órden a ejecutarse
        """
        if len(self.deque) == 0:
            raise Exception("El fichero no tiene órdenes.")
        return self.deque.popleft();

