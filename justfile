default: build

@build:
    rm -rf dist
    uv build

@format:
    uv run black .

@lint:
    uv run pylint ./seam ./test
    uv run black --check .
    uv run rstcheck README.rst
    uv run mypy seam/resources --disable-error-code=arg-type --disable-error-code=import-not-found

@test:
    uv run pytest --cov=./seam

@watch:
    uv run ptw

@version:
    git add pyproject.toml uv.lock
    git commit -m "$(uv version --short)"
    git tag --sign "v$(uv version --short)" -m "$(uv version --short)"
    git push --follow-tags
