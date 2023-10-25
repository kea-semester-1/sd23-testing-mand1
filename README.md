[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=testing-mand1_data-faker&metric=coverage)](https://sonarcloud.io/summary/new_code?id=testing-mand1_data-faker)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=testing-mand1_data-faker&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=testing-mand1_data-faker)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=testing-mand1_data-faker&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=testing-mand1_data-faker)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=testing-mand1_data-faker&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=testing-mand1_data-faker)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=testing-mand1_data-faker&metric=bugs)](https://sonarcloud.io/summary/new_code?id=testing-mand1_data-faker)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=testing-mand1_data-faker&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=testing-mand1_data-faker)
# data_faker

This project is the first mandatory assignment, for the SD23 testing subject.

## Prerequisites
* Docker

## Commands

* `make run` -> Run the application
* `make test` -> Run the tests
* `make lint` -> Run the linters

If `make` does not work for you, you can copy paste the commands from the `Makefile`.

`make run` = `docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build`
