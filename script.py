from geojson_length import calculate_distance, Unit
import ast
import pandas as pd

#Creo la lista que voy a utilizar para agregar la nueva columna en el dataframe. Esta columna indicará la distancia de la linea.
newCol = []

#Leo el archivo a analizar
df = pd.read_csv(r"RUTA DEL ARCHIVO A ANALIZAR", header=0,)

#Genero la nueva columna con las distancias.
for i in range(len(df["geojson"])):
    try:
        line = {"type": "Feature","properties": {},"geometry": {"type": "LineString","coordinates": ast.literal_eval(df["geojson"][i][41:-2])}}
        newCol.append(round(calculate_distance(line, Unit.meters),3))
        print("Ejecutando la linea " + str(i))
    except:
        newCol.append(0)
        print("Problema en linea  " + str(i))


print("EJECUTADA CON EXITO LA PRIMERA ETAPA")

#df["distribuidora"] = "NOMBRE DE DISTRIBUIDORA"
df["longitud"] = newCol
df.to_csv('NOMBRE DE DISTRIBUIDORA.csv')
print("EJECUTADO CON EXITO EL GUARDADO DEL ARCHIVO")
