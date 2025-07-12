FROM astral/uv:python3.11-bookworm-slim

WORKDIR /app
COPY . /app

RUN uv venv
RUN . /app/.venv/bin/activate && uv pip install --upgrade pip
RUN uv pip install -r requirements.txt

EXPOSE 5006
