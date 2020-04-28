[![Build Status](https://travis-ci.com/taller2fiuba/hello-world-flask.svg?branch=master)](https://travis-ci.com/taller2fiuba/hello-world-flask)
[![Coverage Status](https://coveralls.io/repos/github/taller2fiuba/hello-world-flask/badge.svg?branch=poner_linter_y_coveralls)](https://coveralls.io/github/taller2fiuba/hello-world-flask?branch=master)

# Hello world en Flask

## Dependencias:

- Docker + Docker compose

## Para correr el server de dev

```bash
$ bin/dev-compose up
```

Cualquier cambio en el sistema de archivos provocará que Flask recargue automáticamente el proyecto. Cualquier cambio en el sistema de archivos dentro del container se verá reflejado fuera del container.

Para iniciar el servidor en segundo plano o pasarle opciones extras a `docker-compose up`, se pueden agregar al final de la línea de comandos, por ejemplo:

```bash
$ bin/dev-compose up -d
```

## Para detener el server de dev

Si estaba corriendo interactivamente (en una terminal) `Ctrl-C`, si estaba corriendo
en segundo plano:

```bash
$ bin/dev-compose down
```

## Para correr un comando de flask

```bash
$ bin/flask
```

Todos los comandos de flask se corren adentro del container de dev que esté corriendo.

## Para deploy a prod

Hay un `Dockerfile` que se usa únicamente para deployar a prod.
```bash
$ docker build -t hello-world-flask .
$ docker run -d -p 5000:80 -e PORT=80 hello-world-flask
```

Con eso el contenedor está corriendo y el sitio es accesible desde localhost:5000.

## Para correr los tests unitarios

```bash
$ bin/run-unit-tests
```

## Para arreglar los errores de lint automaticamente

```bash
$ ./bin/fix-lint.sh
```

# Notas

Tener en consideración que el usuario "virtual" con el que corre el container es `root`, con lo cual si se crearan archivos desde adentro del container (por ejemplo corriendo `flask [algo que cree archivos]` van a quedar creados con usuario y grupo `root`, y hay que cambiarlos manualmente.

# Otras utilidades

## `bin/dev-compose`

Es un atajo a `docker-compose` para el servidor de dev. Se utiliza igual que `docker-compose`, solo
que el archivo `.yml` que va a utilizar está fijo.

## `bin/exec-dev`

Es un atajo para ejecutar un comando dentro del servidor de dev que está corriendo.

Casos comunes:
- `bin/exec-dev bash`: Para ejecutar un bash dentro del container
- `bin/exec-dev python`: Para abrir un intérprete de python dentro del container
