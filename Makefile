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
	docker container exec $$(docker ps | grep api-1 | awk '{print $$1}') pytest ./data_faker/tests -s -v

migration-generate:  ## Generate a new migration file
	@echo "Running migration"
	docker container exec $$(docker ps | grep sd23-testing-mand1-api-1 | awk '{print $$1}') alembic revision --autogenerate

migration-upgrade-head:  ## Upgrade to the latest migration
	docker container exec $$(docker ps | grep sd23-testing-mand1-api-1 | awk '{print $$1}') alembic upgrade head

test-filter:  ## Run specific tests. Example: 'make test-filter filter="test_phone_numbers"'.
	@echo "Running tests..."
	docker container exec $$(docker ps | grep api-1 | awk '{print $$1}') pytest ./data_faker/tests -s -v -k $(filter)
