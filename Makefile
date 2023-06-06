postgres:
	docker run --name pdb -e POSTGRES_PASSWORD='qwerty' -d --rm -p5432:5432 postgres

test:
	pytest ./tests/test.py

web:
	docker compose up --build
