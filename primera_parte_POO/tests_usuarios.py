import unittest
from main import Usuario, Tema, Alerta, AlertaInformativa, AlertaUrgente, lista_alertas
from datetime import datetime, timedelta

class UsuarioTestCase(unittest.TestCase):
    def setUp(self):
        lista_alertas.clear()

        self.agustin = Usuario('self.agustin', 'password')
        self.kike = Usuario('enrique', 'password')
        self.marta = Usuario('self.marta', 'password')
        self.martin = Usuario('self.martin', 'password')

        self.tema_deportes = Tema('deportes')
        self.tema_tecnologia = Tema('tecnologia')
        self.tema_literatura = Tema('literatura')

        self.alerta_unica_agustin = Alerta(tema = self.tema_deportes)
        self.alerta_unica_kike = Alerta(tema = self.tema_tecnologia)
        self.alerta_unica_marta = Alerta(tema = self.tema_literatura)

        self.alerta_unica_expirada_agustin = Alerta(tema = self.tema_deportes, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))
        self.alerta_unica_expirada_kike = Alerta(tema = self.tema_tecnologia, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))
        self.alerta_unica_expirada_marta = Alerta(tema = self.tema_literatura, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))

        self.alerta_spam_deportiva = Alerta(tema = self.tema_deportes)
        self.alerta_spam_tecnologica = Alerta(tema = self.tema_tecnologia)
        self.alerta_spam_literaria = Alerta(tema = self.tema_literatura)

        self.alerta_informativa_deportiva = AlertaInformativa(tema = self.tema_deportes)
        self.alerta_informativa_tecnologica = AlertaInformativa(tema = self.tema_tecnologia)
        self.alerta_informativa_literaria = AlertaInformativa(tema = self.tema_literatura)

        self.alerta_urgente_deportiva = AlertaUrgente(tema = self.tema_deportes)
        self.alerta_urgente_tecnologica = AlertaUrgente(tema = self.tema_tecnologia)
        self.alerta_urgente_literaria = AlertaUrgente(tema = self.tema_literatura)

    def test_asigna_y_obtiene_temas(self):
        
        self.agustin.asigna_temas(self.tema_deportes)
        self.assertEqual(self.agustin.obtener_temas()[1].__str__(),'deportes')

        self.kike.asigna_temas(self.tema_tecnologia)
        self.assertEqual(self.kike.obtener_temas()[1].__str__(),'tecnologia')

        self.marta.asigna_temas(self.tema_literatura)
        self.assertEqual(self.marta.obtener_temas()[1].__str__(),'literatura')

        self.martin.asigna_temas(self.tema_deportes)
        self.martin.asigna_temas(self.tema_literatura)
        self.martin.asigna_temas(self.tema_tecnologia)
        self.assertEqual(len(self.martin.obtener_temas()),4)
        self.assertEqual(self.martin.obtener_temas()[0].__str__(),'spam')
        self.assertEqual(self.martin.obtener_temas()[1].__str__(),'deportes')
        self.assertEqual(self.martin.obtener_temas()[2].__str__(),'literatura')
        self.assertEqual(self.martin.obtener_temas()[3].__str__(),'tecnologia')

    def test_asigna_alerta_unica(self):
        self.agustin.asigna_alerta_unica(self.alerta_unica_agustin)
        self.assertEqual(len(self.agustin.alertas_usuario),1)

        self.kike.asigna_alerta_unica(self.alerta_unica_kike)
        self.assertEqual(len(self.kike.alertas_usuario),1)

        self.marta.asigna_alerta_unica(self.alerta_unica_marta)
        self.assertEqual(len(self.marta.alertas_usuario),1)

    def test_filtra_alertas_leidas_y_expiradas(self):
        self.agustin.asigna_alerta_unica(self.alerta_unica_expirada_agustin)
        self.assertEqual(self.agustin.filtra_alertas_leidas_y_expiradas()[0],self.alerta_unica_expirada_agustin)

        self.kike.asigna_alerta_unica(self.alerta_unica_expirada_kike)
        self.assertEqual(self.kike.filtra_alertas_leidas_y_expiradas()[0],self.alerta_unica_expirada_kike)
        
        self.marta.asigna_alerta_unica(self.alerta_unica_expirada_marta)
        self.assertEqual(self.marta.filtra_alertas_leidas_y_expiradas()[0],self.alerta_unica_expirada_marta)

    def test_asigna_y_obtiene_alertas(self):
        #Agrega alertas ya leidas para verificar que la funcion asigne solo las alertas sin leer
        self.alerta_informativa_deportiva_leida = AlertaInformativa(tema = self.tema_deportes, alerta_leida = True)
        self.alerta_informativa_tecnologica_leida = AlertaInformativa(tema = self.tema_tecnologia, alerta_leida = True)
        self.alerta_informativa_literaria_leida = AlertaInformativa(tema = self.tema_literatura, alerta_leida = True)
        self.assertEqual(len(lista_alertas),18)

        #Se llama dos veces a la función asigna_alertas para verificar que no se asignen alertas ya asignadas
        self.agustin.asigna_temas(self.tema_deportes)
        self.agustin.asigna_alertas()
        self.agustin.asigna_alertas()
        self.assertEqual(len(self.agustin.obtener_alertas_sin_leer()),3)
        self.assertEqual(len(self.agustin.obtener_alertas_sin_leer()['spam']),2)
        self.assertEqual(len(self.agustin.obtener_alertas_sin_leer()['urgentes']),1)
        self.assertEqual(len(self.agustin.obtener_alertas_sin_leer()['informativas']),1)
        self.assertEqual(self.agustin.obtener_alertas_sin_leer()['urgentes'][0].tema.__str__(),'deportes')

        self.kike.asigna_temas(self.tema_tecnologia)
        self.kike.asigna_alertas()
        self.kike.asigna_alertas()
        self.assertEqual(len(self.kike.obtener_alertas_sin_leer()),3)
        self.assertEqual(len(self.kike.obtener_alertas_sin_leer()['spam']),2)
        self.assertEqual(len(self.kike.obtener_alertas_sin_leer()['urgentes']),1)
        self.assertEqual(len(self.kike.obtener_alertas_sin_leer()['informativas']),1)
        self.assertEqual(self.kike.obtener_alertas_sin_leer()['urgentes'][0].tema.__str__(),'tecnologia')

        self.marta.asigna_temas(self.tema_literatura)
        self.marta.asigna_alertas()
        self.marta.asigna_alertas()
        self.assertEqual(len(self.marta.obtener_alertas_sin_leer()),3)
        self.assertEqual(len(self.marta.obtener_alertas_sin_leer()['spam']),2)
        self.assertEqual(len(self.marta.obtener_alertas_sin_leer()['urgentes']),1)
        self.assertEqual(len(self.marta.obtener_alertas_sin_leer()['informativas']),1)
        self.assertEqual(self.marta.obtener_alertas_sin_leer()['urgentes'][0].tema.__str__(),'literatura')

        self.martin.asigna_temas(self.tema_deportes)
        self.martin.asigna_temas(self.tema_literatura)
        self.martin.asigna_temas(self.tema_tecnologia)
        self.martin.asigna_alertas()
        self.martin.asigna_alertas()
        self.assertEqual(len(self.martin.obtener_alertas_sin_leer()),3)
        self.assertEqual(len(self.martin.obtener_alertas_sin_leer()['spam']),6)
        self.assertEqual(len(self.martin.obtener_alertas_sin_leer()['urgentes']),3)
        self.assertEqual(len(self.martin.obtener_alertas_sin_leer()['informativas']),3)
        self.assertEqual(self.martin.obtener_alertas_sin_leer()['urgentes'][0].tema.__str__(),'deportes')
        self.assertEqual(self.martin.obtener_alertas_sin_leer()['urgentes'][1].tema.__str__(),'tecnologia')
        self.assertEqual(self.martin.obtener_alertas_sin_leer()['urgentes'][2].tema.__str__(),'literatura')

    def test_alertas_creadas(self):
        self.assertEqual(len(lista_alertas),15)

if __name__ == '__main__':
    unittest.main()

