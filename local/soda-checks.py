import os
from soda.scan import Scan

import warnings

warnings.filterwarnings("ignore", message='Your application has authenticated using end user credentials', category=Warning)

for file in os.listdir("soda-checks"):
    scan = Scan()
    scan.add_configuration_yaml_file(file_path="soda-config/config.yaml")
    dataset = file.split(".")[0]
    scan.set_data_source_name(dataset)
    scan.add_sodacl_yaml_file(f"soda-checks/{file}")
    scan.execute()

    scan_result = scan.get_scan_results()
    messages = [log["message"] for log in scan_result["logs"]]

    for message in messages:
        print(message)
