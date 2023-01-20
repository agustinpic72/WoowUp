import unittest
from main import Tema, AlertaInformativa, AlertaUrgente, Alerta, lista_alertas

class TemaTestCase(unittest.TestCase):
    def setUp(self):
        lista_alertas.clear()

        self.tema_deportes = Tema('deportes')
        self.tema_tecnologia = Tema('tecnologia')
        self.tema_literatura = Tema('literatura')

        self.alerta_spam_deportiva = Alerta(tema = self.tema_deportes)
        self.alerta_spam_tecnologica = Alerta(tema = self.tema_tecnologia)
        self.alerta_spam_literaria = Alerta(tema = self.tema_literatura)

        self.alerta_informativa_deportiva = AlertaInformativa(tema = self.tema_deportes)
        self.alerta_informativa_tecnologica = AlertaInformativa(tema = self.tema_tecnologia)
        self.alerta_informativa_literaria = AlertaInformativa(tema = self.tema_literatura)

        self.alerta_urgente_deportiva = AlertaUrgente(tema = self.tema_deportes)
        self.alerta_urgente_tecnologica = AlertaUrgente(tema = self.tema_tecnologia)
        self.alerta_urgente_literaria = AlertaUrgente(tema = self.tema_literatura)


    def test_cargar_y_obtener_alertas(self):
        self.tema_deportes.asigna_alertas_a_temas()
        self.assertEqual(len(self.tema_deportes.obtener_alertas()),3)
        self.assertEqual(len(self.tema_deportes.obtener_alertas()['spam']),1)
        self.assertEqual(len(self.tema_deportes.obtener_alertas()['urgentes']),1)
        self.assertEqual(len(self.tema_deportes.obtener_alertas()['informativas']),1)

        self.tema_literatura.asigna_alertas_a_temas()
        self.assertEqual(len(self.tema_literatura.obtener_alertas()),3)
        self.assertEqual(len(self.tema_literatura.obtener_alertas()['spam']),1)
        self.assertEqual(len(self.tema_literatura.obtener_alertas()['urgentes']),1)
        self.assertEqual(len(self.tema_literatura.obtener_alertas()['informativas']),1)

        self.tema_tecnologia.asigna_alertas_a_temas()
        self.assertEqual(len(self.tema_tecnologia.obtener_alertas()),3)
        self.assertEqual(len(self.tema_tecnologia.obtener_alertas()['spam']),1)
        self.assertEqual(len(self.tema_tecnologia.obtener_alertas()['urgentes']),1)
        self.assertEqual(len(self.tema_tecnologia.obtener_alertas()['informativas']),1)

    def test_alertas_creadas(self):
        self.assertEqual(len(lista_alertas),9)