import pandas as pd

# --------------------------------------------------------------------------
# ETAPA 1: CARGA Y VALIDACIÓN DE DATOS
# --------------------------------------------------------------------------
# Se cargan los dos archivos necesarios en memoria:
# - El CSV contiene las respuestas de cada estudiante.
# - El Excel contiene la clave de respuestas correctas.
# Pandas los convierte en tablas de datos llamadas DataFrames.
df_estudiantes = pd.read_csv('archivos/respuestas_estudiantes.csv')
df_correctas = pd.read_excel('archivos/respuestas_correctas.xlsx')

# --------------------------------------------------------------------------
# ETAPA 2: PROCESAMIENTO CENTRAL
# --------------------------------------------------------------------------

# --- 2.1: Preparar la clave de respuestas para una comparación eficiente ---

# Se extraen los nombres de todas las preguntas (ej. 'P1', 'P2') en una lista.
preguntas = df_correctas['Pregunta'].values 

# Se crea un diccionario vacío para almacenar las respuestas correctas.
# Un diccionario permite buscar la respuesta correcta de una pregunta muy rápido.
clave_respuestas = {}
# Se recorren las filas del DataFrame de respuestas correctas.
for i in range (df_correctas.shape[0]):

    # En cada fila, se extrae el nombre de la pregunta y su respuesta correcta.
    pregunta = df_correctas['Pregunta'].iloc[i]
    respuesta = df_correctas['Respuesta'].iloc[i]
    
    # Se guarda el par pregunta-respuesta en el diccionario.
    # Ejemplo: clave_respuestas['P1'] = 'A'
    clave_respuestas[pregunta] = respuesta

# --- 2.2: Calcular la calificación de cada estudiante ---

# Se añade una nueva columna 'Calificacion' al DataFrame de estudiantes y se inicia en 0.
df_estudiantes['Calificacion'] = 0

# Se recorre la lista de preguntas que obtuvimos antes.
for p in preguntas:
    # Para cada pregunta, se busca su respuesta correcta en el diccionario.
    respuesta_correcta = clave_respuestas[p]
    
    # Se comparan las respuestas de TODOS los estudiantes con la respuesta correcta.
    # Si la respuesta coincide (True), se convierte a 1. Si no (False), se convierte a 0.
    # Finalmente, se suman estos puntos (1 o 0) a la calificación de cada estudiante.
    df_estudiantes['Calificacion'] = df_estudiantes['Calificacion'].add(
        (df_estudiantes[p] == respuesta_correcta).astype(int))

# --------------------------------------------------------------------------
# ETAPA 3: GENERACIÓN DE REPORTES
# --------------------------------------------------------------------------

# --- 3.1: Crear y mostrar un reporte detallado con errores marcados ---

# Se crea una copia del DataFrame de estudiantes para no modificar los resultados originales.
df_detalle = df_estudiantes.copy()

# Se recorre cada pregunta de nuevo.
for p in preguntas:
    # Se usa el método .where() para marcar errores:
    # Si la respuesta del estudiante es correcta, se deja como está.
    # Si es incorrecta, se le añade una 'X' al final.
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p],
        df_detalle[p] + 'X'
    )

# Se ordena la tabla detallada por calificación, de mayor a menor.
df_detalle = df_detalle.sort_values(by='Calificacion', ascending=False)

# Se imprime el reporte detallado en la consola.
print("Letenda: Respuesta X = Incorrecta")
print(df_detalle.to_string(index=False)) # .to_string() para mostrar todas las filas y columnas

# --- 3.2: Mostrar un reporte resumido de calificaciones finales ---

# Se imprime una tabla más simple, solo con el nombre y la calificación final.
print("\nCalificaciones finales:")
print(df_estudiantes[['Nombre', 'Calificacion']].sort_values('Calificacion', ascending=False).to_string(index=False))

# --- 3.3: Guardar los resultados en un archivo CSV ---

# Se exporta el DataFrame con las calificaciones a un nuevo archivo CSV.
# index=False evita que se guarde una columna extra con los números de fila.
df_estudiantes.to_csv('archivos/calificaciones_finales.csv', index=False)
print("\nLas calificaciones finales han sido guardadas en 'archivos/calificaciones_finales.csv'")