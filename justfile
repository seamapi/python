default: build

@build:
    rm -rf dist
    poetry build

@format:
    poetry run black .

@lint:
    poetry run pylint ./seam ./test
    poetry run black --check .
    poetry run rstcheck README.rst
    poetry run mypy seam/resources --disable-error-code=arg-type --disable-error-code=import-not-found

@test:
    poetry run pytest --cov=./seam

@watch:
    poetry run ptw

@version:
    git add pyproject.toml
    git commit -m "$(poetry version -s)"
    git tag --sign "v$(poetry version -s)" -m "$(poetry version -s)"
    git push --follow-tags
