#### Local installation
To install this project you need:
1. Poetry (https://python-poetry.org/docs/#installation)
2. pyenv (optional)

#### Installation steps:
1. `cd` into project root
2. Run: `poetry install`

If you're running on Windows, you might need to delete `poetry.lock` and generate it again.
To re-create lockfile after it was deleted run: `poetry update`


#### Run tests:
1. `cd` into project root
2. Run: `poetry run pytest .`