import pandas as pd

# Lectura de archivo excel con pandas
archivo_excel = 'datos/turnos.xlsx'

# Carga de las hojas de excel
personas_df = pd.read_excel(archivo_excel, sheet_name='Personas')
tareas_df = pd.read_excel(archivo_excel, sheet_name='Planificacion')

# Mostrar datos cargados
print("=== Personas Disponibles ===")
print(personas_df)

print("\n=== Tareas por asignar ===")
print(tareas_df)