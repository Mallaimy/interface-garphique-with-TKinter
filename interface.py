from tkinter import Label, Tk
window = Tk()
mon_label1= Label(window, text="Bienvenu dans mon interface")
mon_label2= Label(window, text="Mon nom est Abakar Mahamat Mallah")
mon_label1.grid(row=0, column=0)
mon_label2.grid(row=1, column=0)
window.title("Mon interface")
window.geometry("720x360")
window.minsize(480, 360)
window.config(background='green')
window.mainloop()
