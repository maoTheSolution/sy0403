import tkinter

window=tkinter.Tk()
app_x = 200
app_y = 200
x = str(window.winfo_screenwidth()//2 - app_x//2)
y = str(window.winfo_screenheight()//2 - app_y//2)
window.title("식단표")
window.geometry(str(app_x)+"x"+str(app_y)+"+"+x+"+"+y)
window.resizable(False, False)

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))
    print(entry.get().split(','))

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()