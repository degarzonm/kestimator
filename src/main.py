from os import name
import tkinter as tk
from tkinter import Label, XView, filedialog
from tkinter.constants import COMMAND
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import csv
import KDE

class Application(tk.Frame):
  
        
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.createWidgets()

    def createWidgets(self):
        global lam
        root.title("Kernel Density Estimation")
        
        fig = Figure(figsize=(7,7), dpi=100)
        
        ax=fig.add_axes([0.1,0.06,0.85,0.85])
        

        lienzo = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        lienzo.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4,
                                    padx=5)
        lienzo.draw()
        toolbarFrame = tk.Frame(master=root)
        toolbarFrame.grid(row=5, column=0)
        toolbar = NavigationToolbar2Tk(lienzo, toolbarFrame)
        toolbar.update()

        self.titulos=tk.Label(master=root, text="Estimador de densidad con Kernel", font = "Helvetica 16 bold")
        self.titulos.grid(sticky=tk.E, pady=4, padx=5)

        boton_archivo = tk.Button(master=root, text="archivo CSV", command=lambda: self.selectorArchivo())
        boton_archivo.grid(row=1, column=3,sticky=tk.E+tk.W+tk.S+tk.N)

        boton_graficar=tk.Button(master=root, text="Graficar", command=lambda: self.graficar(lienzo,ax))
        boton_graficar.grid(row=2, column=3, pady=4,sticky=tk.E+tk.W+tk.S+tk.N)

        boton_dataset_alea=tk.Button(master=root,text="Dataset Aleatorio",command=lambda: self.datasetGenerado(lienzo,ax))
        boton_dataset_alea.grid(row=3,column=3,pady=4,sticky=tk.E+tk.W+tk.S+tk.N)

        boton_kde=tk.Button(master=root, text="KDE",command=lambda: self.KDEPlotter(lienzo,ax))
        boton_kde.grid(row=4, column=3,pady=4,sticky=tk.E+tk.W+tk.S+tk.N)
        
        lam = tk.Scale(master=root, from_=0, to=10,digits=3,resolution=0.001)
        lam.grid(row=4, column=4,sticky=tk.S+tk.N)


    #cargamos el dataset en un csv globlal 
    def selectorArchivo(self):
        global np_dataset,nombres_data,datos_1
        self.filename = filedialog.askopenfilename(initialdir="/datasets", title="Seleccione el archivo de datos separado por coma",filetypes=(("archivos csv","csv"),("todos","*")))
       # texto_ruta_csv= Label(root , text= self.filename).grid(row=4, column=3,pady=4)
        np_dataset = np.genfromtxt(self.filename,delimiter=',',names=True,encoding="utf-8")
        nombres_data=np_dataset.dtype.names
        datos_1=np.array(np_dataset[nombres_data[0]])
        print("dataset cargado:")
        #print(np_dataset)
        print(type(np_dataset), "and names", nombres_data)
    
    def graficar(self,lienzo,ax):
        ax.clear()

        x=np.array(np_dataset[nombres_data[0]])
        y=np.array(np_dataset[nombres_data[1]])
       
        ax.scatter(x,y)
        #ax.scatter(np.arange(len(y)),y)
        
        print("pintando datos, hay ",len(y)," datos")
        lienzo.draw()

    #Botón de generación de datos
    def datasetGenerado(self, canvas, ax):
        global datos_1
        tam=56
        c = ['r','b','g']  # plot marker colors
        ax.clear()         # clear axes from previous plot

        y1 = np.zeros(tam)
        #x1 = np.random.normal(1,1,tam)
        x1 = np.random.uniform(0,35,tam)
        y2 = np.array([0.5 for x in range(tam)])
        x2 = np.random.normal(7,4,tam)
        #x2=np.random.uniform(0,35,tam)
        datos_1=np.append(x1,x2)

        ax.eventplot(x1,colors=c[0],lineoffsets=0.2,linelengths=0.05)
        ax.eventplot(x2,colors=c[1],lineoffsets=0.3,linelengths=0.05)
        ax.eventplot(datos_1,colors=c[2],lineoffsets=0,linelengths=0.1)
        canvas.draw()
    
    def KDEPlotter(self,lienzo,ax):
        
        x_0=np.linspace(datos_1.min(),datos_1.max(),100)
        print(x_0)
        y=[KDE.estimador(1,x,datos_1,lam.get()) for x in x_0]
        ax.plot(x_0,y,color='r')
        lienzo.draw()


root=tk.Tk()
app=Application(master=root)
app.mainloop()