import os
import yaml
import logging.config
import logging


def setup_logging(default_path="log-config.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = os.getenv(env_key, None) or default_path
    if os.path.exists(path):
        with open(path, "rt") as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print("Error in Logging Configuration. Using default configs")
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print("Failed to load configuration file. Using default configs")

