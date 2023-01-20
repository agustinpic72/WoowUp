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

def asignaciones():
    agustin.asigna_temas(tema_deportes)
    kike.asigna_temas(tema_tecnologia)
    marta.asigna_temas(tema_literatura)

    agustin.asigna_alertas()
    kike.asigna_alertas()
    marta.asigna_alertas()

    tema_deportes.asigna_alertas_a_temas()
    tema_literatura.asigna_alertas_a_temas()
    tema_tecnologia.asigna_alertas_a_temas()

def demostracion_completa():

    print('=' * 60)
    print(f'\nLos temas de interes de {agustin} son: {agustin.obtener_temas()}')
    print(f'Los temas de interes de {kike} son: {kike.obtener_temas()}')
    print(f'Los temas de interes de {marta} son: {marta.obtener_temas()}\n')
    print('=' * 60)

    print(f'\nLas alertas sin leer de {agustin} son: {agustin.obtener_alertas_sin_leer()}')
    print(f'Las alertas sin leer de {kike} son: {kike.obtener_alertas_sin_leer()}')
    print(f'Las alertas sin leer de {marta} son: {marta.obtener_alertas_sin_leer()}\n')
    print('=' * 60)

    print(f'\nLas alertas sin leer del tema {tema_deportes.__str__()} son: {tema_deportes.obtener_alertas()}')
    print(f'Las alertas sin leer del tema {tema_tecnologia.__str__()} son: {tema_tecnologia.obtener_alertas()}')
    print(f'Las alertas sin leer del tema {tema_literatura.__str__()} son: {tema_literatura.obtener_alertas()}\n')
    print('=' * 60)

    print(f'\nEsta alerta pertenece al tema: {alerta_spam_deportiva.obtener_tema()}')
    print(f'Esta alerta pertenece al tema: {alerta_spam_tecnologica.obtener_tema()}')
    print(f'Esta alerta pertenece al tema: {alerta_spam_literaria.obtener_tema()}\n')
    print('=' * 60)

    print(f'\nEsta tarjeta expirara en la fecha: {alerta_informativa_deportiva.obtener_fecha_expiracion()}')
    print(f'Esta tarjeta expirara en la fecha: {alerta_informativa_tecnologica.obtener_fecha_expiracion()}')
    print(f'Esta tarjeta expirara en la fecha: {alerta_informativa_literaria.obtener_fecha_expiracion()}\n')
    print('=' * 60)

    print(f'\nFalta {alerta_urgente_deportiva.obtener_tiempo_hasta_que_expire()} para que la alerta expire')
    print(f'Falta {alerta_urgente_deportiva.obtener_tiempo_hasta_que_expire()} para que la alerta expire')
    print(f'Falta {alerta_urgente_deportiva.obtener_tiempo_hasta_que_expire()} para que la alerta expire\n')
    print('=' * 60)

    print(f'\n{alerta_spam_literaria}')
    print(f'{alerta_informativa_tecnologica}')
    print(f'{alerta_urgente_deportiva}\n')
    print('=' * 60)

if __name__ == '__main__':
    asignaciones()
    demostracion_completa()

