import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

house_df = pd.read_csv("src\kc_house_data.csv")

print(f"El archivo contiene {house_df.shape[0]} filas y {house_df.shape[1]}")
print(house_df.info())
print(f"Nombre de las columnas: {house_df.columns}")