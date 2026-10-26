.PHONY: build up down logs ps check migrate makemigrations shell dbshell superuser

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

check:
	docker compose exec web python manage.py check

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

shell:
	docker compose exec web python manage.py shell

dbshell:
	docker compose exec db sh -c 'psql -U "$$POSTGRES_USER" -d "$$POSTGRES_DB"'

superuser:
	docker compose exec web python manage.py createsuperuser
