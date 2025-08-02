FROM python:3.13-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]


# FROM python:3.13-slim-bookworm

# COPY --from=ghcr.io/astral-sh/uv:0.8.4 /uv /uvx /bin/

# # Copy the project into the image
# ADD . /app

# # Sync the project into a new environment, asserting the lockfile is up to date
# WORKDIR /app
# RUN uv sync --locked

# CMD ["uv", "run", "app.py"]





