Do it:

docker-compose -f docker-compose.prod.yml down -v

docker-compose -f docker-compose.prod.yml up -d --build

docker-compose -f docker-compose.prod.yml exec web python manage.py create_db

docker-compose -f docker-compose.prod.yml exec web python manage.py seed_db


And open http://localhost:1337/
