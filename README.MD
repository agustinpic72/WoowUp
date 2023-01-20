# Entrevista técnica para WoowUp
En este repositorio se podrán encontrar con la resolución de una prueba técnica para la empresa: [WoowUp.](https://www.woowup.com/)

## Comentarios
Seguramente conocés la funcionalidad de Notificaciones de Facebook: es esa campanita arriba en el menú donde te muestra las nuevas alertas que el sistema tiene para mostrarte sobre distintos temas: un amigo cumple años, una página que seguís compartió una publicación, un amigo publicó una foto, alguien comentó un posteo tuyo, una sugerencia de amistad, etc.

En este proyecto se busca realizar a grandes rasgos un sistema de usuarios y alertas con programación orientada a objetos en el cual se pueda simular la interaccion del usuario con el entorno.

## Recomendaciones y primeros pasos
El proyecto esta pensado para ejecutarse por linea de comandos, por lo que para ejecutarlo recomiendo abrir una terminal nueva en la carpeta donde hayamos descargado localmente el repositorio, ejecutar python e importar el archivo **main.py** completo. Cabe destacar que tambien existe un archivo llamado **datos_de_ejemplo.py** que al importarlo genera diferentes estructuras de datos para facilitar la interacción con la aplicación, además de esto, también podremos ejecutar el archivo directamente para ver el output de un caso ideal.

```bash
python3 datos_de_ejemplo.py
```
```python
from main import * 
#también podemos utilizar
from datos_de_ejemplo import *
```

Una vez importadas todas las clases y metodos podrémos empezar a jugar un poco con los mismos.
```python
agustin = Usuario('agustin', 'password') #Esta clase solicita un nombre de usuario y una contraseña.
tema_deportes = Tema('deportes') #Creamos un tema para posteriormente asignarlo a nuestro usuario
agustin.asigna_temas(tema_deportes)
'Tema agregado'

```

Ahora que tenemos nuestro usuario configurado podemos proceder a crear alertas.
Las alertas se dividen en 3 tipos, *Urgentes*, consideradas de maxima prioridad, *Informativas*, son de segunda prioridad, y por ultimo decidí agregar un tercer tipo a la clasificación, *Spam*, creada para enviar alertas generales a todos los usuarios, como ser: **Actualizaciones de sistema, cambio en las normas, lanzamiento de una nueva feature**.
```python
alerta_spam_deportiva = Alerta(tema = self.tema_deportes)
alerta_informativa_deportiva = AlertaInformativa(tema = self.tema_deportes)
alerta_urgente_deportiva = AlertaUrgente(tema = self.tema_deportes)
```
 
Estos son los objetos que nos encontraremos a lo largo de este proyecto, en las secciones siguientes voy a diseccionar un poco cada uno de ellos para hablar en profundidad de cada uno de sus metodos.

## class Usuario():
Como podemos ver, la clase se inicializa con un nombre de usuario y una contraseña, a su vez tambien tenemos dos atributos mas, *alertas_usuario*, corresponde a las alertas que tiene pendientes dicho usuario, *temas_usuario*, corresponde a los temas de interés del usuario.
Las ultimas dos lineas del metodo *init* comprueban si el usuario ya esta en la lista de usuarios, en caso de que aún no exista, lo agrega. 
```python
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.alertas_usuario = []
        self.temas_usuario = ['spam']
        if self not in lista_usuarios:
            lista_usuarios.append(self)
```

Esta función se encarga de agregar temas de interés para el usuario como lo vimos anteriormente.
```python
    def asigna_temas(self, tema):
        try:
            self.temas_usuario.append(tema)
            return 'Tema agregado'
        except Exception as e:
            return f'Ocurrio un problema: {e}'
```
Devuelve los temas de interés del usuario agregados con el metodo anterior.
```python
    def obtener_temas(self):
        return self.temas_usuario
```
Este metodo se utiliza para asignar alertas especificas para este usuario.
```python
    def asigna_alerta_unica(self, alerta):
        self.alertas_usuario.append(alerta)
```
Filtra las alertas dentro de *lista_alertas*, comprobando que no esten expiradas, que correspondan al tema de interes del usuario, y que no esten ya agregadas a la lista de alertas del usuario, de darse las 3 condiciones, agrega la alerta a la lista correspondiente.
```python
    def asigna_alertas(self):
        for alerta in lista_alertas:
            if datetime.now() < alerta.fecha_expiracion and alerta.tema in self.temas_usuario and alerta not in self.alertas_usuario:
                self.alertas_usuario.append(alerta)
            else:
                continue
```
Se utiliza para devolver las alertas aún no leídas, comienza creando una sub-lista que acabará siendo de ayuda para construir el diccionario que se enviará de respuesta.
Luego genera 3 listas para cada uno de los tipos de alertas ya mencionados, fijandose también que las mismas no esten vencidas.
Para finalizar, vacía la lista del comienzo y agrega las 3 anteriores ordenadas por fecha de expiración y genera un diccionario que envía como respuesta, el mismo contiene 3 keys que simbolizan cada una de las listas ordenadas.
```python
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
```

## class Tema():
Esta clase requiere que se le envie un string por parametro, a su vez se genera un diccionario con 3 keys que organizarán las diferentes alertas asignadas al tema.
```python
    def __init__(self, tema = None):
        self.tema = tema
        self.alertas = {'urgentes':[],'informativas':[],'spam':[]}
```
Este metodo es utilizado para clasificar las diferentes alertas asignadas a este tema y almacenarlas en un diccionario nativo de la clase.
```python
    def asigna_alertas_a_temas(self):
        for alerta in lista_alertas:
            if alerta.tema.__str__() == self.tema and alerta not in self.alertas and alerta.tipo_de_alerta == 'Informativa':
                self.alertas['informativas'].append(alerta)
            elif alerta.tema.__str__() == self.tema and alerta not in self.alertas and alerta.tipo_de_alerta == 'Urgente':
                self.alertas['urgentes'].append(alerta)
            elif alerta.tema.__str__() == self.tema and alerta not in self.alertas and alerta.tipo_de_alerta == 'Spam':
                self.alertas['spam'].append(alerta)
```
Este metodo lo podemos llamar al crear alertas nuevas, recorre la lista de usuarios y envia las alertas correspondientes a cada uno.
```python
    def asigna_alertas_a_usuarios(self):
        for usuario in lista_usuarios:
            usuario.asigna_alertas()
```
Este método es utilizado para retornar las alertas sin expirar correspondientes a un tema especifico.
```python
    def obtener_alertas(self):
        alertas_sin_leer_ni_expirar = {'urgentes':[],'informativas':[],'spam':[]}
        alertas_urgentes_sin_leer_ni_expirar =  [alerta for alerta in self.alertas['urgentes'] if alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_informativas_sin_leer_ni_expirar =  [alerta for alerta in self.alertas['informativas'] if alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_spam_sin_leer_ni_expirar =  [alerta for alerta in self.alertas['spam'] if alerta.alerta_leida == False and datetime.now() < alerta.fecha_expiracion]
        alertas_sin_leer_ni_expirar['urgentes'] = alertas_urgentes_sin_leer_ni_expirar
        alertas_sin_leer_ni_expirar['informativas'] = alertas_informativas_sin_leer_ni_expirar
        alertas_sin_leer_ni_expirar['spam'] = alertas_spam_sin_leer_ni_expirar
        return alertas_sin_leer_ni_expirar
```

## class Alerta(Tema):
Al crear una alerta desde la clase padre, la generaremos como tipo *'Spam'*, también de forma predeterminada tenemos un vencimiento a 1 dia y 10 horas posterior a la creación de las mismas.
Ademas de lo mencionado, se llaman dos metodos para asignar la alerta a la lista correspondiente en los temas y se la envia a los usuarios correspondientes.
Esta clase también hereda todos los metodos ya mencionados de la clase *Tema*
```python
    def __init__(self, tema = None, alerta_leida = False, tipo_de_alerta = 'Spam', fecha_expiracion = datetime.now() + timedelta(days=1, hours=10)):
        Tema.__init__(self, tema)
        self.alerta_leida = alerta_leida
        self.fecha_expiracion = fecha_expiracion
        self.tipo_de_alerta = tipo_de_alerta
        lista_alertas.append(self)
        self.asigna_alertas_a_temas()
        self.asigna_alertas_a_usuarios()
```
Se utiliza para obtener el tema al que pertenece la alerta.
```python
    def obtener_tema(self):
        return f'Esta alerta pertenece al tema: {self.tema.__str__()}'
```
Se utiliza para obtener la fecha de expiración de la alerta.
```python
    def obtener_fecha_expiracion(self):
        return self.fecha_expiracion
```
Se utiliza para obtener el tiempo hasta que expire la alerta.
```python
    def obtener_tiempo_hasta_que_expire(self):
        return self.fecha_expiracion - datetime.now()
```
Se utiliza para obtener el tipo al que pertenece la alerta.
```python
    def obtener_tipo_de_alerta(self):
        return self.tipo_de_alerta
```

## class AlertaInformativa(Alerta):

Esta clase hija, posee herencia multiple de la clase *Alerta* y de *Tema*, genera una Alerta como las ya vistas, solo que de tipo 'Informativa'
```python
    def __init__(self, tema = None, alerta_leida = False):
        Alerta.__init__(self, tema, alerta_leida, tipo_de_alerta = 'Informativa', fecha_expiracion = datetime.now() + timedelta(days=1, hours=10))
```

## class AlertaUrgente(Alerta):

Esta clase hija, posee herencia multiple de la clase *Alerta* y de *Tema*, genera una Alerta como las ya vistas, solo que de tipo 'Urgente'
```python
    def __init__(self, tema = None, alerta_leida = False):
        Alerta.__init__(self, tema, alerta_leida, tipo_de_alerta = 'Urgente', fecha_expiracion = datetime.now() + timedelta(days=1, hours=10))
```

# Testing
He escrito 3 archivos diferentes para testear cada una de las clases principales, *Usuario, Alerta, Tema*, se pueden ejecutar los mismos situandose en la carpeta *primera_parte_POO* y corriendo el comando:
```bash
python3 -m unittest
o
python3 -m unittest -v #Para un output mas descriptivo
```

## Ejercicio - SQL Query
Esta query nos realiza un inner join de dos tablas, y las filtra con las fechas comprendidas entre el año pasado y este, a su vez, el import de las ventas debe ser mayor a $100.000.

```SQL
SELECT C.id, C.nombre, C.apellido, V.fecha, V.importe FROM Clientes C
INNER JOIN Ventas V ON C.id = V.id_cliente
WHERE V.fecha BETWEEN '20220120' AND '20230120' AND V.importe > 100000;
```

# CONSIGNAS
## Ejercicio - Sistema de Alertas:
### Se pide programar un sistema para enviar alertas a usuarios que tenga la siguiente funcionalidad:

    1- Se pueden registrar usuarios que recibirán alertas. 

    2- Se pueden registrar temas sobre los cuales se enviarán alertas.

    3- Los usuarios pueden optar sobre cuales temas quieren recibir alertas.

    4- Se puede enviar una alerta sobre un tema y lo reciben todos los usuarios que han optado recibir alertas de ese tema.

    5- Se puede enviar una alerta sobre un tema a un usuario específico, solo lo recibe ese único usuario.

    6- Una alerta puede tener una fecha y hora de expiración. Las alertas que tienen expiración, no se muestran al usuario si han expirado.

    7- Hay dos tipos de alertas: Informativas y Urgentes.

    8- Un usuario puede marcar una alerta como leída.

    9- Se pueden obtener todas las alertas no expiradas de un usuario que aún no ha leído, ordenadas primero las Urgentes y luego las informativas de la más reciente a la más antigua.

    10- Se pueden obtener todas las alertas no expiradas para un tema (primero las Urgentes y luego las Informativas de la más reciente a la más antigua). Se informa para cada alerta si es para todos los usuarios o para uno específico.

### Aclaraciones importantes:

    1- La aplicación se ejecuta desde línea de comando. En ningún caso pedimos que escribas código de front end, tampoco que hagas impresiones a la consola.

    2- Debe tener Tests Unitarios.

    3- No debés hacer ningún tipo de persistencia de datos (base de datos, archivos). Todo debe resolverse con estructuras en memoria.

    4- Si tenés que hacer algún supuesto sobre algo que no esté claro en el ejercicio, por favor anotalo para que lo tengamos en cuenta al revisar el código.

## Ejercicio - SQL:

    Escribir una consulta SQL que traiga todos los clientes que han comprado en total más de 100,000$ en los últimos 12 meses usando las siguientes tablas: 
        
        1- Clientes: ID, Nombre, Apellido

        2- Ventas: Fecha, Sucursal, Numero_factura, Importe, Id_cliente
