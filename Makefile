.PHONY: install-backend install-frontend test lint format run

install-backend:
	python -m pip install -r requirements/base.txt -r requirements/dev.txt

install-frontend:
	cd apps/web-dashboard && npm install

test:
	pytest

run:
	docker compose up --build
