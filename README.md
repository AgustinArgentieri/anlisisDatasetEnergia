# anlisisDatasetEnergia
Cálculo de longitud de redes eléctricas de la provincia de Buenos Aires. 

A partir de los datos publicados por el Ministerio de Energía y Minería (https://datos.gob.ar/dataset/energia-redes-distribucion-electrica),
en los cuales se indican de forma georeferenciada las lineas electricas de la Argentina, se realiza el cálculo de la longitud de cada linea de forma individual
mediante el programa script.py.

Para este estudio solo tomamos como base los dataset de las distribuidoras y cooperativas de la provincia de Buenos Aires.
Una vez calculadas las longitudes de las líneas eléctricas, se unifican los dataset en un único Excel, procurando conservar datos extras como secciones, 
niveles de tensión y tipo de línea (Subterranea - Aerea). 
Se detectaron errores en la informacion de algunos datasets, como secciones mal indicadas, suministros trifasicos realizados por solo uno o dos conductores,
y faltantes de información. 
Algunos de los dataset analalizados tambien incluyen redes de Alta Tensión.

Finalmente, con el script2.py se procesaron los datos para agruparlos por distribuidora/cooperativa y caracteristica de linea.

De esta forma, podemos tener una referencia respecto a la cantidad de redes de MT que posee cada coperativa/distribuidora, y clasificarlas por niveles de tensión,
materiales y fases.

El resultado final de este trabajo es: "Lineas electricas BS AS.xlsx"
