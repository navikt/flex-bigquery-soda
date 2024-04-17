# Definerer alle tasks som .PHONY.
.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))

help:
	 @echo "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

bootstrap: ## Sikrer at poetry finnes.
	@jq --version || brew install jq
	@poetry --version || brew install poetry
	poetry update

run-soda-checks: ## Autentiserer mot GCP og kjører Soda-sjekker.
	@gcloud --format=json auth list | jq --exit-status '.[] | select(.status == "ACTIVE")' || gcloud auth application-default login
	poetry run python ./soda-checks.py
