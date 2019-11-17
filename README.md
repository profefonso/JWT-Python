# JWT - Python

Creacion de Token JWT con Python Django API REST.

  - Genera TOKEN JWT de valicacion Usando Autenticacion Django
  - Valida Token Generado
  - Crea usuarios con dos niveles de seguridad (staff - default)
  - Lista de usuarios usando solo perfil Staff


### Tecnologias 

Desarrollado usando tecnologias:

* [Python] - Django Rest Framework - Gunicorn.
* [Docker] - Gestion de contenedores y despliegue.
* [PostgreSql] - Base de datos relacional.
* [Nginx] - Servidor de aplicaciones.

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Instalación

Para la instalación requiere [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

Clonar el proyecto e ingresar al directorio creado

```sh
$ git clone https://github.com/profefonso/JWT-Python.git
$ cd BinarySearchTree
```

Descargar y construir las imagenes necesarias

```sh
$ docker-compose build
$ docker-compose up 
```

### Probar App

Ingrese a la direccion para ver la documentacion del API en swagger
[http://localhost/api/](http://localhost/api/)


License
----

MIT
