import unittest
from Ataques.Ataques import Ataque
from Ataques.Espadazo import Espadazo
from Ataques.Flechazo import Flechazo
from Ataques.Hechizo import Hechizo

class TestAtaques(unittest.TestCase):

    def test_atributo(self):
        self.assertEquals(hasattr(Ataque, "ataques"), True);
        self.assertEquals(len(Ataque.ataques), 3);

    def test_getAtaque(self):
        self.assertEquals(hasattr(Ataque.getAtaque, "__call__"), True);
        self.assertEquals(Ataque.getAtaque("hechizo").__class__, Hechizo)
        self.assertEquals(Ataque.getAtaque("espadazo").__class__, Espadazo)
        self.assertEquals(Ataque.getAtaque("flechazo").__class__, Flechazo)
        self.assertIsNone(Ataque.getAtaque("6456yge5"), None)

    def test_getAtaques(self):
        self.assertEquals(hasattr(Ataque.getAtaques, "__call__"), True);
        self.assertEquals(len(Ataque.getAtaques()), 3);
        self.assertEquals(Ataque.getAtaques(), Ataque.ataques);


