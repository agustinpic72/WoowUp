from datetime import datetime
from datetime import timedelta

lista_alertas = []
lista_usuarios = []

class Usuario():     
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.alertas_usuario = []
        self.temas_usuario = ['spam']
        if self not in lista_usuarios:
            lista_usuarios.append(self)

    def asigna_temas(self, tema):
        try:
            self.temas_usuario.append(tema)
            return 'Tema agregado'
        except Exception as e:
            return f'Ocurrio un problema: {e}'
    
    def obtener_temas(self):
        return self.temas_usuario

    def asigna_alerta_unica(self, alerta):
        self.alertas_usuario.append(alerta)

    def filtra_alertas_leidas_y_expiradas(self):
        alertas_expiradas = []
        for indice, alerta in enumerate(self.alertas_usuario):
            if datetime.now() > alerta.fecha_expiracion or alerta.alerta_leida == True:
                self.alertas_usuario.pop(indice)
                alertas_expiradas.append(alerta)
        return alertas_expiradas
            

    def asigna_alertas(self):
        for alerta in lista_alertas:
            if datetime.now() < alerta.fecha_expiracion and alerta.tema in self.obtener_temas() and alerta not in self.alertas_usuario:
                self.alertas_usuario.append(alerta)
            else:
                continue

    def obtener_alertas_sin_leer(self):
        alertas = self.alertas_usuario
        alertas_informativas = [alerta for alerta in alertas if alerta.tipo_de_alerta == 'Informativa' and alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_urgentes = [alerta for alerta in alertas if alerta.tipo_de_alerta == 'Urgente' and alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_spam = [alerta for alerta in alertas if alerta.tipo_de_alerta == 'Spam' and alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas = []
        alertas.append(sorted(alertas_urgentes, key=lambda alerta: alerta.fecha_expiracion))
        alertas.append(sorted(alertas_informativas, key=lambda alerta: alerta.fecha_expiracion))
        alertas.append(sorted(alertas_spam, key=lambda alerta: alerta.fecha_expiracion))
        return {'urgentes':alertas[0], 'informativas':alertas[1], 'spam':alertas[2]}
    
    def __str__(self):
        return self.nombre_usuario
    
class Tema():
    def __init__(self, tema = None):
        self.tema = tema
        self.alertas = {'urgentes':[],'informativas':[],'spam':[]}

    def asigna_alertas_a_temas(self):
        for alerta in lista_alertas:
            if alerta.tema.__str__() == self.tema and alerta not in self.alertas and alerta.tipo_de_alerta == 'Informativa':
                self.alertas['informativas'].append(alerta)
            elif alerta.tema.__str__() == self.tema and alerta not in self.alertas and alerta.tipo_de_alerta == 'Urgente':
                self.alertas['urgentes'].append(alerta)
            elif alerta.tema.__str__() == self.tema and alerta not in self.alertas and alerta.tipo_de_alerta == 'Spam':
                self.alertas['spam'].append(alerta)
    
    def asigna_alertas_a_usuarios(self):
        for usuario in lista_usuarios:
            usuario.asigna_alertas()
            
    def obtener_alertas(self):
        alertas_sin_leer_ni_expirar = {'urgentes':[],'informativas':[],'spam':[]}
        alertas_urgentes_sin_leer_ni_expirar =  [alerta for alerta in self.alertas['urgentes'] if alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_informativas_sin_leer_ni_expirar =  [alerta for alerta in self.alertas['informativas'] if alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_spam_sin_leer_ni_expirar =  [alerta for alerta in self.alertas['spam'] if alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_sin_leer_ni_expirar['urgentes'] = alertas_urgentes_sin_leer_ni_expirar
        alertas_sin_leer_ni_expirar['informativas'] = alertas_informativas_sin_leer_ni_expirar
        alertas_sin_leer_ni_expirar['spam'] = alertas_spam_sin_leer_ni_expirar
        return alertas_sin_leer_ni_expirar

    def __str__(self):
        return self.tema

class Alerta(Tema):
    #Las alertas expiran 1 dia, 10 horas despues de creadas
    def __init__(self, tema = None, alerta_leida = False, tipo_de_alerta = 'Spam', fecha_expiracion = datetime.now() + timedelta(days=1, hours=10)):
        Tema.__init__(self, tema)
        self.alerta_leida = alerta_leida
        self.fecha_expiracion = fecha_expiracion
        self.tipo_de_alerta = tipo_de_alerta
        lista_alertas.append(self)
        self.asigna_alertas_a_temas()
        self.asigna_alertas_a_usuarios()

    def obtener_tema(self):
        return self.tema.__str__()

    def obtener_fecha_expiracion(self):
        return self.fecha_expiracion
    
    def obtener_tiempo_hasta_que_expire(self):
        return self.fecha_expiracion - datetime.now()

    def obtener_tipo_de_alerta(self):
        return self.tipo_de_alerta
    
    def __str__(self):
        return f'Alerta de tipo {self.obtener_tipo_de_alerta()}'

        
class AlertaInformativa(Alerta):
    def __init__(self, tema = None, alerta_leida = False):
        Alerta.__init__(self, tema, alerta_leida, tipo_de_alerta = 'Informativa', fecha_expiracion = datetime.now() + timedelta(days=1, hours=10))
    
class AlertaUrgente(Alerta):
    def __init__(self, tema = None, alerta_leida = False):
        Alerta.__init__(self, tema, alerta_leida, tipo_de_alerta = 'Urgente', fecha_expiracion = datetime.now() + timedelta(days=1, hours=10))

    