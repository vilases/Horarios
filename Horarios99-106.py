#Importar Modulos
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
import sqlite3 as SQL

#Variables
user=[]
password=[]

#Funcion Nula
def disable_event():
    pass

#Funcion para pasar la hora de str a dos int
def Hora(hora):
    a=hora.split(":")
    print (a)
    return a

#Funcion para establecer horario y generarlo
def Vuelta(diag,a,b,c):
    vuelta=[]
    try:
        f=int(c[0])
        e=int(c[1])
    
        dif=[]
        f1=""
        e1=""
        if f<= 24 and e<=60:
            f1=str(f)
            e1=str(e)
            d=f1+":"+e1
            if a=="106":
                if diag == "Nocturno":
                    
                    
                    if b=="IDA":
                        dif=[0,4,8,5,6,5,6,5,6,5,8,8]
                    if b=="VUELTA":
                        dif=[0,9,8,5,5,5,4,4,4,6,8,4]
                    if b=="REF":
                        dif=[0,4,8,5,6,5,6,5,6,5,8,8,5,9,8,5,5,5,4,4,4,6,8,4]
                if diag == "Sem Inv":
                    if b=="IDA":
                        dif=[0,4,11,7,7,7,7,7,10,7,17,14]
                    if b=="VUELTA":
                        dif=[0,9,15,5,7,7,4,4,3,8,9,4]
                    if b=="REF":
                        dif=[0,4,11,7,7,7,7,7,10,7,17,14,10,9,15,5,7,7,4,4,3,8,9,4]
                if diag == "Sab Ver":
                    if b=="IDA":
                        dif=[0,4,8,6,4,5,4,6,7,6,8,8]
                    if b=="VUELTA":
                        dif=[0,11,9,5,6,5,4,4,4,6,8,5]
                    if b=="REF":
                        dif=[0,4,8,6,4,5,4,6,7,6,8,8,5,11,9,5,6,5,4,4,4,6,8,5]
                if diag == "Sab Inv":
                    if b=="IDA":
                        dif=[0,5,10,6,6,7,6,8,10,6,14,13]
                    if b=="VUELTA":
                        dif=[0,9,12,5,8,6,4,4,4,6,9,4]
                    if b=="REF":
                        dif=[0,5,10,6,6,7,6,8,10,6,14,13,5,9,12,5,8,6,4,4,4,6,9,4]
                if diag == "Dom Ver":
                    if b=="IDA":
                        dif=[0,4,8,4,8,4,4,5,6,4,7,8]
                    if b=="VUELTA":
                        dif=[0,9,8,4,4,4,3,4,3,6,7,5]
                    if b=="REF":
                        dif=[0,4,8,4,8,4,4,5,6,4,7,8,5,9,8,4,4,4,3,4,3,6,7,5]
                if diag == "Dom Inv":
                    if b=="IDA":
                        dif=[0,5,8,5,7,5,6,6,8,6,11,10]
                    if b=="VUELTA":
                        dif=[0,9,9,5,6,5,4,4,4,6,7,5]
                    if b=="REF":
                        dif=[0,5,8,5,7,5,6,6,8,6,11,10,5,9,9,5,6,5,4,4,4,6,7,5]
                if diag == "Sem Ver":
                    if b=="IDA":
                
                        dif=[0,4,10,6,8,6,7,7,9,6,14,11]
                    if b=="VUELTA":
                
                        dif=[0,9,12,5,7,6,4,4,4,6,9,4]
                    if b=="REF":
               
                        dif=[0,4,10,6,8,6,7,7,9,6,14,11,10,9,12,5,7,6,4,4,4,6,9,4]
        
            if a=="99":
                if diag == "Nocturno":
                    if b=="IDA":
                        dif=[0,5,7,7,7,5,8,3,5,5,10]
                    if b=="VUELTA":
                        dif=[0,9,4,5,3,4,4,4,6,6,3]
                    if b=="REF":
                        dif=[0,5,7,7,7,5,8,3,5,5,10,5,9,4,5,3,4,4,4,6,6,3]
                if diag == "Sem Inv":
                    if b=="IDA":
                        dif=[0,5,7,14,10,8,11,5,8,7,17]
                    if b=="VUELTA":
                        dif=[0,12,6,5,4,7,4,5,8,8,3]
                    if b=="REF":
                        dif=[0,5,7,14,10,8,11,5,8,7,17,10,12,6,5,4,7,4,5,8,8,3]
                if diag == "Sab Inv":
                    if b=="IDA":
                        dif=[0,3,8,10,7,7,8,5,6,5,12]
                    if b=="VUELTA":
                        dif=[0,11,5,5,4,6,4,4,7,8,4]
                    if b=="REF":
                        dif=[0,3,8,10,7,7,8,5,6,5,12,5,11,5,5,4,6,4,4,7,8,4]
                if diag == "Sab Ver":
                    if b=="IDA":
                        dif=[0,3,8,10,7,7,6,5,5,4,10]
                    if b=="VUELTA":
                        dif=[0,13,4,6,3,4,4,4,7,7,3]
                    if b=="REF":
                        dif=[0,3,8,10,7,7,6,5,5,4,10,5,13,4,6,3,4,4,4,7,7,3]
                if diag == "Dom Ver":
                    if b=="IDA":
                        dif=[0,3,7,6,7,5,8,3,4,4,10]
                    if b=="VUELTA":
                        dif=[0,13,4,5,3,4,4,4,6,7,3]
                    if b=="REF":
                        dif=[0,3,7,6,7,5,8,3,4,4,10,5,13,4,5,3,4,4,4,6,7,3]
                if diag == "Dom Inv":
                    if b=="IDA":
                        dif=[0,3,8,8,7,5,8,4,4,4,10]
                    if b=="VUELTA":
                        dif=[0,11,4,5,4,4,4,4,6,6,3]
                    if b=="REF":
                        dif=[0,3,8,8,7,5,8,4,4,4,10,5,11,4,5,4,4,4,4,6,6,3]
                if diag == "Sem Ver":
                    if b=="IDA":
                
                        dif=[0,3,7,11,8,6,11,5,7,7,13]
                    if b=="VUELTA":
                
                        dif=[0,10,6,5,4,6,4,4,7,8,3]
                    if b=="REF":
                
                        dif=[0,3,7,11,8,6,11,5,7,7,13,8,10,6,5,4,6,4,4,7,8,3]
                
        else:
            pass
        
        
        if dif!=[]:
            for item in dif:
                f1=""
                e1=""
                d=""
                e=e+item
                if e>=60:
                    e=e-60
                    f=f+1
                if e<=9:
                    e1="0"+str(e)
                else:
                    e1=str(e)
                if f<=9:
                    f1="0"+str (f)
                else:
                    f1=str(f)
        
                d=f1+":"+e1
        
                vuelta.append(d)
        else:
            pass  
    except:
        pass
    return vuelta

#Funcion ventana principal   
def Paso2():
    
    #Funcion ventana que muestra el horario
    def Show(diag,a,b,c):
        
        cb0.delete(0,END)
        cb2.delete(0,END)
        cb1.delete(0,END)
        ent.delete(0,END)
        
        titulo=a+"  "+b
        d=[]
        hora=Hora(c)
        d=Vuelta(diag,a,b,hora)
        text=""
        if d!=[]:
            try:
                v2=Toplevel()
                v2.geometry("700x500")
                v2.title("Horarios")
                v2.resizable(False,False)
                v2.protocol("WM_DELETE_WINDOW", disable_event())
        
                frm2=Frame(v2,bg="green",height=500,width=700).pack(fill="both")
        
                lb=Label(v2,text=titulo,font=("Times",15,"underline"),bg="green").place(x=20,y=20)
   
                scr=scrolledtext.ScrolledText(v2,width=21,height=12,font=("Times",16,"bold"),wrap=WORD)
                scr.place(x=30,y=100)
                try:
                    if b=="REF":
                        if a=="99":
                            cont=0
                            while cont <11:
                                t=""
                                t=d[cont]+"---"+d[cont+11]
                                scr.insert(END,t+"\n")
                                cont+=1
                    
                        if a=="106":
                           cont=0
                           while cont <12:
                               t=""
                               t=d[cont]+"---"+d[cont+12]
                               scr.insert(END,t+"\n")
                               cont+=1
               
               
                    else:
            
                        for item in d:
                            scr.insert(END,item+"\n")
                            scr.yview(END)
                except:
                    messagebox.showerror("Error","Hora Invalida")
                
                but=Button(v2,text="Cerrar",command=lambda:v2.destroy()).place(x=350,y=900)
            except ValueError:
                pass
            
        else:
            messagebox.showerror("Error","Sin Datos")
                 
    v0.iconify()
    v1=Toplevel()
    v1.geometry("700x500")
    v1.title("Inicio")
    v1.resizable(False,False)
    v1.protocol("WM_DELETE_WINDOW", disable_event())
    
    frm1=Frame(v1,bg="blue",height=500,width=700).pack(fill="both")
    
    lbl0=Label(v1,text="Diag:",font=("Times",15),fg="blue",relief="ridge",borderwidth=10).place(x=30,y=30)
    
    lbl1=Label(v1,text="Linea:",font=("Times",15),fg="blue",relief="ridge",borderwidth=10).place(x=30,y=100)
    
    lbl2=Label(v1,text="Vuelta:",font=("Times",15),fg="blue",relief="ridge",borderwidth=10).place(x=30,y=170)
    
    lbl3=Label(v1,text="Hora:",font=("Times",15),fg="blue",relief="ridge",borderwidth=10).place(x=30,y=240)
    
    cb0=ttk.Combobox (v1,values=["Sem Inv","Sem Ver","Sab Inv","Sab Ver","Dom Inv","Dom Ver","Nocturno"],width=7,font=("Times",15))
    cb0.place(x=200,y=35)
    
    cb1=ttk.Combobox (v1,values=["99","106"],width=4,font=("Times",15))
    cb1.place(x=200,y=105)
    
    cb2=ttk.Combobox (v1,values=["IDA","VUELTA","REF"],width=8,font=("Times",15))
    cb2.place(x=200,y=175)
    
    ent=Entry(v1,width=5,font=("Times",15))
    ent.place(x=200, y=245)
    
    bot1=Button (v1,text="Cerrar",command=lambda:(v1.destroy(),v0.destroy())).place(x=400,y=450)
    
    btn2=Button (v1,text="Aceptar",command=lambda:Show(cb0.get(),cb1.get(),cb2.get(),ent.get())).place(x=30,y=450)
    
    Label(v1,text="by @aldopehablo",font=("Helvetica",5,"italic"),bg="blue").place(x=250,y=450)
#Funcion que toma los usuarios y contraseñas de la Base de Datos
 
def Usuario():
    global user
    global password
    
    bbdd = SQL.connect('bbdd.dat')

    cursor = bbdd.cursor()
    
    cursor.execute("""select * from empleados """)

    for tupla in cursor.fetchall():
        user.append(tupla[0])
        password.append(tupla[1])
    cursor.close()
    bbdd.close()

#Funcion que toma los valores del usuario y los verifica

def Control(a,b,us,pa):
    
    a=str(a)
    b=str(b)
    
    c=0
    bol=False
    for item in us:
        if a==item and b==pa[c]:
            messagebox.showinfo("Generador de Horario","Bienvenido")
            bol=True
            Paso2()
            entry.delete(0, END)
            entry1.delete(0, END)  
        if a==item and b!=pa[c]:
            messagebox.showerror("Error","Contraseña erronea")
            entry1.delete(0, END)  
            bol=True
        c+=1
        
    if bol==False:
          messagebox.showerror("Error","Usuario no existe")
          entry.delete(0, END)
          entry1.delete(0, END)       
          
    

Usuario()

#Ventana de acceso usuario/contraseña
v0=Tk()
v0.geometry("500x300")
v0.title("Generador de Horarios")
v0.minsize(700,500)
v0.maxsize(700,500)

frm0=Frame(v0,bg="red",height=700,width=500).pack(fill='both')

lbl0=Label(frm0,text="Usuario:",bg="grey",fg="white",font=("Times",12),relief="ridge",borderwidth=6).place(x=50,y=50)

lbl1=Label(frm0,text="Contraseña: ",bg="grey",fg="white",font=("Times",12),relief="ridge",borderwidth=6).place(x=50,y=150)

entry = Entry(frm0,width=10,font=("Times",12))

entry.place(x=200, y=50)

entry1 = Entry(frm0,width=10,font=("Times",12),show="*")

entry1.place(x=200, y=150)

btn=Button(frm0,text="Aceptar",command=lambda:Control(entry.get(),entry1.get(),user,password),borderwidth=5).place(x=200,y=250)

btn1=Button(v0,text="Cerrar",command=lambda:v0.destroy(),borderwidth=5).place(x=200,y=350)

Label(v0,text="by @aldopehablo",font=("Helvetica",7,"italic"),bg="red").place(x=200,y=450)
v0.mainloop()


