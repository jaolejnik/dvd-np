# DVD NP - A web project boilerplate

## Technology overview

### The main cast

-   [`D`jango](https://www.djangoproject.com/)
-   [`V`ue.js](https://vuejs.org/)
-   [`D`ocker](https://www.docker.com/)
-   [`N`ginx](https://www.nginx.com/)
-   [`P`ostreSQL](https://www.postgresql.org/)

### Requirements to run this project

-   Docker and [Docker Compose](https://docs.docker.com/compose/)

And that should be it. That's the beauty of [containerization](https://www.docker.com/resources/what-container).
`Django`, `Vue` and `PostgreSQL` images will be downloaded and laoded into seperate containers.
For Django all the requirements are specified in `Pipfile` created by `pipenv` and in Vue's case
it's `package.json` created by `yarn`.

_For more details check `Pipfile` and `package.json`._

## Development Environment

When first time building a project run

```
docker-compose build && docker-compose up -d
```

This will create and initialize containers with all necessarry services for development. You can now
check your `localhost:8080` for running Vue server. The same goes for `localhost:8000`, where Django
should be accessible. You'll see an error page that says **"TemplateDoesNotExist at /"**. It's
because Django is configured to serve a template file at `'/'` in the production environment, but it's missing since it's the development environment. You can check `'/admin'` for the admin login page.\

If you want to launch already built containers just run

```
docker-compose up -d
```

where `-d` means it runs in the background. Otherwise all the logs from the containers would end up
in you stdout. If you want to access the logs just run

```
docker-compose logs -f [SERVICE_NAME]
```

You can find yourself in need to access the container itself. You can do that with

```
docker-compose exec [SERVICE_NAME] bash     // or some other shell used by the container*
```

If you want to stop and remove containers created by `up` you can simply run

```
docker-compose down
```

When rebuilding it's a good idea to add these flags to the build command:

```
docker-compose  build --force-rm --no-cache && docker-compose  up -d
```

_For more info visit official Docker docs [here](https://docs.docker.com/compose/reference/overview/)._

## But how does it work?

Once the containers are up you usally want to visit `localhost:8080`. That's where Vue development server is running. Thanks to the config in `vue.config.js` every request at `"/api/"` is redirected to `django:8000`, so in other words container with Django development server. \
You can easily develop your app outside the containers since _almost_ every change will be automatically applied inside them. The only exception is when you change something in the development configuration, then you should rebuild the containers.

## Linters and formatters

TODO

---

## Production Environment

Starting and removing containers for production is basically the same thing with one small difference:

### **You have to specify the YAML file meant for production after `docker-compose` command.**

You can do this using `-f` flag, see example below.

```
docker-compose -f docker-compose.prod.yml up -d
```

_(By default Docker Compose will use `docker-compose.yml` that's why you didn't have to do this for
development environment.)_

## But how does it work?

Although container related commands are quite similar, the way the production build works couldn't
be any more different from development one.\
First of all there is an `Nginx` web server running in a container. This is like a gateway from the internet to the backend. All the requests on the site will go through this web server and its job is
to find requested resources and send them back to the user.\
Django is run by [Gunicorn](https://gunicorn.org/), which is _a web server gateway interface (WSGI)_.
It's kind of a middleman between a web server (Nginx) and WSGI app (Django) that makes them work together. _For more info see [here](https://www.fullstackpython.com/wsgi-servers.html)._\
So the Nginx is listening on `localhost:80` and passes requests to Gunicorn which is running in Django's container on port 8000, so in other words `django:8000`. Of course the production build is not meant to
be run on your local machine but rather on some remote Virtual Machine like those on [DigitalOcean](https://www.digitalocean.com/) or [Heroku](https://www.heroku.com/) so the `localhost` will be
replaced by the address of your remote server.
