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


lista_1_unidim=[2,4,3,2,3,34,23,4,42,27,23,42,42,42,42,34,28,34,36,23,34,24,23]
n = 100

contador_uno=1
ventana = tk.Tk()

def KDE():
    return 42

def _quit():
    ventana.quit()     # stops mainloop
    ventana.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def actualizarDatos():
    print(contador_uno)

def graficar():
    global contador_uno
    #plt.hist(lista_1_unidim)
    #plt.scatter(x, y, label='y noise',color='g')
    #plt.show()
    
    contador_uno=contador_uno+1
    print(contador_uno)

def selectorArchivo():
    global archivo_csv
    ventana.filename = filedialog.askopenfilename(initialdir="/datasets", title="Seleccione el archivo de datos separado por coma",filetypes=(("archivos csv","csv"),("todos","*")))


if __name__ == '__main__':

    x = np.random.normal(size=len(lista_1_unidim ))
    #y = np.sin(x) + 0.3
    y= np.add( [3/5*i+2 for i in lista_1_unidim],np.random.normal(size=len(lista_1_unidim )))
    print(y)

    #mainKSM()

    ventana.title("Kernel Density Estimation")
    ventana.geometry("900x630")


    #ventana.pack(fill=tk.BOTH, expand=True)

    ventana.columnconfigure(1, weight=1)
    ventana.columnconfigure(3, pad=7)
    ventana.rowconfigure(3, weight=1)
    ventana.rowconfigure(5, pad=7)


    titulos=tk.Label(ventana, text="Estimador de densidad con Kernel", font = "Verdana 16 bold italic")
    titulos.grid(sticky=tk.W, pady=4, padx=5)

    
    #Elemento visual - botones

    boton_archivo = tk.Button(ventana, text="archivo CSV", command=selectorArchivo)
    boton_archivo.grid(row=1, column=3)

    boton_grafo= tk.Button(ventana, text="Graficar", command=graficar)
    boton_grafo.grid(row=2, column=3, pady=4)

    boton_randomize=tk.Button(ventana, text="Mezclar",command=actualizarDatos)
    boton_randomize.grid(row=3, column=3,pady=4)

    #mas botones aqui#

    ##################

    #Elemento visual - grafico embebido
    fig = Figure(figsize=(7,5), dpi=100)               
    fig.add_subplot(111).scatter(x, y)               ##agregamos un scatterplot a la cola de matplotlib

    lienzo = FigureCanvasTkAgg(fig, master=ventana)  # A tk.DrawingArea.
    
    lienzo.get_tk_widget().grid(row=1, column=0, columnspan=2, rowspan=4,
                                padx=5, sticky=tk.E+tk.W+tk.S+tk.N)
    lienzo.draw()

    #Elemento visual- herramientas del grafo 
    toolbarFrame = tk.Frame(master=ventana)
    toolbarFrame.grid(row=5, column=0, padx=5)
    toolbar = NavigationToolbar2Tk(lienzo, toolbarFrame)
    toolbar.update()
    
    ##
    ##dibujo final tkinter
    ventana.mainloop()

#import KSM
