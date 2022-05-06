import tkinter.ttk
from tkinter import *
from persona import Persona
from persona_dao import PersonaDAO
from logger_base import log
from evento import Evento
from evento_dao import EventoDAO
from tkcalendar import DateEntry
from tktimepicker import AnalogPicker

menu = Tk()
menu.title('Programa para eventos')


canvas = Canvas(menu, height=400, width=500)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# para agregar un texto
label = Label(frame, text='Programa para eventos')
label.grid(row=0, column=1)


# Todo para el organizador


def save_new_org(name, apellido, email):
    persona = Persona(nombre=name, apellido=apellido, email=email)
    personas_insertadas = PersonaDAO.insertar(persona)
    log.info(f'Personas insertadas: {personas_insertadas}')


def save_edit_org(id, name, apellido, email):
    persona = Persona(nombre=name, apellido=apellido, email=email, id_persona=id)
    personas_actualizadas = PersonaDAO.actualizar(persona)
    log.info(f'Personas actualizadas: {personas_actualizadas}')
    lista_organizadores()


def new_organizador():
    new_organizador = Toplevel()
    new_organizador.title('Agregar un nuevo organizador')
    new_organizador.geometry('400x300')

    label = Label(new_organizador, text='Agregar a un nuevo organizador')
    label.grid(row=1, column=1)

    # input nombre
    label = Label(new_organizador, text='Nombre')
    label.grid(row=2, column=0)
    entry_name = Entry(new_organizador)
    entry_name.grid(row=2, column=1)

    # input apellido
    label = Label(new_organizador, text='Apellido')
    label.grid(row=3, column=0)
    entry_apellido = Entry(new_organizador)
    entry_apellido.grid(row=3, column=1)

    # input email
    label = Label(new_organizador, text='Email')
    label.grid(row=5, column=0)
    entry_email = Entry(new_organizador)
    entry_email.grid(row=5, column=1)

    button = Button(new_organizador, text='Agregar organizador', command=lambda: save_new_org(
        entry_name.get(),
        entry_apellido.get(),
        entry_email.get()
    ), foreground='darkslateblue', activeforeground='darkred')
    button.grid(row=6, column=1, sticky=W + E)


def eliminar_org(tabla):
    try:
        tabla.item(tabla.selection())['text']
    except IndexError as e:
        f'A ocurrido el siguiente error: {e}'
        return
    id = tabla.item(tabla.selection())['text']
    persona = Persona(id_persona=id)
    PersonaDAO.eliminar(persona)
    lista_organizadores()


def editar_org(tabla):
    editar_organizadores = Toplevel()
    editar_organizadores.title('Edición de una persona')
    editar_organizadores.geometry('400x300')

    label = Label(editar_organizadores, text='Edición de una persona')
    label.grid(row=0, column=0)

    # input nombre
    label = Label(editar_organizadores, text='Nuevo Nombre')
    label.grid(row=2, column=0)
    entry_name = Entry(editar_organizadores)
    entry_name.grid(row=2, column=1)

    # input apellido
    label = Label(editar_organizadores, text='Nuevo Apellido')
    label.grid(row=3, column=0)
    entry_apellido = Entry(editar_organizadores)
    entry_apellido.grid(row=3, column=1)

    # input email
    label = Label(editar_organizadores, text='Nuevo Email')
    label.grid(row=5, column=0)
    entry_email = Entry(editar_organizadores)
    entry_email.grid(row=5, column=1)

    try:
        tabla.item(tabla.selection())['text']
    except IndexError as e:
        f'A ocurrido el siguiente error: {e}'
        return
    id = tabla.item(tabla.selection())['text']
    persona = Persona(id_persona=id)
    PersonaDAO.actualizar(persona)

    button = Button(editar_organizadores, text='Guardar cambios', command=lambda: save_edit_org(
        id,
        entry_name.get(),
        entry_apellido.get(),
        entry_email.get()
    ), foreground='darkslateblue', activeforeground='darkred')
    button.grid(row=6, column=1, sticky=W + E)


def lista_organizadores():
    lista_organizadores = Toplevel()
    lista_organizadores.title('Lista de organizadores')
    lista_organizadores.geometry('800x230')

    label = Label(lista_organizadores, text='Lista de organizadores')
    label.grid(row=0, column=0)

    tabla = tkinter.ttk.Treeview(lista_organizadores, height=6, columns=('#0', '#1', '#2', '#3'))
    tabla.grid(row=2, column=0, columnspan=1)
    tabla.heading('#0', text='Id', anchor=CENTER)
    tabla.heading('#1', text='Nombre', anchor=CENTER)
    tabla.heading('#2', text='Apellido', anchor=CENTER)
    tabla.heading('#3', text='Email', anchor=CENTER)

    records = tabla.get_children()
    for element in records:
        tabla.delete(element)

    personas = PersonaDAO.seleccionar()
    for persona in personas:
        tabla.insert(parent="", index=0, text=persona.id_persona,
                 values=(persona.nombre, persona.apellido, persona.email))

    button1 = Button(lista_organizadores, text='Editar', command=lambda: editar_org(tabla),
                     foreground='darkslateblue', activeforeground='darkred')
    button1.place(x=0.5, y=180, width=400, height=30)
    button2 = Button(lista_organizadores, text='Eliminar', command=lambda: eliminar_org(tabla),
                     foreground='darkslateblue', activeforeground='darkred')
    button2.place(x=400, y=180, width=400, height=30)


# Todo para el evento
def save_new_event(name, fecha, hora, id_persona):
    evento = Evento(nombre=name, fecha=fecha, hora=hora, id_persona=id_persona)
    eventos_insertados = EventoDAO.insertar(evento)
    log.info(f'Eventos insertados: {eventos_insertados}')


def save_edit_event(id, name, fecha, hora):
    evento = Evento(nombre=name, fecha=fecha, hora=hora, id_persona=id)
    eventos_actualizados = EventoDAO.actualizar(evento)
    log.info(f'Eventos actualizados: {eventos_actualizados}')
    lista_eventos()


def selected2(time_picker, new_evento3):
    myTime = time_picker.time()
    mensa = Label(new_evento3, text='Escriba la hora elegida en el formulario')
    mensa.place(x=140, y=350)
    selected = Label(new_evento3, text=myTime)
    selected.place(x=205, y=370)


def time():
    new_evento3 = Toplevel()
    new_evento3.title('Para agregar la hora')
    new_evento3.geometry('400x500')
    time_picker = AnalogPicker(new_evento3)
    time_picker.place(x=10, y=20)

    button = Button(new_evento3, text='Seleccionar hora', command=lambda: selected2(time_picker, new_evento3))
    button.place(x=10, y=370)


def new_evento():
    new_evento = Toplevel()
    new_evento.title('Agregar un nuevo evento')
    new_evento.geometry('400x300')

    label = Label(new_evento, text='Agregar un nuevo evento')
    label.grid(row=1, column=1)

    # input nombre del evento
    label = Label(new_evento, text='Nombre del evento')
    label.grid(row=2, column=0)
    entry_name = Entry(new_evento)
    entry_name.grid(row=2, column=1)

    # input fecha
    label = Label(new_evento, text='Fecha')
    label.grid(row=3, column=0)
    entry_fecha = DateEntry(new_evento, width=12, day=31, month=8, year=2021, background='darkblue', foreground='white', borderwidth=2)
    entry_fecha.grid(row=3, column=1)

    # input hora
    label = Label(new_evento, text='Hora')
    label.grid(row=4, column=0)
    entry_hora = Entry(new_evento)
    entry_hora.grid(row=4, column=1)

    openClock = Button(new_evento,  text="Para seleccionar la hora", command=lambda: time())
    openClock.grid(row=4, column=2)

    # input organizador
    label = Label(new_evento, text='Organizador')
    label.grid(row=5, column=0)
    entry_id_persona = Entry(new_evento)
    entry_id_persona.grid(row=5, column=1)

    list = Listbox(new_evento, width=20, height=5)
    personas = PersonaDAO.seleccionar()
    for index, persona in enumerate(personas):
        list.insert(index, persona.id_persona)
        list.grid(row=5, column=2)

    button = Button(new_evento, text='Agregar evento', command=lambda: save_new_event(
        entry_name.get(),
        entry_fecha.get(),
        entry_hora.get(),
        entry_id_persona.get()
    ), foreground='darkslateblue', activeforeground='darkred')
    button.grid(row=6, column=1, sticky=W + E)


def editar_evento(tabla):
    editar_evento = Toplevel()
    editar_evento.title('Edición de un evento')
    editar_evento.geometry('400x300')

    label = Label(editar_evento, text='Edición de un evento')
    label.grid(row=0, column=0)

    # input nombre del evento
    label = Label(editar_evento, text='Nombre del evento')
    label.grid(row=2, column=0)
    entry_name = Entry(editar_evento)
    entry_name.grid(row=2, column=1)

    # input fecha
    label = Label(editar_evento, text='Fecha')
    label.grid(row=3, column=0)
    entry_fecha = Entry(editar_evento)
    entry_fecha.grid(row=3, column=1)

    # input hora
    label = Label(editar_evento, text='Hora')
    label.grid(row=4, column=0)
    entry_hora = Entry(editar_evento)
    entry_hora.grid(row=4, column=1)


    try:
        tabla.item(tabla.selection())['text']
    except IndexError as e:
        f'A ocurrido el siguiente error: {e}'
        return
    id = tabla.item(tabla.selection())['text']
    evento = Evento(id_persona=id, nombre='', fecha='', hora='')
    EventoDAO.actualizar(evento)

    button = Button(editar_evento, text='Guardar cambios', command=lambda: save_edit_event(
        id,
        entry_name.get(),
        entry_fecha.get(),
        entry_hora.get()
    ), foreground='darkslateblue', activeforeground='darkred')
    button.grid(row=6, column=1, sticky=W + E)


def eliminar_evento(tabla):
    try:
        tabla.item(tabla.selection())['text']
    except IndexError as e:
        f'A ocurrido el siguiente error: {e}'
        return
    id = tabla.item(tabla.selection())['text']
    evento = Evento(id_persona=id, nombre='', fecha='', hora='')
    EventoDAO.eliminar(evento)
    lista_eventos()


def lista_eventos():
    lista_eventos = Toplevel()
    lista_eventos.title('Lista de eventos')
    lista_eventos.geometry('800x230')

    label = Label(lista_eventos, text='Lista de eventos')
    label.grid(row=0, column=0)

    tabla = tkinter.ttk.Treeview(lista_eventos, height=6, columns=('#0', '#1', '#2', '#3'))
    tabla.grid(row=2, column=0, columnspan=1)
    tabla.heading('#0', text='Organizador', anchor=CENTER)
    tabla.heading('#1', text='Nombre del evento', anchor=CENTER)
    tabla.heading('#2', text='Fecha', anchor=CENTER)
    tabla.heading('#3', text='Hora', anchor=CENTER)

    records = tabla.get_children()
    for element in records:
        tabla.delete(element)

    eventos = EventoDAO.seleccionar()
    for evento in eventos:
        tabla.insert(parent="", index=0, text=evento.id_persona,
                     values=(evento.nombre, evento.fecha, evento.hora))

    button1 = Button(lista_eventos, text='Editar', command=lambda: editar_evento(tabla),
                     foreground='darkslateblue', activeforeground='darkred')
    button1.place(x=0.5, y=180, width=400, height=30)
    button2 = Button(lista_eventos, text='Eliminar', command=lambda: eliminar_evento(tabla),
                     foreground='darkslateblue', activeforeground='darkred')
    button2.place(x=400, y=180, width=400, height=30)
# Botones


button = Button(frame, text='Lista de organizdores', command=lambda: lista_organizadores(),
                foreground='darkslateblue', activeforeground='darkred')
button.grid(row=3, column=1, sticky=W+E)

button2 = Button(frame, text='Agregar un nuevo organizador', command=lambda: new_organizador(),
                 foreground='darkslateblue', activeforeground='darkred')
button2.grid(row=4, column=1, sticky=W+E)

butto3 = Button(frame, text='Lista de eventos', foreground='darkslateblue', command=lambda: lista_eventos(),
                activeforeground='darkred')
butto3.grid(row=3, column=2, sticky=W+E)

button4 = Button(frame, text='Agregar un nuevo evento', foreground='darkslateblue', command=lambda: new_evento(),
                 activeforeground='darkred')
button4.grid(row=4, column=2, sticky=W+E)


menu.mainloop()