import os
import yaml

import rich

from x_browse.utils import path_to_file, log, log_types


class BrowseModel:

    def __init__(self, yaml_file="data.yaml"):
        try:
            self.yaml_file = path_to_file(yaml_file)

            with open(self.yaml_file, "r") as file:
                self.data = yaml.safe_load(file)

        except FileNotFoundError:
            log(f"{yaml_file} was not found", log_types.ERROR)
        except yaml.YAMLError:
            log(f"{yaml_file} contained yaml errors", log_types.ERROR)
        except:
            log(f"{yaml_file} was found but had another error", log_types.ERROR)
