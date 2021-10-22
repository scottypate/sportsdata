.PHONY: clean-sdk
clean-sdk:
	rm -rf .swagger-codegen docs sportsdata test .gitignore .swagger-codegen-ignore README.md requirements.txt setup.py test-requirements.txt

.PHONY: generate-sdk
generate-sdk:
	./build_sdks.sh
	rm .travis.yml git_push.sh tox.ini

.PHONY: run-tests
run-tests:
	pytest ./test