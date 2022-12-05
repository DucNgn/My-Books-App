# My Book App


# Without Docker 🚫🐳

## Backend 

#### Requirements:
- Python 3.9+

#### Steps:

- Start the Postgresql Database: `docker-compose up db` from the main directory.
- 2 options to install dependencies

1. With Poetry (recommended, install [Poetry](https://python-poetry.org))
- `cd backend` to change directory to the backend folder.
- `poetry shell` to activate a virtual shell for the back-end.
- `poetry install` to install Python dependencies.

2. Without Poetry:
- `cd backend` to change directory to the backend folder.
- `python -m venv .venv` to create a virtual environment.
- `source .venv/bin/activate` to activate the virtual environment.
- `pip install -r requirements.txt` to install the dependencies.
  

3. Run: ```./prestart.sh```
  to populate initialize some data to the database.
  If you get permission error when executing this command, run `chmod +x ./prestart.sh` to add execution permission to the file. The first admin will have the following login info:
  - Admin user:
    + email: `user@user.user`
    + password: `password`
  - Test user 1:
    + email: `william.arbour@gmail.com`
    + password: `costion`
  - Test user 2:
    + email: `ana.miranda@gmail.com`
    + password: `teranda`

- ```bash -c "uvicorn backend.main:app --host 0.0.0.0 --port 8000"``` : To start the back-end.

The back-end starts at localhost:8000 by default. 

In addition, localhost:8000/docs has the swagger ui for the back-end API.

## Frontend

#### Requirements:
- Node 10 (recommend to use [fnm](https://github.com/Schniz/fnm) or [nvm](https://github.com/nvm-sh/nvm) to manage node version)

#### Steps:

- `cd frontend` to change directory to the frontend folder.
- `npm i` to install node dependencies.
- `npm run serve` to start the server with hot reload.

By default, front-end starts at localhost:8080.

# With Docker 🐳
- `docker-compose up`: To start all the containers.
- `docker-compose up --build`: To rebuild if there's any changes.

# During Development:
- `make lint-backend`: to run linter through all backend code (all dependencies needed to be installed inside `./venv`)
- `make lint-frontend`: to run linter through all frontend code (all dependencies needed to be installed inside `node_modules`)
- `poetry export -f requirements.txt --output requirements.txt` to export all poetry dependencies to requirements.txt file

# Testing 🧪
While inside virtual environment created by Poetry. 
- `cd backend` to change directory to the backend folder (the directory that contains `pyproject.toml`)
- `poetry run pytest` to run all tests.
- `poetry run pytest -k "prefix_of_your_test_name"` to run a subset of test cases.
  - Example: If run `poetry run pytest -k "test_check"`, that will run 2 tests: `test_check_user_created` and `test_check_shelves_have_books`, but not `test_create_user`

# Technologies 🛠️:
- Back-end: Python with FastAPI
- Database: PostgreSQL with SQLAlchemy
- Front-end: Vue.js
