import unittest
from Enemigo import Enemigo
from Usuario import UsuarioNormal, Usuario, UsuarioDesatado


class TestUsuarioNormal(unittest.TestCase):

    def setUp(self):
        self.usuarioNormal = UsuarioNormal();

    def test_constructor(self):
        self.assertEquals(hasattr(self.usuarioNormal, "vida"), True);
        self.assertEquals(hasattr(self.usuarioNormal, "hechizos"), True);
        self.assertEquals(hasattr(self.usuarioNormal, "flechas"), True)

        self.assertEquals(self.usuarioNormal.vida, 60);
        self.assertEquals(self.usuarioNormal.hechizos, 3);
        self.assertEquals(self.usuarioNormal.flechas, 7);


    def test_execute(self):
        self.assertEquals(hasattr(self.usuarioNormal.execute, "__call__"), True);

    def test_muerto(self):
        self.usuarioNormal.vida = 0;
        self.assertEquals(hasattr(self.usuarioNormal.muerto, "__call__"), True);
        self.assertEquals(self.usuarioNormal.muerto(), True);

    def test_generarBonus(self):
        self.assertEquals(hasattr(self.usuarioNormal.generarBonus, "__call__"), True);

    def test_claseBase(self):
        self.assertEquals(issubclass(self.usuarioNormal.__class__, Usuario), True);

    def test_strEstado(self):
        self.assertEquals(hasattr(self.usuarioNormal.strEstado, "__call__"), True);
        self.assertEquals(self.usuarioNormal.strEstado(), "USUARIO NORMAL")

    def test_cambioEstado(self):
        normal = UsuarioNormal();
        desatado = UsuarioDesatado();
        self.assertEquals(type(self.usuarioNormal), type(normal));
        self.usuarioNormal.vida = 20;
        self.usuarioNormal.compruebaEstado();
        self.assertEquals(type(self.usuarioNormal), type(desatado));
        self.usuarioNormal.vida = 50;
        self.usuarioNormal.compruebaEstado();
        self.assertEquals(type(self.usuarioNormal), type(normal));