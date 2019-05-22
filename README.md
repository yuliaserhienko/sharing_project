### Files sharing project

[X] Models
[X] Views
[X] Redis
[X] MySQL
[X] Celery beat
[ ] Authorization
[ ] WSGI
[ ] Nginx
[ ] Code cleanup
[ ] Bootstrap

```sh
docker-compose build
docker-compose up

docker-compose exec web bash -c "./sharing/manage.py makemigrations"
docker-compose exec web bash -c "./sharing/manage.py migrate"
docker-compose exec web bash -c "./sharing/manage.py createsuperuser"
```