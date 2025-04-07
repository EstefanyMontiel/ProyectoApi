# ProyectoApi
Este proyecto es una API REST desarrollada en Python utilizando el framework FastAPI, conectada a una base de datos MySQL, y orquestada con Docker Compose para un entorno de desarrollo completo y reproducible.

## Como levantar el entorno (Api + BD)
**Requisitos**
-Docker desktop
-Python v3.9+
-MySQL workbench 
Package 
-fastapi
-uvicorn
-sqlalchemy
-PyMySQL
-alembic
-python-dotenv
-cryptography

* 1.- Clona el repositorio 
git clone https://github.com/EstefanyMontiel/ProyectoApi.git

* 2.- Levanta el entorno con Docker compose con el siguiente comando
    
     docker-compose up --build


Esto inicia:
api: la aplicacion FastAPI en Uvicorn 
db: una base de datos MySQL 

* 3.- Conexión a la BD desde MySQL workbench 

**Asegurate de usar los valores que se definieron en el servicio bd dentro del archivo docker-compose.yml

 a.- Abre MySQL workbench, haz clic en el ícono de + para crear una nueva conexión
 b.- Completa el formulario con los siguientes datos:
 Connection name: Proyecto_crud 
 Hostname: localhost 
 Port: 3307
 Username: root 
 Password: 1234

 Haz clic en Test Connection para verificar que todo esté bien. Si la conexión es exitosa, haz clic en OK para guardarla.
 
* 4.- Abre tu navegador 
Documentacion Swagger: 
👉http://localhost:8000/docs
 Documentación Redoc:
👉 http://localhost:8000/redoc


## Cómo probar los endpoints mediante Postman o Swagger.

* Con Swagger UI
1.- Asegúrate de que los contenedores estén corriendo:
Ejecuta en terminal: docker-compose up

2.- Abre tu navegador y visita:
http://localhost:8000/docs

Se abrirá la documentación interactiva de Swagger UI, generada automáticamente por FastAPI.

3.- Para probar un endpoint:

Haz clic sobre el nombre del endpoint (por ejemplo, GET /users). Aparecerá una sección con un botón azul que dice Try it out.

Haz clic en Try it out para activar el formulario.

Completa los parámetros si es necesario.

Presiona el botón Execute. Debajo se mostrarán:

El Request URL.
La respuesta (Response Body, Status Code, etc.).

* Con Postman
1.-Abre Postman (puedes descargarlo desde https://www.postman.com/).

2.- Crea una nueva Request o Collection.
3.-Establece la URL base de la API:
http://localhost:8000/DogBreeds

4.- Agrega el endpoint que deseas probar. Por ejemplo:http://localhost:8000/users

5.-Verifica que el método HTTP sea el correcto (GET, POST, PUT, DELETE, etc.).

6.- Haz clic en Send para enviar la solicitud.
Verás la respuesta en la parte inferior: cuerpo, código de estado (200 OK, 201 Created, 404 Not Found, etc.).

## Ejemplos de peticiones y respuestas esperadas
* GET /dog_breeds
Descripción: Obtiene una lista de todas las razas de perros registradas.
Petición: GET http://localhost:8000/dog_breeds

Respuesta esperada: 

[
  {
    "id": 1,
    "name": "Labrador Retriever",
    "description": "Amigable, activo y sociable",
    "size": "grande",
    "energy_level": "alto"
  },
  {
    "id": 2,
    "name": "Chihuahua",
    "description": "Pequeño pero valiente",
    "size": "pequeño",
    "energy_level": "medio"
  }
]
* POST /dog_breeds
Descripción: Crea una nueva raza de perro.
Petición:POST http://localhost:8000/dog_breeds

Respuesta esperada: 

{
  "id": 3,
  "name": "Golden Retriever",
  "description": "Muy amigable y leal",
  "size": "grande",
  "energy_level": "alto"
}

* GET /dog_breeds/{id}
Descripción: Obtiene los datos de una raza específica por su ID.

Petición: GET http://localhost:8000/dog_breeds/1

Respuesta esperada: 
{
  "id": 1,
  "name": "Labrador Retriever",
  "description": "Amigable, activo y sociable",
  "size": "grande",
  "energy_level": "alto"
}

* DELETE /dog_breeds/{id}
Descripción: Elimina una raza del sistema.
Petición: DELETE http://localhost:8000/dog_breeds/1

Respuesta esperada: 
{
  "detail": "Raza eliminada correctamente"
}
