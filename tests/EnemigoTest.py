import unittest
from Enemigo import Enemigo

class TestEnemigo(unittest.TestCase):

    def setUp(self):
        self.testClass = Enemigo(2);

    def test_constructor(self):
        self.assertEquals(hasattr(self.testClass, "vida"), True);
        self.assertEquals(hasattr(self.testClass, "nivel"), True);
        self.assertEquals(hasattr(self.testClass, "ataque"), True)
        self.assertEquals(hasattr(self.testClass, "defensa"), True)
        self.assertEquals(hasattr(self.testClass, "piedra"), True)

        self.assertEquals(self.testClass.vida, 36);
        self.assertEquals(self.testClass.nivel, 2);
        self.assertEquals(self.testClass.ataque, 9);
        self.assertEquals(self.testClass.defensa, 7);
        self.assertEquals(self.testClass.piedra, False);

    def test_curar(self):
        self.assertEquals(hasattr(self.testClass.curar, "__call__"), True);
        self.testClass.curar();
        self.assertEquals(self.testClass.vida, 43);

    def test_cuerpoACuerpo(self):
        self.assertEquals(hasattr(self.testClass.ataqueCuerpoACuerpo, "__call__"), True);
        self.assertEquals(self.testClass.ataqueCuerpoACuerpo(), 11);

    def test_ataqueChino(self):
        self.assertEquals(hasattr(self.testClass.ataqueChino, "__call__"), True);
        self.assertEquals(self.testClass.ataqueChino(), 13);

    def test_lanzarAtaque(self):
        self.assertEquals(hasattr(self.testClass.lanzarAtaque, "__call__"), True);

    def test_muerto(self):
        self.testClass.vida = 0;
        self.assertEquals(hasattr(self.testClass.muerto, "__call__"), True);
        self.assertEquals(self.testClass.muerto(), True);



