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
$ cd JWT-Python
```

Descargar y construir las imagenes necesarias

```sh
$ docker-compose build
$ docker-compose up 
```

### Probar App

Ingrese a la direccion para ver la documentacion del API en swagger
[http://localhost/api/](http://localhost/api/)

#### Crear Usuario:

```sh
$ curl -X POST -H "Content-Type: application/json" \
 -d '{"username":"demo-admin@admin.com", "email":"demo-admin@admin.com", "password": "12345678", "is_staff": true}' \
 http://localhost/user/
```

#### Obtener Token:

```sh
$ curl -X POST -H "Content-Type: application/json" \
 -d '{"username":"demo-admin@admin.com", "password": "12345678"}' \
 http://localhost/token
```

#### Validar Token:

```sh
$ curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://localhost/validate/
```

#### Listar Usuarios:

```sh
$  curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://localhost/user-list/
```

License
----

MIT
