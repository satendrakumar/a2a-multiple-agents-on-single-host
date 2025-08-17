FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files first for better caching
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-cache

# Copy code
COPY src ./src

COPY main.py .

COPY start.sh .

RUN chmod +x ./start.sh

# Use the startup script
CMD ["./start.sh"]