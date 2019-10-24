import unittest
from Enemigo import Enemigo
from Juego import Juego
from Usuario import UsuarioNormal


class TestEnemigo(unittest.TestCase):

    def setUp(self):
        self.usuario = UsuarioNormal();
        self.enemigo = Enemigo(2);
        self.testClass = Juego(self.usuario, self.enemigo);

    def test_constructor(self):
        self.assertEquals(hasattr(self.testClass, "usuario"), True);
        self.assertEquals(hasattr(self.testClass, "enemigo"), True);
        self.assertEquals(hasattr(self.testClass, "nivelActual"), True)
        self.assertEquals(hasattr(self.testClass, "tiempo"), True)

        self.assertEqual(self.testClass.usuario, self.usuario);
        self.assertEqual(self.testClass.enemigo, self.enemigo);
        self.assertEqual(self.testClass.nivelActual, 1);

    def test_nivelSuperado(self):
        self.assertEquals(hasattr(self.testClass.nivelSuperado, "__call__"), True);

    def test_mostrarTiempos(self):
        self.assertEquals(hasattr(self.testClass.mostrarTiempos, "__call__"), True);
