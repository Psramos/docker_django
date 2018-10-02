#   ___ _
#   /   (_) __ _ _ __   __ _  ___
#  / /\ / |/ _` | '_ \ / _` |/ _ \
# / /_//| | (_| | | | | (_| | (_) |
#/___,'_/ |\__,_|_| |_|\__, |\___/
#     |__/             |___/

.PHONY: bash build database remove restart stop up

PROJECT := "django"

bash:
	@docker exec -ti django_core bash

build:
	@docker-compose -p $(PROJECT) -f docker-compose.yml up --build -d

database:
	@docker exec -ti django_db mysql -u root  -ppasswd -D core

remove:
	@docker rm django_core django_db

restart:
	@docker restart django_core django_db

stop:
	@docker stop django_core django_db

up:
	@docker-compose -p $(PROJECT) -f docker-compose.yml up -d