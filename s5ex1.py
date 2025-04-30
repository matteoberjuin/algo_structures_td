from tkinter import Tk, Canvas, Button

root = Tk()
root.title("ligne")
    
canvas = Canvas(root, width=300,height=400,bg='ivory')
canvas.grid(column=300,row=400)



def read_word(canvas, mot, h, w, y):
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
        
        canvas.create_line(x, y, x1, y1, fill='black', width=2)
        
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
        read_word(canvas,R[i] , 20, 20,150+20*i)
    return R
        

print(retourner_mot([2, 1, 1, 0, 2] , 4))
root.mainloop()
