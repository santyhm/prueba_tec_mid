Proyecto de Prueba Técnica
Este proyecto incluye tres módulos principales desarrollados en Django y FastAPI, donde se cubren los siguientes puntos:

Gestión de blogs con usuarios, publicaciones, comentarios y etiquetas.
Resolución de problemas numéricos mediante una API que encuentra dos números que suman un valor objetivo.
Sistema de gestión de bibliotecas implementado tanto con consola como con API en FastAPI.
Requisitos previos
Python 3.x
MySQL (para la base de datos del módulo de blogs)
Dependencias del proyecto listadas en requirements.txt
Instrucciones de instalación
1. Crear y activar un entorno virtual


python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
2. Instalar dependencias
Con el entorno virtual activo, instala las dependencias del proyecto:

pip install -r requirements.txt
Módulo 1: Blogs (Django)
Este módulo implementa un sistema básico de gestión de blogs con los siguientes elementos:

Usuarios
Publicaciones de blog
Comentarios
Etiquetas
Migraciones de base de datos
Configura la conexión a la base de datos en el archivo settings.py (ubicado en la carpeta /prueba_tec_mid), la base de datos utilizada es MySQL.

Crea las migraciones y aplica los cambios en la base de datos con los siguientes comandos:

python manage.py makemigrations
python manage.py migrate
Acceso al panel de administración
Para interactuar con los modelos visualmente y gestionar las entradas de blogs, etiquetas y comentarios:

Crea un superusuario para el panel de administración con:

python manage.py createsuperuser
Inicia el servidor de desarrollo:

python manage.py runserver
Accede al panel de administración en: http://127.0.0.1:8000/admin y utiliza las credenciales del superusuario que creaste.
Módulo 2: Resolución de problemas numéricos (FastAPI)
Este módulo utiliza FastAPI para resolver el problema de encontrar los índices de dos números en una lista que suman un valor objetivo.

Ejecución del módulo
Ve a la carpeta /number_int.

Ejecuta el servidor FastAPI con uno de los siguientes comandos:

python num_int.py
O con Uvicorn:

uvicorn num_int:app --reload
Accede a la documentación interactiva de la API en: http://127.0.0.1:8000/docs, donde podrás probar los endpoints disponibles.
Módulo 3: Gestión de bibliotecas (FastAPI y consola)
Este módulo incluye dos versiones del sistema de gestión de bibliotecas:

Versión por consola: Un sistema de gestión básico que simula una biblioteca y permite realizar operaciones de gestión de libros y miembros.

Versión con FastAPI: Una API para manejar las mismas operaciones de forma más estructurada.

Ejecución de la versión por consola
Ve a la carpeta /library.

Ejecuta el siguiente comando:

python library.py
Ejecución de la versión con FastAPI
Ve a la carpeta /library.

Ejecuta el servidor FastAPI con uno de los siguientes comandos:

python library_fastapi.py
O con Uvicorn:

uvicorn library_fastapi:app --reload
Accede a la documentación interactiva de la API en: http://127.0.0.1:8000/docs.
Notas adicionales:
Asegúrate de tener configurada correctamente la conexión a la base de datos MySQL para el módulo de Blogs.
Si deseas cambiar las rutas o configuraciones, puedes hacerlo en los archivos settings.py (Django).
