# Calculadora-y-Graficadora-de-integrales-

opcion=0 

while True: 
    print ("""
    Bienvenido a la calculadora de integrales 
    ¿Que opcion desea usar?

    1)Calcular integral indefinida

    2)Calcular integral definida 

    3)Graficar integral metodo del trapecio 

    4)Graficar Integral metodo del trapecio definiendo el usuario los pasos 

    5)salir
    """)
    
    opcion=int(input("Introduce el numero aqui:"))

    if opcion==1:
        from sympy import *
        print(" ")

        f=input ("Ingrese la funcion f=")

        x=symbols('x')

        resultado1=integrate(f,x)

        print(f"la respuesta es {resultado1}")

    elif opcion==2:
        from sympy import *
        print (" ")
        print ("Integrales definidas")
        
        x=symbols('x')

        f=input("Ingrese la fuincion f= ")
        x1=input("Ingrese limite superior: ")
        x0=input("Ingrese limite inferior: ")
        
        resultado2=integrate (f,(x,x0,x1))
        print(f"el resultado es {resultado2}")

    elif opcion==3:
        from sympy import *
        print (" ")
        print ("Integrales definidas")
        
        x=symbols('x')

        f=input("Ingrese la fuincion f= ")
        x0=input("Ingrese limite superior: ")
        x1=input("Ingrese limite inferior: ")
        
        resultado2=integrate (f,(x,x0,x1))
       

        from tkinter import *
        from matplotlib.figure import Figure
        from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
        import numpy as np 
        from  matplotlib import style
        #ventana 
        win=Tk()
        win.geometry("1050x800")
        win.title("Graficador De Integrales")

        #Funcion para graficar 
        def graficador():
            fig=Figure(figsize=(5,15),dpi=120)
            plt1=fig.add_subplot(111)

            fun={"sin":"np.sin","cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","log":"np.log","pi":"np.pi"}
                    
            def fx(funcion,x):
                for i in fun:
                        if i in funcion:
                            funcion=funcion.replace(i,fun[i])
                return eval(funcion)
            #Recuperamos las expreciones para los demas botones
            a=int(inferior.get())
            b=int(superior.get()) 
            t=int(tramos.get())
            #le damos un punto x
            muestras=t+1

            #Calcular el Area de la Fuincion 
            h=(a-b)/t
            suma=0
            xi=a
            for i in range (0,t,1):
                areat=h*(fx(funcion.get(),xi)+fx(funcion.get(),xi+h))/2
                suma=areat
                xi+=h


            muestraslineas=muestras*10
            xk=np.linspace(a,b,muestraslineas)
            fk=fx(funcion.get(),xk)
            xi=np.linspace(a,b,muestras)
            fi=fx(funcion.get(),xi)

            plt1.fill_between(xi,0,fi,color="b")

            for i in range (0,muestras,1):
                plt1.axvline(xi[i],color="w")


            plt1.plot(xi,fi,"ro")

            plt1.plot(xk,fk)

            plt1.set_title(f"El area es:{resultado2}")
            


            cvs1=FigureCanvasTkAgg(fig,master=canvas)
            cvs1.get_tk_widget().pack(padx=240,pady=50)

            tlb=NavigationToolbar2Tk(cvs1,win)
            tlb.undate()
            cvs1.get_tk_widget().pack(side=TOP,fill=BOTH)

        #Botones:
        #Función 
        fun=Label(win,text="Función")
        fun.pack()
        fun.place(x=10,y=600)
        #entrada 
        funcion=Entry(win)
        funcion.pack()
        funcion.place(x=10, y=630)
                        
        #limite-inf 
        inf=Label (win, text="Lim.Inferior")
        inf.pack
        inf.place(x=200,y=600)
        inferior=Entry(win)
        inferior.pack()
        inferior.place(x=200,y=630)

        #limite-superior
        sup=Label (win, text="Lim.Superior")
        sup.pack
        sup.place(x=400,y=600)
        superior=Entry(win)
        superior.pack()
        superior.place(x=400,y=630) 
                        
        #Tramos
        tramo=Label (win, text="Tramos")
        tramo.pack
        tramo.place(x=600,y=600)
        tramos=Entry(win)
        tramos.pack()
        tramos.place(x=600,y=630) 
                        
        #Canvas/Grafica 
        btn=Button(win,text="Graficar",bg="purple",command=graficador)
        btn.pack()
        btn.place(x=900,y=70)
        canvas=Canvas(win, width=1010,height=450,highlightbackground="green")
        canvas.pack(pady=100)


        win.mainloop()
    
    elif opcion==4:
        from math import *
        from matplotlib import pyplot
        from sympy import *
        import numpy as np

        def trapecio(n,x,y,Num_Trapecios):
            suma=0
            for i in range(1,n):#
                suma=suma+y[i]
            Rta=(x[n]-x[0])*(y[0]+2*suma+y[n])/(2*Num_Trapecios)##
            return Rta




        a = float(input("Valor de el intervalo inferior de la integral: "))
        b = float(input("Valor de el intervalo superior de la integral: "))
        t = int(input("¿Cantidad de puntos?:  "))
        #altura de los trapecios 
        h = (b-a)/t 



        xi= np.linspace(a,b,t+1)#
        yi=np.zeros(t+1)#


        x= np.linspace(a,b,t+1)#
        print("Valores que asume: ",x)
        y=np.zeros(t+1)#



        for i in range(0,t+1):#
            y[i]=float(input(f"El Valor de y{i}: "))

        Num_Trapecios=t-1



        respuesta=trapecio(t,x,y,t)
        print("Su integral es: ",respuesta)



        pyplot.axhline(0, 
        color="black")
        pyplot.axvline(0, 
        color="Black")


        pyplot.plot(x,y)
        pyplot.plot(xi,y,"ro")

        pyplot.show()





        #Grafica con trapecios dijando su area

        pyplot.plot(x,y)
        pyplot.plot(xi,y,"ro")
        pyplot.fill_between(xi,y,color='b')           
        #definir puntos en eje x
        for i in range(0,t-1,1):
            
            pyplot.axvline(xi[i], color='white')

        pyplot.show()
        
    elif opcion==5:
        break

