import unittest
from Enemigo import Enemigo
from Ataques.Hechizo import Hechizo
from Usuario import UsuarioNormal

class TestFlechazo(unittest.TestCase):

    def setUp(self):
        self.testClass = Hechizo();
        self.enemigo = Enemigo(2);
        self.usuario = UsuarioNormal();

    def test_execute(self):
        self.assertEquals(hasattr(self.testClass.execute, "__call__"), True);

        self.assertEquals(self.enemigo.vida, 36);
        self.assertEquals(self.usuario.hechizos, 3);
        self.assertEquals(self.enemigo.piedra, False);

        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.enemigo.vida, 36);
        self.assertEquals(self.enemigo.piedra, True);
        self.assertEquals(self.usuario.hechizos, 2);

        self.testClass.execute(self.enemigo, self.usuario);

        self.assertEquals(self.enemigo.vida, 36);
        self.assertEquals(self.enemigo.piedra, True);
        self.assertEquals(self.usuario.hechizos, 2);

