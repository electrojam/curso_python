import os

# Obtener el directorio actual cwd = current working directory
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)

# Listar los archivos .txt del directorio actual
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt: ", txt_files)

'''
# Renombrar archivo txt
os.rename('caperucita.txt', 'cuento.txt')
print('Archivo renombrado')

txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Archivos txt:", txt_files)
'''
