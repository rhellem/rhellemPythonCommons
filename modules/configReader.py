import yaml
import os
from copy import deepcopy

class ConfigReader:
    def __init__(self, config_path):
        """
        Initializes the ConfigReader with the path to the YAML configuration file.
        
        :param config_path: Path to the YAML configuration file.
        """
        self.config_path = config_path
        self.config_data = self._load_config()
        

    def _load_config(self):
        """
        Loads the YAML configuration file.
        
        :return: Parsed YAML data as a dictionary.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def get_database_config(self, db_name):
        """
        Retrieves the database configuration for a specific database name.

        :param db_name: Name of the database (key in the YAML file).
        :return: Dictionary containing database connection parameters.
        """
        if db_name not in self.config_data:
            raise ValueError(f"Database configuration for '{db_name}' not found in the config file.")
        
        config = self.config_data[db_name]
        
        # Return the unmasked configuration
        return config