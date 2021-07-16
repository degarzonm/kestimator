from os import name
import tkinter as tk
from tkinter import Label, filedialog
from tkinter.constants import COMMAND
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import csv
import otro

class Application(tk.Frame):
    counter=0
    
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.createWidgets()

    def createWidgets(self):

        root.title("Kernel Density Estimation")
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        #fig=plt.figure(figsize=(8,8))
        fig = Figure(figsize=(9,9), dpi=100)
        
        #ax=fig.add_axes([0.1,0.1,0.8,0.8],polar=True)
        ax=fig.add_axes([0.04,0.06,1,1])
        
        #canvas=FigureCanvasTkAgg(fig,master=root)
        #canvas.get_tk_widget().grid(row=0,column=1)
        #canvas.draw()

        lienzo = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        lienzo.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4,
                                    padx=5, sticky=tk.E+tk.W+tk.S+tk.N)
        lienzo.draw()
        toolbarFrame = tk.Frame(master=root)
        toolbarFrame.grid(row=5, column=0)
        toolbar = NavigationToolbar2Tk(lienzo, toolbarFrame)
        toolbar.update()

        self.titulos=tk.Label(master=root, text="Estimador de densidad con Kernel", font = "Helvetica 16 bold")
        self.titulos.grid(sticky=tk.E, pady=4, padx=5)
        #Elemento visual - botones

        self.boton_archivo = tk.Button(master=root, text="archivo CSV", command=lambda: self.selectorArchivo())
        self.boton_archivo.grid(row=1, column=3,sticky=tk.E+tk.W+tk.S+tk.N)

        self.boton_graficar=tk.Button(master=root, text="Graficar", command=lambda: self.graficar(lienzo,ax))
        self.boton_graficar.grid(row=2, column=3, pady=4,sticky=tk.E+tk.W+tk.S+tk.N)

        self.boton_dataset_alea=tk.Button(master=root,text="DS Aleatorio",command=lambda: self.datasetGenerado(lienzo,ax))
        self.boton_dataset_alea.grid(row=3,column=3,pady=4,sticky=tk.E+tk.W+tk.S+tk.N)

        self.boton_kde=tk.Button(master=root, text="KDE",command=lambda: self.KDE(lienzo,ax))
        self.boton_kde.grid(row=4, column=3,pady=4,sticky=tk.E+tk.W+tk.S+tk.N)
        
        w = tk.Scale(master=root, from_=0, to=42)
        w.grid(row=4, column=4)

        OptionList = [
        "Epanechnikov",
        "Tri-cube",
        "Gaussian"
        ] 

        #self.combo = tk.Combobox(self)
        #self.combo.place(x=50, y=50)

    #cargamos el dataset en un csv globlal 
    def selectorArchivo(self):
        global np_dataset,nombres_data
        self.filename = filedialog.askopenfilename(initialdir="/datasets", title="Seleccione el archivo de datos separado por coma",filetypes=(("archivos csv","csv"),("todos","*")))
       # texto_ruta_csv= Label(root , text= self.filename).grid(row=4, column=3,pady=4)
        np_dataset = np.genfromtxt(self.filename,delimiter=',',names=True,encoding="utf-8")
        nombres_data=np_dataset.dtype.names
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


    def datasetGenerado(self, canvas, ax):
        c = ['r','b','g']  # plot marker colors
        ax.clear()         # clear axes from previous plot
        for i in range(3):
            theta = np.random.uniform(0,36,10)
            r = np.random.uniform(0,1,10)
            ax.plot(theta,r,linestyle="None",marker='*', color=c[i])
            canvas.draw()
        theta = np.random.uniform(0,36,10)
        r = np.random.uniform(0,1,10)
        ax.plot(theta,r,linestyle="None",marker='x',color=c[0])
        canvas.draw()
    
    
    def KDE(self,lienzo,ax):
        datos_1=np.array(np_dataset[nombres_data[1]])
        x_0=np.linspace(datos_1.min(),datos_1.max(),100)
        
        y=[otro.estimador(1,x,datos_1,1) for x in x_0]
        
        
        ax.plot(x_0,y)
        lienzo.draw()
        self.counter+=1
        print("To Do: refrescar", self.counter)
        print("Aqui quiero actualizar la grafica, dada una columna:", y)




root=tk.Tk()
app=Application(master=root)
app.mainloop()