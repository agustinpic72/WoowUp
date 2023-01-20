from main import *

agustin = Usuario('agustin', 'password')
kike = Usuario('enrique', 'password')
marta = Usuario('marta', 'password')
martin = Usuario('martin', 'password')

tema_deportes = Tema('deportes')
tema_tecnologia = Tema('tecnologia')
tema_literatura = Tema('literatura')

alerta_unica_agustin = Alerta(tema = tema_deportes)
alerta_unica_kike = Alerta(tema = tema_tecnologia)
alerta_unica_marta = Alerta(tema = tema_literatura)

alerta_unica_expirada_agustin = Alerta(tema = tema_deportes, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))
alerta_unica_expirada_kike = Alerta(tema = tema_tecnologia, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))
alerta_unica_expirada_marta = Alerta(tema = tema_literatura, fecha_expiracion = datetime.now() - timedelta(days=1, hours=10))

alerta_spam_deportiva = Alerta(tema = tema_deportes)
alerta_spam_tecnologica = Alerta(tema = tema_tecnologia)
alerta_spam_literaria = Alerta(tema = tema_literatura)

alerta_informativa_deportiva = AlertaInformativa(tema = tema_deportes)
alerta_informativa_tecnologica = AlertaInformativa(tema = tema_tecnologia)
alerta_informativa_literaria = AlertaInformativa(tema = tema_literatura)

alerta_urgente_deportiva = AlertaUrgente(tema = tema_deportes)
alerta_urgente_tecnologica = AlertaUrgente(tema = tema_tecnologia)
alerta_urgente_literaria = AlertaUrgente(tema = tema_literatura)

