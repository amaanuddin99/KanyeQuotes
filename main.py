import tkinter
import quotegen
window=tkinter.Tk()
window.minsize(500,700)
window.title("Kanye Quotes")
canvas=tkinter.Canvas(height=455,width=310)
bg=tkinter.PhotoImage(file="background.png")
kanye=tkinter.PhotoImage(file="kanye.png")
def genq():
    quote=quotegen.Quote().newq["quote"]
    canvas.itemconfig(quotetxt,text=quote)

    
quote=quotegen.Quote().newq["quote"]
canvas.create_image(160,250,image=bg)
quotetxt=canvas.create_text(160,230,width=250,text=quote,font=("Arial",19,"bold"),fill="white")


canvas.config(bg="black",highlightthickness=0)
canvas.place(x=80,y=0)

button=tkinter.Button(image=kanye,command=genq)
button.place(x=200,y=490)
window.config(bg="black")
window.mainloop()