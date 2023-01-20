import unittest
from main import Tema, Alerta, AlertaInformativa, AlertaUrgente, lista_alertas
from datetime import datetime, timedelta

class AlertaTestCase(unittest.TestCase):
    def setUp(self):
        lista_alertas.clear()

        self.tema_deportes = Tema('deportes')
        self.tema_tecnologia = Tema('tecnologia')
        self.tema_literatura = Tema('literatura')

        self.alerta_deportiva = Alerta(tema = self.tema_deportes)
        self.alerta_tecnologica = Alerta(tema = self.tema_tecnologia)
        self.alerta_literaria = Alerta(tema = self.tema_literatura)


        self.alerta_deportiva_expirada = Alerta(tema = self.tema_deportes, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))
        self.alerta_tecnologica_expirada = Alerta(tema = self.tema_tecnologia, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))
        self.alerta_literaria_expirada = Alerta(tema = self.tema_literatura, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))

    def test_obtener_tema(self):
        self.assertEqual(self.alerta_deportiva.obtener_tema(),'Esta alerta pertenece al tema: deportes')
        self.assertEqual(self.alerta_tecnologica.obtener_tema(),'Esta alerta pertenece al tema: tecnologia')
        self.assertEqual(self.alerta_literaria.obtener_tema(),'Esta alerta pertenece al tema: literatura')
    
    def test_obtener_fecha_expiracion(self):
        self.assertLess(datetime.now(), self.alerta_deportiva.obtener_fecha_expiracion())
        self.assertLess(datetime.now(), self.alerta_tecnologica.obtener_fecha_expiracion())
        self.assertLess(datetime.now(), self.alerta_literaria.obtener_fecha_expiracion())

        self.assertLess(self.alerta_deportiva_expirada.obtener_fecha_expiracion(), datetime.now())
        self.assertLess(self.alerta_tecnologica_expirada.obtener_fecha_expiracion(), datetime.now())
        self.assertLess(self.alerta_literaria_expirada.obtener_fecha_expiracion(), datetime.now())
    
    def test_obtener_tiempo_hasta_que_expire(self):
        self.assertGreater(self.alerta_deportiva.obtener_tiempo_hasta_que_expire(), timedelta(days=0, hours=0))
        self.assertGreater(self.alerta_tecnologica.obtener_tiempo_hasta_que_expire(), timedelta(days=0, hours=0))
        self.assertGreater(self.alerta_literaria.obtener_tiempo_hasta_que_expire(), timedelta(days=0, hours=0))

        self.assertGreater(timedelta(days=0, hours=0), self.alerta_deportiva_expirada.obtener_tiempo_hasta_que_expire())
        self.assertGreater(timedelta(days=0, hours=0), self.alerta_tecnologica_expirada.obtener_tiempo_hasta_que_expire())
        self.assertGreater(timedelta(days=0, hours=0), self.alerta_literaria_expirada.obtener_tiempo_hasta_que_expire())

    def test_obtener_tipo_de_alerta(self):
        self.assertEqual(self.alerta_deportiva.obtener_tipo_de_alerta(),'Spam')
        self.assertEqual(self.alerta_tecnologica.obtener_tipo_de_alerta(),'Spam')
        self.assertEqual(self.alerta_literaria.obtener_tipo_de_alerta(),'Spam')

    def test_alertas_creadas(self):
        self.assertEqual(len(lista_alertas),6)

class AlertaInformativaTestCase(unittest.TestCase):
    def setUp(self):
        lista_alertas.clear()

        self.tema_deportes = Tema('deportes')
        self.tema_tecnologia = Tema('tecnologia')
        self.tema_literatura = Tema('literatura')

        self.alerta_informativa_deportiva = AlertaInformativa(tema = self.tema_deportes)
        self.alerta_informativa_tecnologica = AlertaInformativa(tema = self.tema_tecnologia)
        self.alerta_informativa_literaria = AlertaInformativa(tema = self.tema_literatura)

    def test_obtener_tipo_de_alerta(self):
        self.assertEqual(self.alerta_informativa_deportiva.obtener_tipo_de_alerta(),'Informativa')
        self.assertEqual(self.alerta_informativa_tecnologica.obtener_tipo_de_alerta(),'Informativa')
        self.assertEqual(self.alerta_informativa_literaria.obtener_tipo_de_alerta(),'Informativa')

    def test_alertas_creadas(self):
        self.assertEqual(len(lista_alertas),3)

class AlertaUrgenteTestCase(unittest.TestCase):
    def setUp(self):
        lista_alertas.clear()

        self.tema_deportes = Tema('deportes')
        self.tema_tecnologia = Tema('tecnologia')
        self.tema_literatura = Tema('literatura')

        self.alerta_urgente_deportiva = AlertaUrgente(tema = self.tema_deportes)
        self.alerta_urgente_tecnologica = AlertaUrgente(tema = self.tema_tecnologia)
        self.alerta_urgente_literaria = AlertaUrgente(tema = self.tema_literatura)

    def test_obtener_tipo_de_alerta(self):
        self.assertEqual(self.alerta_urgente_deportiva.obtener_tipo_de_alerta(),'Urgente')
        self.assertEqual(self.alerta_urgente_tecnologica.obtener_tipo_de_alerta(),'Urgente')
        self.assertEqual(self.alerta_urgente_literaria.obtener_tipo_de_alerta(),'Urgente')

    def test_alertas_creadas(self):
        self.assertEqual(len(lista_alertas),3)