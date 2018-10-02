*[Home](../README.md)/ database*

### Migrations
To generate a new update on the mysql, when you have
your model updated, you should run:

```bash
> python manage.py makemigrations api
```

You will see that it will make a file in **migrations** directory, then
for generating the new migration, you can just apply it by running:

```bash
> python manage.py migrate api
```

Check the database. You should see that a table with the dummy
model has been generated successfully.

```bash
> make database
> show tables;
```