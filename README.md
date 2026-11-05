# flex-bigquery-soda

Bygger på [nada-soda](https://github.com/navikt/nada-soda) og er tungt inspirert av, og har stålet mye fra, [helse-styringsinfo-kvalitetssjekk](https://github.com/navikt/helse-styringsinfo-kvalitetssjekk).

[Naisjob](https://doc.nais.io/naisjob/) for periodisk kjøring av [Soda](https://www.soda.io/)-sjekker på BigQuery-tabeller. Varsler på Slack ved avvik.

## Utvikling

Prosjektet bruker Soda V4 Data Contracts, med én YAML-fil per BigQuery-tabell.
Produksjon kjører med `nada-soda-contracts`-imaget i [nais/naisjob.yaml](nais/naisjob.yaml).
Kontraktene ligger som separate filer i ConfigMap-en [nais/soda-checks-prod.yaml](nais/soda-checks-prod.yaml).

I mappen [local/](local/) ligger en egen Python-runner og kontrakter for lokal kjøring mot samme BigQuery-prosjekt.
Kontraktene i [local/soda-checks/](local/soda-checks/) skal speile produksjonskontraktene, inkludert terskler og navn.
Ved endringer må begge oppdateres. Datasource-navnet er `flex`, og hver kontrakt angir
`dataset: flex/<gcp-project-id>/<bq-dataset>/<table>`.
Lokal kjøring bruker Application Default Credentials og publiserer ikke resultater eller Slack-varsler.
Den lokale Soda-versjonen er låst til samme versjon som produksjonsimaget; oppdater begge sammen.

Før første gang testene kjøres lokalt må poetry konfigureres:

```sh
cd local/
poetry env use 3.15
poetry install
```

Testene kan deretter kjøres med:

```sh
make run-soda-checks
```

## Aksjoner

Hvis noen av sjekkene som verifiser at det er streamet data til BigQuery feiler kan status på Datastreams sjekkes med:

```cmd
# Sett flex-prod som prosjekt:
gcloud config set project flex-prod-af40

# List datastreams:
gcloud datastream streams list --location=europe-north1 | tr -s ' ' | cut -d ' '  -f1,2
```
Datastreams skal ha status `RUNNING`.


Restart Cloud SQL Proxy hvis noen av datastreamene har status `FAILED`:
```cmd
gcloud compute instances reset flex-datastream-cloud-sql-proxy-vm --zone=europe-north1-a
```

## Avhengigheter

- [Homebrew](https://brew.sh/)

## Ressurser

- [NADA: Kvalitetssikre data med Soda](https://docs.knada.io/dataprodukter/kvalitetssikring/)
- [Soda Data Contract Language](https://docs.soda.io/reference/contract-language-reference)
