
docker-build:
	docker build -t todo-backend .


docker-run:
	docker run -p 5000:5000 todo-backend

docker build-run:
	docker build -t todo-backend . && docker run -p 5000:5000 todo-backend

run:
	pipenv run python src/routes.py
