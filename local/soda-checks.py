import logging
import warnings
from pathlib import Path

from soda_core.contracts import verify_contract_locally

warnings.filterwarnings("ignore", message='Your application has authenticated using end user credentials', category=Warning)
logging.basicConfig(level=logging.INFO)

local_dir = Path(__file__).resolve().parent

for contract in sorted((local_dir / "soda-checks").glob("*.yaml")):
    logging.info("Running contract %s", contract.name)
    verify_contract_locally(
        contract_file_path=str(contract),
        data_source_file_path=str(local_dir / "soda-config/config.yaml"),
    )
