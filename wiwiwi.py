from tkinter import Tk
from tkinter import *
from Compte import*
from CompteCourant import*
from CompteEpargne import*
from tkinter import ttk
window = Tk()
window.config(background='pink')
window.geometry('800x900')
window.title("compt bancaire")

nombre = Label(window,text = "number: " , font=('arila',10,'italic'),bg='pink')
nombre.place( x=10 , y=10)

nbr = 0
num = Label(window, text= nbr)
num.place(x=100, y=10)

prop = Label(window,text= " propreiétaire: " , font=('arial',10,'italic'),bg='pink' )
prop.place( x=10 , y= 40 )
entreyprop = Entry(window)
entreyprop.place ( x=100 , y=40 , width=200)

solde  = Label(window , text= "solde initial: "  , font=('arial',10,'italic'),bg='pink')
solde.place( x=10 , y= 70)
euro = Label(window , text="Euro € " , font=('arial',10,'italic'),bg='pink')
euro.place( x= 300 , y= 70)
entrysold = Entry(window)
entrysold.place( x= 100 , y= 70 , width=200)

account_type_var = StringVar()
account_type_var.set("courant espargne")
def desactive():
    account_type = account_type_var.get()
    if account_type == "courant":
        entry_taux .config(state = NORMAL)
        entrymdec.config(state=DISABLED)
    else :
        entry_taux.config(state= DISABLED)
        entrymdec.config(state=NORMAL)



typ = Label(window, text="type : " , font=('arial',10,'italic'),bg='pink')
typ.place(x = 10 , y=100)
courant = Radiobutton(window, text="Courant",value= "courant" , variable= account_type_var , command= desactive , font=('arial',10,'italic'),bg='pink')
courant.place(x=90 ,y= 100)
epargne = Radiobutton(window, text="Epargne" , value="epargne",width=30 , variable= account_type_var ,command=desactive , font=('arial',10,'italic'),bg='pink')
epargne.place(x=140 ,y= 100)

taux_interet = Label(window , text="taut intéret : " , font=('arial',10,'italic'),bg='pink')
taux_interet.place( x = 10 , y= 140)
entry_taux = Entry(window)
entry_taux.place(x=100 , y=140 , width= 200)

Mdec = Label(window , text="M.decouvert : " , font=('arial',10,'italic'),bg='pink' )
Mdec.place(x=10 , y=180)
entrymdec = Entry(window)
entrymdec.place(x=100 , y=180 , width=200)




tree = ttk.Treeview(window , columns=('numéro','propriétaire', 'solde' , 'type' ,'taux', 'montant'))


tree.column("#0", width=120, minwidth=25)  # invisible first column
tree.column("numéro",anchor=W,  width=120)
tree.column("propriétaire",anchor=CENTER,  width=120)
tree.column("solde",anchor=W, width=100)
tree.column("type",anchor= CENTER, width=100)
tree.column("taux", width=100)
tree.column("montant",  width=100)

tree.heading('numéro', text="numéro")
tree.heading('propriétaire', text="propriétaire" , anchor=W)
tree.heading('solde', text="solde", anchor=W)
tree.heading('type', text="type", anchor=W)
tree.heading('taux', text="taux", anchor=W)
tree.heading('montant', text="montant", anchor=W)

tree.place( x= 20 ,y=280)

def click():
   global nbr
   nbr = nbr+1
   num.config(text=nbr)
   prop = entreyprop.get()
   solde = entrysold.get()
   typ = account_type_var.get()
   taux = entry_taux.get()
   montant = entrymdec.get()
   tree.insert("","end",values=(nbr , prop , solde , typ , taux, montant))
    


button = Button(window , text="création du compt",  font=('arial',10,'italic'),bg='#D97CF7',
                activebackground='#9975A5',
                activeforeground='#E0C7E8',
                command=click)
button.place(x=100 , y=250)











window.mainloop()