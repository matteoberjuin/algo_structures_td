from tkinter import Tk, Canvas, Button
from random import *

class Data:
    def __init__(self, nombre_fils, desc_entrelacement):
        self.nombre_fils = nombre_fils
        self.desc_entrelacement = desc_entrelacement

    def retourner_mot(self):
        R = ['H'] * self.nombre_fils
        fils = {i: i for i in range(self.nombre_fils)}

        for t in self.desc_entrelacement:
            for j in range(self.nombre_fils):
                if j == fils[t]:
                    R[j] += 'DH'
                elif j == fils[t + 1]:
                    R[j] += 'UH'
                else:
                    R[j] += 'HH'
            fils[t], fils[t + 1] = fils[t + 1], fils[t]

        return R
    
    def randomize(self):
        self.nombre_fils=randint(2,15)
        self.desc_entrelacement=[randint(0,self.nombre_fils-2) for elmt in range(10)]



class App:
    def __init__(self, data):
        self.root = Tk()
        self.root.title("ligne")
        self.canvas = Canvas(self.root, width=300, height=400, bg='ivory')
        self.canvas.grid(column=0, row=0)
        self.data = data  
        bouton = Button(self.root, text="randomiser", command=self.randomize) 
        bouton.grid(column=1,row=0,sticky='nw')

    def read_word(self, mot, h, w, y):
        x = 0
        for lettre in mot:
            if lettre == 'H':
                x1, y1 = x + h, y
            elif lettre == 'U':
                x1, y1 = x + w, y - h
            elif lettre == 'D':
                x1, y1 = x + w, y + h
            else:
                continue
            self.canvas.create_line(x, y, x1, y1, fill='black', width=2)
            x, y = x1, y1

    def redraw(self):
        self.canvas.delete("all")
        mots = self.data.retourner_mot() 
        for i, mot in enumerate(mots):
            self.read_word(mot, 20, 20, 150 + 20 * i)

    def run_forever(self):
        self.redraw()
        self.root.mainloop()

    def randomize(self):
        self.data.randomize()
        self.redraw()
        



if __name__ == "__main__":
    nb_fils = randint(2,10)
    description = [randint(0,nb_fils-1) for elmt in range(nb_fils)]
    data = Data(nb_fils, description) 
    app = App(data)
    app.run_forever()
