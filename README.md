Djando skeleton app
========

### Requirements
- Docker
- Git

### Installation

Run this command to bring up the environment

```bash
> make build
```
### Webserver

By default, building the container will do the following

```bash
python3 manage.py runserver 0.0.0.0:8000
```

But in case the webserver is down, or you want to run it again by yourself,
just run the command.

### Components

- Check [Database](./docs/database.md) to learn about migrations.
- In [Api](./docs/api.md) you will see some examples about the most basic api.
