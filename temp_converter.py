import tkinter as ttk

stone = ttk.Tk()
stone.title("Temp Converter")
stone.geometry("500x400")

a = ttk.StringVar()
e1 = ttk.Entry(master=stone, textvar=a)
e1.place(x=50, y=100)

l1 = ttk.Label(master=stone, text='Celsius')
l1.place(x=150, y=100)

def convert_to_farenheit():
    celsius = float(a.get())
    faren = (celsius*1.8) + 32
    bvar.set(str(faren))

b1 = ttk.Button(master=stone, text="DO SOMETHING", command=convert_to_farenheit)
b1.place(x=100, y=200)

bvar = ttk.StringVar()
#ans1 = ttk.Label(stone, textvar=bvar)
#ans1.place(x=100, y=300)
e2 = ttk.Entry(stone, textvar=bvar)
e2.place(x=50, y=300)

l2 = ttk.Label(stone, text="Farenheit")
l2.place(x=150, y=300)

stone.mainloop()
