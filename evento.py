class Evento:
    def __init__(self, nombre, fecha, hora, id_persona):
        self._nombre = nombre
        self._fecha = fecha
        self._hora = hora
        self._id_persona = id_persona

    def __str__(self):
        return f'''
            Nombre del evento: {self._nombre}, Fecha: {self._fecha}, Hora: {self._hora}, Organizador: {self._id_persona}
        '''

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):
        self._hora = hora

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona
