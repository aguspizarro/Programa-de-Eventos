from tkinter import *
from tkcalendar import DateEntry
from tktimepicker import AnalogPicker, SpinTimePickerOld


menu = Tk()
menu.title('Programa para eventos')


canvas = Canvas(menu, height=400, width=500)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# para agregar un texto
label = Label(frame, text='Programa para eventos')
label.grid(row=0, column=1)

cal = DateEntry(menu, width=12, year=2019, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)



menu.mainloop()