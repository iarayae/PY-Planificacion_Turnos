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

#--------------------

# Inicializar diccionario de carga de actividades por persona
carga_persona= {}

# Llenar con 0 horas al inicio
for nombre in personas_df["Nombre"]:
    carga_persona[nombre] = 0

# Verificar estructura
print("\n=== Carga inicial por persona ===")
print(carga_persona)

# ---- Asignación de Tareas ----
# Ordenar tareas por duración descendente
tareas_df = tareas_df.sort_values(by="Duración (hrs)", ascending=False)

# Asignar tareas a la persona con menor carga acumulada
for i, fila in tareas_df.iterrows():
    duracion = fila["Duración (hrs)"]

    # Buscar persona con menor carga
    persona_menos_cargada = min(carga_persona, key=carga_persona.get)

    # Asignar tareas
    tareas_df.at[i, "Persona asignada"] = persona_menos_cargada

    # Sumar duración a su carga
    carga_persona[persona_menos_cargada] += duracion

# Mostrar resultado
print("\n=== Tareas Asignadas ===")
print(tareas_df[["Día", "Actividad", "Duración (hrs)", "Persona asignada"]])

print("\n=== Carga final por persona")
print(carga_persona)