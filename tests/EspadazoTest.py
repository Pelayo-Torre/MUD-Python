import unittest
from Enemigo import Enemigo
from Ataques.Espadazo import Espadazo
from Usuario import UsuarioNormal

class TestEspadazo(unittest.TestCase):

    def setUp(self):
        self.testClass = Espadazo();
        self.enemigo = Enemigo(2);
        self.usuario = UsuarioNormal();

    def test_execute(self):
        self.assertEquals(hasattr(self.testClass.execute, "__call__"), True);

        self.assertEquals(self.enemigo.vida, 36);
        self.assertEquals(self.usuario.vida, 60);

        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.enemigo.vida, 23);
        self.assertEquals(self.usuario.vida, 57);


