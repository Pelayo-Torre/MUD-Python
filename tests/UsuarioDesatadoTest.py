import unittest
from Enemigo import Enemigo
from Usuario import Usuario, UsuarioDesatado, UsuarioNormal


class TestUsuarioNormal(unittest.TestCase):

    def setUp(self):
        self.usuarioDesatado = UsuarioDesatado();

    def test_constructor(self):
        self.assertEquals(hasattr(self.usuarioDesatado, "vida"), True);
        self.assertEquals(hasattr(self.usuarioDesatado, "hechizos"), True);
        self.assertEquals(hasattr(self.usuarioDesatado, "flechas"), True)

        self.assertEquals(self.usuarioDesatado.vida, 60);
        self.assertEquals(self.usuarioDesatado.hechizos, 3);
        self.assertEquals(self.usuarioDesatado.flechas, 7);


    def test_execute(self):
        self.assertEquals(hasattr(self.usuarioDesatado.execute, "__call__"), True);

    def test_muerto(self):
        self.usuarioDesatado.vida = 0;
        self.assertEquals(hasattr(self.usuarioDesatado.muerto, "__call__"), True);
        self.assertEquals(self.usuarioDesatado.muerto(), True);

    def test_generarBonus(self):
        self.assertEquals(hasattr(self.usuarioDesatado.generarBonus, "__call__"), True);

    def test_claseBase(self):
        self.assertEquals(issubclass(self.usuarioDesatado.__class__, Usuario), True);

    def test_strEstado(self):
        self.assertEquals(hasattr(self.usuarioDesatado.strEstado, "__call__"), True);
        self.assertEquals(self.usuarioDesatado.strEstado(), "USUARIO DESATADO")

    def test_cambioEstado(self):
        self.assertEquals(self.usuarioDesatado.__class__, UsuarioDesatado);
        self.usuarioDesatado.vida = 50;
        self.usuarioDesatado.compruebaEstado();
        self.assertEquals(self.usuarioDesatado.__class__, UsuarioNormal);
        self.usuarioDesatado.vida = 20;
        self.usuarioDesatado.compruebaEstado();
        self.assertEquals(self.usuarioDesatado.__class__, UsuarioDesatado);