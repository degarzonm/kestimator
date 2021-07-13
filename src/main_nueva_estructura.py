from os import name
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import COMMAND
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

class Application(tk.Frame):
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
        fig = Figure(figsize=(7,5), dpi=100)
        ax=fig.add_axes([0.1,0.1,0.8,0.8],polar=True)
        #canvas=FigureCanvasTkAgg(fig,master=root)
        #canvas.get_tk_widget().grid(row=0,column=1)
        #canvas.draw()

        lienzo = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        lienzo.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4,
                                    padx=5, sticky=tk.E+tk.W+tk.S+tk.N)
        lienzo.draw()
        toolbarFrame = tk.Frame(master=root)
        toolbarFrame.grid(row=5, column=0, padx=5)
        toolbar = NavigationToolbar2Tk(lienzo, toolbarFrame)
        toolbar.update()

        self.titulos=tk.Label(master=root, text="Estimador de densidad con Kernel", font = "Helvetica 16 bold")
        self.titulos.grid(sticky=tk.W, pady=4, padx=5)
        #Elemento visual - botones

        self.boton_archivo = tk.Button(master=root, text="archivo CSV", command=lambda: self.selectorArchivo())
        self.boton_archivo.grid(row=1, column=3)

        self.boton_graficar=tk.Button(master=root, text="Graficar", command=lambda: self.graficar(lienzo,ax))
        self.boton_graficar.grid(row=2, column=3, pady=4)

        self.boton_randomize=tk.Button(master=root, text="Mezclar",command=self.actualizarDatos)
        self.boton_randomize.grid(row=3, column=3,pady=4)

        
    def graficar(self,canvas,ax):
        c = ['r','b','g']  # plot marker colors
        ax.clear()         # clear axes from previous plot
        for i in range(3):
            theta = np.random.uniform(0,360,10)
            r = np.random.uniform(0,1,10)
            ax.plot(theta,r,linestyle="None",marker='*', color=c[i])
            canvas.draw()
    
    def selectorArchivo(self):
        global archivo_csv
        self.filename = filedialog.askopenfilename(initialdir="/datasets", title="Seleccione el archivo de datos separado por coma",filetypes=(("archivos csv","csv"),("todos","*")))
    
    def actualizarDatos():
        print("To Do: refrescar")

root=tk.Tk()
app=Application(master=root)
app.mainloop()