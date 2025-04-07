from setuptools import setup

AUTHORS = [ 
    { "name": "may", "email": "maydaymm66@yahoo.com" }, 
    { "name": "juan", "email": "juan@example.com" }
]

# Convertir lista de autores a string
author_names = ", ".join(author["name"] for author in AUTHORS)
author_emails = ", ".join(author["email"] for author in AUTHORS)

setup (
    name = 'smv_prueba1',  #para el import
    version ='0.0.2', #se va cambiando según se incluyan cambios
    #packages = ['smv_prueba1'], #Debe coincidir con el nombre de la carpeta
    description = 'libreia para sumar dos numeros',
    long_description = open('README.md', encoding='utf-8').read(),
    long_description_content_type = "text/markdown",
    author = author_names,
    author_email = author_emails,
    url = 'https://github.com/greenmay99/semovi_libreria',
    license = 'MIT' #Tipo de licencia
)