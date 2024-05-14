#Source: https://stackoverflow.com/questions/67660952/attributeerror-type-object-calculavariaciones-has-no-attribute-retornos-diar
import os
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

class ImportaYahoo:
    def __init__(self):
        self.df_apple = pd.DataFrame({})
        self.apple_close = pd.DataFrame({})    
    
    def importar_cotizaciones (self):
        # Importar cotizaciones de Apple
        import yfinance
        name = 'AAPL'
        ticker = yfinance.Ticker(name)
        self.df_apple = ticker.history(interval="1d",start="2017-01-4",end="2021-04-10")
        self.apple_close = self.df_apple[["Close"]]

class CalculaVariaciones:
    
    def __init__(self, importar_yahoo):
        self.df_yahoo = importar_yahoo
        self.retornos_diarios = pd.DataFrame({})
        self.log_retornos_diarios = pd.DataFrame({})
        
    def calc_retornos_diarios(self):
        # Porcentaje de variación diaria
        self.retornos_diarios = self.df_yahoo.apple_close.pct_change()
        self.retornos_diarios.fillna(0, inplace=True)
        self.retornos_diarios.dropna(inplace = True)
    
    def calc_log_retornos_diarios(self):
        self.log_retornos_diarios = np.log(self.df_yahoo.retornos_diarios + 1)
        
class DibujaHistograma():  
    def __init__(self, CalculaVariaciones ):
        self.variaciones = CalculaVariaciones
        
    def mostrar_histograma (self):
        # Plot the histogram
        print("\n*******************************************************")        
        self.variaciones.retornos_diarios.hist(bins = 100, color='blue', figsize=(15, 8))
        plt.ylabel('Frecuencia')
        plt.xlabel('Retornos diarios')
        plt.title('Histograma de los retornos diarios')
        plt.show()        
        
importar_yahoo = ImportaYahoo()
importar_yahoo.importar_cotizaciones() 

calcula_variaciones = CalculaVariaciones (importar_yahoo)
calcula_variaciones.calc_retornos_diarios()
#calcula_variaciones.calc_log_retornos_diarios()

histograma = DibujaHistograma(CalculaVariaciones)
histograma.mostrar_histograma ()