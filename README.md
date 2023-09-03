# flex-bigquery-soda

Bygger på [nada-soda](https://github.com/navikt/nada-soda) og er tungt inspirert av, og har stålet mye fra, [helse-styringsinfo-kvalitetssjekk](https://github.com/navikt/helse-styringsinfo-kvalitetssjekk).

[Naisjob](https://doc.nais.io/naisjob/) for periodisk kjøring av [Soda](https://www.soda.io/)-sjekker på BigQuery-tabeller. Varsler på Slack-kanalen `#flex-dev`` ved avvik.

## Utvikling

I mappen [local/](local/) ligger det filer som kan brukes til å kjøre Soda-sjekker fra lokal maskin. Sjekkene som ligger her er ikke de samme som kjøres av naisjobben, og er i all hovedak ment for testing av tester i forbindelse med utvikling. Sjekkene i `local/` kan kun kjøres mot `dev`.

Testene kjøres med:

```sh
cd local
make run-soda
```

## Avhengigheter

- [Homebrew](https://brew.sh/)

## Ressurser

[List of SodaCL metrics and checks](https://docs.soda.io/soda-cl/metrics-and-checks.html#list-of-sodacl-metrics-and-checks)
