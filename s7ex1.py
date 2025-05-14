'''exo1'''

from tkinter import Tk, Canvas, Button
from random import *
import numpy as np

root = Tk()
root.title("graphe")

largeur = 720
hauteur = 720
    
canvas = Canvas(root, width=largeur,height=hauteur,bg='ivory')
canvas.grid(column=largeur,row=hauteur)


graph=[[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
vitesse = np.array([((random()-0.5)*10, (random()-0.5)*10) for i in range(len(graph))])
position = np.array([(random()*largeur*0.9, random()*hauteur*0.9) for elmt in range(len(graph))])



def drawgraph(graph):
    canvas.delete("all")
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            canvas.create_line(position[i][0], position[i][1], position[j][0], position[j][1])
    for i, (x, y) in enumerate(position):
        canvas.create_oval(x-10,y-10,x+10,y+10,fill="#f3e1d4")
        canvas.create_text(x,y,text=str(i),fill="black", font=("Arial", 10))


'''exo2'''


def force(position):
    forces = np.zeros_like(position)
    
    for i in range(len(graph)):
        for j in graph[i]:
            vectij=position[i]-position[j]
            distij=np.linalg.norm(vectij)+1e-5
            k=10
            force_normale=k*vectij/distij
            forces[i]-=force_normale
            forces[j]+=force_normale
            
        repulsion = 2000
    for i in range(len(position)):
        for j in range( len(position)):
            if i==j:
                continue
            vect = position[i] - position[j]
            dist = np.linalg.norm(vect) + 1e-5
            rep_force = repulsion * vect / (dist ** 3)
            forces[i] += rep_force
    return forces
            
def update(event):
    global position, vitesse
    f = force(position)  
    frottements=-0.9 * vitesse 
    f+=frottements
    position += vitesse*0.8     
    for i in range(len(position)):
        x, y = position[i]
        if x <= 10:
            position[i][0] = 10
            vitesse[i][0] *= -0.5 
        elif x >= largeur - 10:
            position[i][0] = largeur - 10
            vitesse[i][0] *= -0.5
        if y <= 10:
            position[i][1] = 10
            vitesse[i][1] *= -0.5
        elif y >= hauteur - 10:
            position[i][1] = hauteur - 10
            vitesse[i][1] *= -0.5
    drawgraph(graph)


drawgraph(graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]])    
            
            
root.bind("f", update)
root.mainloop()            
            
