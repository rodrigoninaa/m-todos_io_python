import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.transforms import Bbox
from datetime import datetime, timedelta
import pandas as pd

# Función para convertir una cadena de fecha a formato datetime
def convertir_fecha(fecha):
    return datetime.strptime(fecha, "%d-%m-%Y")

# Leer datos desde un archivo Excel
datos = pd.read_excel('Planificacion.xlsx')

# Procesamiento de las fechas de inicio y fin
if datos['Inicio'].dtypes == 'datetime64[ns]':
    datos['DT inicio'] = datos['Inicio']
    datos['Inicio'] = datos['Inicio'].dt.strftime('%d/%m/%Y')
else:
    datos['DT inicio'] = datos['Inicio'].apply(convertir_fecha)

if datos['Fin'].dtypes == 'datetime64[ns]':
    datos['DT fin'] = datos['Fin']
    datos['Fin'] = datos['Fin'].dt.strftime('%d/%m/%Y')
else:
    datos['DT fin'] = datos['Fin'].apply(convertir_fecha)

# Calcular la duración y otros campos adicionales
datos['DT duracion'] = datos['DT fin'] - datos['DT inicio']
datos['Color'] = datos['Color'].replace(np.nan, 'blue')
datos['Avance'] = datos['Avance'].replace(np.nan, 0)
datos.reset_index(inplace=True)
datos['DT duracion avance'] = datos['DT duracion'] * datos['Avance']
hitos = datos[datos['DT duracion'] == timedelta()]
nrows = datos.shape[0]
valores_tabla = datos[['Tarea', 'Inicio', 'Fin', 'DT duracion']]
duracion_total = datos['DT fin'].max() - datos['DT inicio'].min()

# Crear la figura y el eje
fig, ax = plt.subplots(1, 1, figsize=(duracion_total.days / 10, nrows * 0.3), constrained_layout=True, sharex=False)
ax.invert_yaxis()

# Graficar las barras horizontales y los hitos
ax.barh(datos['index'],
        datos['DT duracion'],
        left=datos['DT inicio'],
        label=datos['Tarea'],
        color=datos['Color'],
        height=0.35,
        alpha=0.5)
ax.barh(datos['index'],
        datos['DT duracion avance'],
        left=datos['DT inicio'],
        label=datos['Tarea'],
        color=datos['Color'],
        height=0.15,
        alpha=1)
ax.scatter(hitos['DT inicio'],
           hitos['index'],
           marker='D',
           color=hitos['Color'],)

# Configuración del eje x con formato de fechas
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Anotaciones en las barras con el porcentaje de avance
for d, l, r in zip(datos['DT fin'], datos['index'], datos['Avance']):
    ax.annotate('{}%'.format(round(r * 100), 2),
                xy=(d, l),
                xytext=(-3, np.sign(l) * 3),
                textcoords='offset points',
                horizontalalignment='left')

# Crear una tabla con información adicional
tabla = ax.table(cellText=valores_tabla.to_numpy(),
                 loc='left',
                 colLabels=['Tarea', 'Inicio', 'Fin', 'Duracion'],
                 colWidths=[0.02, 0.02, 0.02, 0.03],
                 bbox=(-0.6, 0, 0.6, (nrows + 1) / nrows))

# Configuración adicional de la figura
ax.margins(y=0.005)
tabla.auto_set_font_size(False)
tabla.set_fontsize(9)
ax.grid(True)
ax.yaxis.set_ticklabels([])

# Guardar la figura como un archivo PDF
plt.savefig('Planificacion 1.pdf', bbox_inches='tight')