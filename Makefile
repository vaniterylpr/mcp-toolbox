.PHONY: test lint run

test:
	python -m pytest -q

lint:
	python -m compileall -q .

run:
	# claude_desktop_config.json
