# anlisisDatasetEnergia
Cálculo de longitud de redes eléctricas de la provincia de Buenos Aires. 

A partir de los datos publicados por el Ministerio de Energía y Minería (https://datos.gob.ar/dataset/energia-redes-distribucion-electrica),
en los cuales se indican de forma georreferenciada las líneas eléctricas de la Argentina, se realiza el cálculo de la longitud de cada línea de forma individual
mediante el programa script.py.

Para este estudio solo tomamos como base los datasets de las distribuidoras y cooperativas de la provincia de Buenos Aires.
Una vez calculadas las longitudes de las líneas eléctricas, se unifican los datasets en un único Excel, procurando conservar datos extras como secciones, 
niveles de tensión y tipo de línea (subterránea - aérea). 
Se detectaron errores en la información de algunos datasets, como secciones mal indicadas, suministros trifásicos realizados por solo uno o dos conductores,
y faltantes de información. 
Algunos de los datasets analizados también incluyen redes de Alta Tensión.

Finalmente, con el script2.py se procesaron los datos para agruparlos por distribuidora/cooperativa y característica de línea.

De esta forma, podemos tener una referencia respecto a la cantidad de redes de MT que posee cada cooperativa/distribuidora, y clasificarlas por niveles de tensión,
materiales y fases.

El resultado final de este trabajo es: "Lineas electricas BS AS.xlsx"
