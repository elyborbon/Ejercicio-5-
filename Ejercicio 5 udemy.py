import pandas as pd
import numpy as np

employes= ["Employe 1", "Employe 2", "Employe 3", "Employe 4", "Employe 5", "Employe 6","Employe 7"]
positiom = ["analist", "manager", "analist","analist", "manager", "Senior manager", "manager", "none"]
Salary = [30000, 56000, 28000,33000, 60000, 75000, None, None]
column= ["Employed", "Position", "Salary"]

de= pd.DataFrame(data=list(zip(employes,positiom, Salary)), columns=column)
print (de)
# Head
print (de.head())
print (de.head(2))
#tail
print (de.tail())
print (de.tail(2))
print (de["Employed"])
print (de["Employed"])
print (de.isnull())
print (de.isna())
print (de.dropna())
print (de.dropna(thresh=2))
print (de.dropna(axis=1, thresh=7))
print (de.fillna(0))
print (de.fillna(method="ffill"))
