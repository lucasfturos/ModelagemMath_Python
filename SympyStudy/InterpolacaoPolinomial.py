# Interpolação polinomial pegando valores de uma planilha xlsx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import *

df = pd.read_excel("ConsumoDeGasolina.xlsx")
print(df.head(6))
