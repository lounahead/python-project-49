install: #create poetry dependence
		poetry install

brain-games: #run games
		poetry run brain-games

brain-even:
		poetry run brain-even

brain-calc:
		poetry run brain-calc

brain-gcd:
		poetry run brain-gcd

brain-prog:
		poetry run brain-prog

brain-prime:
		poetry run brain-prime

build: #to build
		poetry build

publish: #to publish
		poetry publish --dry-run

package-install: #reinstall pip
		python3 -m pip install --user  --force-reinstall dist/*.whl

lint:
		poetry run flake8 brain_games		