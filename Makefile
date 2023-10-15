lint: ## Run linter
	@echo "Running linter..."
	poetry run black .
	poetry run ruff --fix .
	poetry run mypy .

run: ## Run the application
	@echo "Running application..."
	docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build

test: ## Run tests
	@echo "Running tests..."
	docker container exec $$(docker ps | grep api-1 | awk '{print $$1}') pytest ./rpg_api/tests