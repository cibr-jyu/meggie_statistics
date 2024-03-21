.PHONY: format
format:
	black -t py39 meggie_statistics

.PHONY: check
check:
	black --check -t py39 meggie_statistics
	pylama meggie_statistics

.PHONY: test
test:
	pytest -s
