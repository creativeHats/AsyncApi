import os
import yaml


class Config:
    """
    This class is used to setup configurations.
    To get the configs object

    Example :
        configs = get_configs()

    """
    configs = None

    def setup_config(self, config_path):
        """
        Setup  configuration and returns array of config values
        """
        if os.path.exists(config_path):
            with open(config_path, 'rt') as f:
                configs = yaml.safe_load(f.read())
        else:
            raise ValueError("Config file does not exist " + config_path)

        return configs

