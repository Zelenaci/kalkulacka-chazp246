import tkinter as tk
from tkinter import ANCHOR, Frame, messagebox, Listbox, END, ACTIVE
from os.path import basename, splitext
import math



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Vypočítátor 3000"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)        
        self.bind("<Return>", self.insert)

        self.var_field = tk.Variable()

        self.entry_field = tk.Entry(self, textvariable = self.var_field, width = 50)
        self.entry_field.grid(row = 1, column=1, columnspan = 2)
        
        self.listbox = Listbox(self, width = 50)
        self.listbox.grid(row = 2, column = 1, pady = 10, columnspan = 2)
        

        self.frame = Frame(self)
        self.frame.grid(row = 2, column = 3)
        self.btn_up = tk.Button(self.frame, text = "Up", command = self.up, width = 10, border = 3)
        self.btn_up.pack()
        self.btn_down = tk.Button(self.frame, text = "Down", command = self.down, width = 10, border = 3)
        self.btn_down.pack()

        self.btn_del = tk.Button(self, text = "Delete", command = self.del_zasobnik, width = 10, border = 3)
        self.btn_del.grid(row = 4, column = 1)
        

        self.btn_quit = tk.Button(self, text = "Quit", command = self.quit)
        self.btn_quit.grid(row = 4, column = 2)


        self.zasobnik = []
        self.dva_operandy = {}
        self.dva_operandy["+"] = lambda a, b: a + b
        self.dva_operandy["-"] = lambda a, b: a - b
        self.dva_operandy["*"] = lambda a, b: a * b
        self.dva_operandy["/"] = lambda a, b: a / b
        self.dva_operandy["//"] = lambda a, b: a // b
        self.dva_operandy["**"] = lambda a, b: a ** b

        self.jeden_operand = {}
        self.jeden_operand["sin"] = math.sin
        self.jeden_operand["cos"] = math.cos
        self.jeden_operand["tg"] = math.tan
        self.jeden_operand["tan"] = math.tan

    def insert(self, event = None):
        raw = self.var_field.get().split()
        if len(raw) == 0:
            pocet = 1
        else:
            pocet = len(raw)
        for i in range(0, pocet):
            if len(raw) == 0:
                messagebox.showerror("Žrádlo", "Tohle nežeru.")
            else:
                item = raw[i]
                if item == "":
                    messagebox.showerror("Žrádlo", "Tohle nežeru.")

                try:
                    self.zasobnik.append(float(item))
                except:
                    pass


                if item.upper() == "Q":
                    self.quit()
                if item.upper() == "PI":
                    self.listbox.insert(END, math.pi)
                    self.zasobnik.append(math.pi)
                if item in self.dva_operandy.keys():
                    if len(self.zasobnik) >= 2:
                        b = self.zasobnik.pop()
                        a = self.zasobnik.pop()
                        self.zasobnik.append(self.dva_operandy[item](a, b))
                        self.listbox.insert(END, self.dva_operandy[item](a, b))
                    else:
                        messagebox.showerror("Žrádlo", "Dal jsi mi toho málo mám ještě hlad.")
                
                if item in self.jeden_operand.keys():
                    if len(self.zasobnik) >= 1:
                        a = self.zasobnik.pop()
                        self.zasobnik.append(self.jeden_operand[item](a))
                        self.listbox.insert(END, self.jeden_operand[item](a))
                    else:
                        messagebox.showerror("Žrádlo", "Nedal jsi mi nic ty hulváte jeden.")
                self.listbox_reload()

    def listbox_reload(self):
        self.var_field.set("")
        self.listbox.delete(0, END)
        for item in self.zasobnik:
            self.listbox.insert(END, item)

    def up(self, event = None):
        if self.listbox.get(ACTIVE) != "":
            item = self.listbox.curselection()[0]
            self.zasobnik[item], self.zasobnik[item - 1] = self.zasobnik[item - 1], self.zasobnik[item]
            self.listbox_reload()
          
            self.listbox.selection_set(item - 1)
            self.listbox.activate(item - 1)
        else:
            messagebox.showerror("Výběr", "Nic jsi nevybral ňoumo.")

    def down(self, event = None):
        if self.listbox.get(ACTIVE) != "":
            item = self.listbox.curselection()[0]
            self.zasobnik[item], self.zasobnik[item + 1] = self.zasobnik[item + 1], self.zasobnik[item]
            self.listbox_reload()
          
            self.listbox.selection_set(item + 1)
            self.listbox.activate(item + 1)          
        else:
            messagebox.showerror("Výběr", "Nic jsi nevybral ňoumo.")

    def del_zasobnik(self):
        if self.listbox.get(ANCHOR) != "":
            item = self.listbox.curselection()[0]
            self.zasobnik.pop(item)
            self.listbox_reload()
        else:
            messagebox.showerror("Výběr", "Nic jsi nevybral ňoumo.")

    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()