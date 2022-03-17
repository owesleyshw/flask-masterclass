.PHONY: test
test:
	FLASK_ENV=testing ward test

.PHONY: check
check:
	black . -l 79