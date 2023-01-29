from tkinter import *

from transliterate import to_latin, to_cyrillic


def trans():
    try:
        if entry.get().isascii():
            result = to_cyrillic(entry.get())


        else:
            result = to_latin(entry.get())
    except Exception as e:
        print(e)
    else:
        text_widget.delete(1.0, END)
        text_widget.insert(END, result)


calc = Tk()
calc.geometry('690x500')
calc.title("LOTIN KRILL LOTIN")
calc.configure(background='yellow')
img = PhotoImage(file='file_path')
calc.iconphoto(False, img)

entry = Entry(background="white", width=50, font=20, borderwidth=5, takefocus=10)
entry.place(x=70, y=30)

button = Button(text="NATIJA:👇",width=30, command=trans, font=30,
                borderwidth=5, background="white", activebackground="red", activeforeground="white")

button.place(x=120, y=100)

text_widget = Text(calc)
text_widget.configure(state='normal')
text_widget.place(x=0, y=160)
text_widget.configure(background="white", font=20)


calc.mainloop()
