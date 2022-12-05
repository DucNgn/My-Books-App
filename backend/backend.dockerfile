FROM python:3.10

WORKDIR /backend/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

# Configure Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
RUN poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* ./

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

ENV PYTHONPATH=/backend
COPY ./ /backend
