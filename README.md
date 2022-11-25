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
  

- *Optional*: 
    Run: ```./prestart.sh```
  to populate initialize some data to the database.
  If you get permission error when executing this command, run `chmod +x ./prestart.sh` to add execution permission to the file. The first admin will have the following login info:
    + email: `user@user.user`
    + password: `password`

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
- (coming soon)

# Technologies 🛠️:
- Back-end: Python with FastAPI
- Database: PostgreSQL with SQLAlchemy
- Front-end: Vue.js
