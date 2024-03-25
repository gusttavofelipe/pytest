run-tests:
	python -m pytest ./tests -vv

test-matching:
	python -m pytest ./tests -vv -k $(K)

test-dir:
	python -m pytest ./tests/$(D) -vv
