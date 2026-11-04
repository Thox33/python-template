FROM python:3.15-alpine3.24

# uv comes from its own published image rather than a curl|sh installer, so the
# version is pinned, verifiable and bumpable by dependabot.
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /uvx /usr/local/bin/

# Keep the project environment at a fixed path and put it on PATH, so the
# installed console scripts are available without activating anything.
ENV UV_PROJECT_ENVIRONMENT=/usr/src/app/.venv \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/usr/src/app/.venv/bin:${PATH}"

# Non root user for safety
RUN adduser -D nonroot \
    && mkdir -p /usr/src/app \
    && chown nonroot:nonroot /usr/src/app
USER nonroot

WORKDIR /usr/src/app

# Install the dependencies on their own layer first, so editing the sources
# does not invalidate the expensive part of the build.
COPY --chown=nonroot:nonroot pyproject.toml uv.lock README.md ./
RUN uv sync --locked --all-extras --no-install-project

# Then add the project itself.
COPY --chown=nonroot:nonroot src ./src
COPY --chown=nonroot:nonroot tests ./tests
RUN uv sync --locked --all-extras

# The environment is already in place, so commands must not trigger another
# sync (which would need network access and could fight the mounted sources).
ENTRYPOINT ["uv", "run", "--no-sync"]
