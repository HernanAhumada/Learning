x = ["a", "b", "c", "d"]
print(x[-3:])
print(x[1:])
print(x[:])
print(x[:-1])

import numpy as np
x = np.array([10, 15, 22, 13, 17, 20, 8])
x_small = x < 17
print(type(x_small))
print(x_small)
x_small = x[x<17]
print(x_small)

x = [15,10,2,84] + [1,4,8,7,9]
print(x)
print(x[0])
print(x.count(x[0]))
print(x.index(x.count(x[0])))

import pandas as pd
# Crear un DataFrame de ejemplo 
data = { 'Año': [2020, 2020, 2021, 2021]
        ,'Mes': ['Enero', 'Febrero', 'Enero', 'Febrero']
        ,'Ventas': [250.123456, 150.78495, 200.00, 300] 
       } 
df = pd.DataFrame(data) 
print(df)
# Crear una tabla dinámica 
#pivot = df.pivot_table(index='Año', columns='Mes', values='Ventas', aggfunc='sum') 
pivot = df.pivot_table('Ventas', index='Año', columns='Mes') 
print(pivot)
print(pivot.loc[2020:2021])


product_line = {'date':['2018-01-15','2018-01-15','2018-01-16','2018-01-16','2018-01-17']
               ,'product_line':['Health and beauty', 'Health and beauty', 'Home and lifestyle', 'Sports', 'Food and beverages']
               ,'product':['shampoo','Headphones','Lamp', 'Yoga mat', 'Milk']
               ,'unit_price':[6.99, 25.28, 46.33, 39.99, 5.99]
               ,'quantity':[7,5,3,5,8]      
               }
print(type(product_line))
sales = pd.DataFrame(product_line)
print(sales)
print(sales['product_line'])
print(sales['product_line'].value_counts())
print(sales['product_line'].value_counts(normalize = True))