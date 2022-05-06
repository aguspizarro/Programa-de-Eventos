from cursor_del_pool import CursorDelPool
from evento import Evento
from logger_base import log


class EventoDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM evento ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO evento(nombre, fecha, hora, id_persona) VALUES (%s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE evento SET nombre=%s, fecha=%s, hora=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM evento WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            eventos = []
            for registro in registros:
                evento = Evento(registro[0], registro[1], registro[2], registro[3])
                eventos.append(evento)
            return eventos

    @classmethod
    def insertar(cls, evento):
        with CursorDelPool() as cursor:
            valores = (evento.nombre, evento.fecha, evento.hora, evento.id_persona)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Evento insertado: {evento}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, evento):
        with CursorDelPool() as cursor:
            valores = (evento.nombre, evento.fecha, evento.hora, evento.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Evento actualizado: {evento}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, evento):
        with CursorDelPool() as cursor:
            valores = (evento.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Evento eliminado: {evento}')
            return cursor.rowcount