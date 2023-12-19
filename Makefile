lint:
	black --line-length 79 .
	isort --profile black .
	flake8 --max-doc-length=72