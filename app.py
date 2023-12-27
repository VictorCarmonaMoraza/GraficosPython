import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request

app = Flask(__name__)

ahorros = [52,104,32,65,15,76]
df = pd.DataFrame(ahorros,index=['Enero','Febrero','Marxo','Abril','Mayo','Junio'])

'''plt.plot(ahorros)
plt.show()'''

@app.route('/ahorro')
def ahorro():
    plt.plot(ahorros)
    plt.show()

@app.route('/dataframe')
def dataframe():
    plt.plot(df)
    plt.show()

@app.route('/ejes')
def ejes():
    ahorros2 =  np.random.randint(100, size=6)
    plt.plot(ahorros2)
    plt.show()

@app.route('/ejes2')
def MapeandoEjes():
    ahorros3 = np.random.randint(100, size=6)
    meses=['Enero','Febrero','Marxo','Abril','Mayo','Junio']
    plt.plot(ahorros3)
    '''plt.xticks(range(len(meses)),meses)'''
    plt.xticks([0,1,2,3,4,5],meses)
    plt.show()

@app.route('/ejes3')
def MapeandoEjesManuales():
    ejeX = ["A","B","C","D","E","F"]
    ejeY=['Enero','Febrero','Marxo','Abril','Mayo','Junio']
    plt.plot(ejeX,ejeY)
    plt.show()

@app.route('/ejes4')
def GraficoInvertido():
    ejeX = ["A","B","C","D","E","F"]
    ejeY=['Enero','Febrero','Marxo','Abril','Mayo','Junio']
    plt.plot(ejeY,ejeX)
    plt.show()


@app.route('/ejes5')
def ValoresAleatorios():
    ejeX = np.random.randint(20, size=[6])
    ejeY = np.random.randint(20, size=[6])
    plt.plot(ejeX,ejeY)
    plt.show()