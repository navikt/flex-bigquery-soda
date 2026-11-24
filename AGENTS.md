# AGENTS.md

This file gives instructions to agents that work with code in this repository.

## Overview

This repository runs Soda data-quality checks on BigQuery tables for team Flex.
A Naisjob runs the checks on a schedule. The job sends a Slack alert when a
check fails. The `README.md` is in Norwegian.

The checks use Soda V4 data contracts. Each BigQuery table has one contract.

## Structure

- `nais/naisjob.yaml`: The Naisjob. It uses the `nada-soda-contracts` image.
- `nais/soda-checks-prod.yaml`: The ConfigMap `soda-checks-v4`. It holds the
  production contracts, one data key per contract.
- `nais/soda-config.yaml`: The Soda data source config for production.
- `nais/prod.yaml`: Variables for the scheduled job.
- `nais/prod-run-once.yaml`: Variables for the job that runs once on deploy.
- `local/`: The local runner. It is a development tool, not the production
  entry point.
- `local/soda-checks/`: The local contracts, one YAML file per contract.
- `local/soda-checks.py`: The Python script that runs all local contracts.

## Commands

Set up the local environment once:

```sh
cd local/
poetry env use 3.15
poetry install
```

Run the local checks:

```sh
cd local/
make run-soda-checks
```

The local runner uses Application Default Credentials. It does not publish
results and does not send Slack alerts.

## Deployment

`.github/workflows/deploy.yaml` deploys to `prod-gcp` on push to `main`. It
deploys two jobs: one that runs once and one that runs on a schedule. Changes
only in `local/` do not trigger a deploy.

## Rules

- The local contracts must mirror the production contracts. This includes
  names and thresholds. The format and the files are different, so you must
  update both in the same change.
- The local Soda version (`soda-bigquery` in `local/pyproject.toml`) must match
  the Soda version in the production image. Update both together.
- The data source name is `flex`. Each contract must set
  `dataset: flex/<gcp-project-id>/<bq-dataset>/<table>`.
- Do not rename the ConfigMap `soda-checks-v4` back to `soda-checks`. The old
  name mounts old Soda v3 files on deploy.
- An error about a missing `dataset` (for example in
  `arkivering_oppgave_datastream.yaml`) means that the runner reads an old v3
  file. The v4 contract for that table is `public_oppgavestyring.yaml`.

## Related repositories

- [navikt/flex-bigquery-terraform](https://github.com/navikt/flex-bigquery-terraform):
  Creates the datasets and views that the checks read, for example
  `soda_dataset`.
- [navikt/nada-soda](https://github.com/navikt/nada-soda): The upstream Soda
  runner.

## Glossary

- **Contract**: A Soda V4 data contract. It defines the checks for one
  BigQuery table.
- **Production contracts**: The contracts in `nais/soda-checks-prod.yaml`.
- **Local contracts**: The contracts in `local/soda-checks/`.
- **Avstemming**: Norwegian for reconciliation. Contracts with this word in the
  name compare data between a source database and BigQuery.
