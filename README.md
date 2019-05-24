### Files sharing project
- [X] Models
- [X] Views
- [X] Redis
- [X] MySQL
- [X] Celery beat
- [X] Authorization
- [X] WSGI
- [X] Nginx
- [ ] Code cleanup
- [ ] Bootstrap
```sh
docker-compose build
docker-compose up

docker-compose exec web bash -c "./manage.py makemigrations"
docker-compose exec web bash -c "./manage.py migrate"
docker-compose exec web bash -c "./manage.py collectstatic"
docker-compose exec web bash -c "./manage.py createsuperuser"
```
