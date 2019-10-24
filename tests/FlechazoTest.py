import unittest
from Enemigo import Enemigo
from Ataques.Flechazo import Flechazo
from Usuario import UsuarioNormal

class TestFlechazo(unittest.TestCase):

    def setUp(self):
        self.testClass = Flechazo();
        self.enemigo = Enemigo(2);
        self.usuario = UsuarioNormal();

    def test_execute(self):
        self.assertEquals(hasattr(self.testClass.execute, "__call__"), True);

        self.assertEquals(self.enemigo.vida, 36);
        self.assertEquals(self.usuario.flechas, 7);

        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.enemigo.vida, 21);
        self.assertEquals(self.usuario.flechas, 6);

        self.testClass.execute(self.enemigo, self.usuario);
        self.testClass.execute(self.enemigo, self.usuario);
        self.testClass.execute(self.enemigo, self.usuario);
        self.testClass.execute(self.enemigo, self.usuario);
        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.enemigo.muerto(), True);
        self.assertEquals(self.usuario.flechas, 1);

        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.usuario.flechas, 0);

        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.usuario.flechas, 0);

