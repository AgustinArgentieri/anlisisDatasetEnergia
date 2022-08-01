import pandas as pd
df = pd.read_excel(r"RUTA DEL EXCEL QUE CONTIENE LAS LINEAS ELECTRICAS DE LA PROV BS AS", header=0, sheet_name="CONJUNTO" )
df2 = df.groupby(by=["tension","fases","seccion","distribuidora","tipo","material"]).sum()
df2= df2.reset_index()
print(df2.head())
df2.to_excel('Lineas electricas BS AS.xlsx', sheet_name="CONJUNTO")
print("EJECUTADO CON EXITO.")