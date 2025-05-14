from tkinter import Tk, Canvas, Button, Text
import random 



T = [2, 1, 1, 0, 2]
n = 4


root = Tk()
root.title("ligne")
    
canvas = Canvas(root, width=300,height=400,bg='ivory')
canvas.grid(column=3,row=400)

couleurs=['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'brown', 'magenta']


text_T = Text(root, height=0)
text_T.grid(row=1, column=3)
text_T.insert("1.0", f"Liste T : {T}\n")  


def read_word(canvas, mot, h, w, y, color):
    x=0
    
    for lettre in mot:
        if lettre == 'H':
            x1,y1 = x+h,y
        elif lettre == 'U':
            x1,y1 = x+w,y-h
        elif lettre == 'D' :
            x1,y1 = x+w,y+h
        else:
            continue
        
        canvas.create_line(x, y, x1, y1, fill=color, width=2)
        
        x,y=x1,y1
 
'''
        
mot='HUHHDUH'        
read_word(canvas,mot , 15, 10)

'''

def retourner_mot(T,n):
    R= ['H']*n
    fils={i: i for i in range(n)}
   
    for i in range(len(T)):
        for j in range(n):
            if j==fils[T[i]]:
                R[j]+= 'DH'
            elif j==fils[T[i]+1]:
                R[j]+= 'UH'
            else :
                R[j]+='HH'
                
        fils[T[i]],fils[T[i]+1]=fils[T[i]+1],fils[T[i]]
        
    for i in range(n):
        read_word(canvas,R[i] , 20, 20,150+20*i,color=couleurs[i % len(couleurs)])
    return R
        

def quitter():
    canvas.destroy()

    
def permuter():  
    R=retourner_mot(T,n)
    random.shuffle(couleurs)
    canvas.delete("all")
    for i in range(len(R)):
        read_word(canvas, R[i], 20, 20, 150 + 20 * i, color=couleurs[i % len(couleurs)])
        


btn_quitter = Button(root, text="Quitter", command=quitter)
btn_quitter.grid(row=1, column=0)

btn_couleurs = Button(root, text="Permuter Couleurs", command=permuter)
btn_couleurs.grid(row=1, column=1)


print(retourner_mot(T , n))
root.mainloop()
