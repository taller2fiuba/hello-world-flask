# Hello world en Flask

## Dependencias:
- Docker + Docker compose

## Para correr el server de dev
```bash
$ bin/start-dev-server
```
Cualquier cambio en el sistema de archivos provocará que Flask recargue automáticamente el proyecto. Cualquier cambio en el sistema de archivos dentro del container se verá reflejado fuera del container.

## Para correr un comando de flask
```bash
$ bin/flask
```

Todos los comandos de flask se corren adentro del container de dev que esté corriendo.

## Para deploy a prod
Hay un `Dockerfile` que se usa únicamente para deployar a prod.
```bash
$ docker build -t hello-world-flask .
$ docker run -d -p 5000:80 hello-world-flask
```

Con eso el contenedor está corriendo y el sitio es accesible desde localhost:5000.

# Notas
Tener en consideración que el usuario "virtual" con el que corre el container es `root`, con lo cual si se crearan archivos desde adentro del container (por ejemplo corriendo `flask [algo que cree archivos]` van a quedar creados con usuario y grupo `root`, y hay que cambiarlos manualmente.
