install: #create dependence
		poetry install

brain-games: #run games
		poetry run brain-games

build: #to build
		poetry build

publish: #to publish
		poetry publish --dry-run

package-install: #install pip
		python3 -m pip install --user dist/*.whl
