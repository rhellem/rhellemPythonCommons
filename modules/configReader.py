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

    def _get_masked_config(self):
        """
        Returns a copy of the configuration data with masked passwords for display purposes.
        
        :return: A dictionary with masked passwords.
        """
        masked_config = deepcopy(self.config_data)  # Create a deep copy to avoid modifying the original data
        for db, values in masked_config.items():
            if "password" in values:
                values["password"] = "****"
        return masked_config


    def get_database_config(self, db_name):
        """
        Retrieves the database configuration for a specific database name.
        
        :param db_name: Name of the database (key in the YAML file).
        :return: Dictionary containing database connection parameters (host, user, password, name).
        """
        if db_name not in self.config_data:
            raise ValueError(f"Database configuration for '{db_name}' not found in the config file.")
        return self.config_data[db_name]
    
    def __str__(self):
        """
        Custom string representation of the object for printing, showing the masked configuration data.
        """
        return f"ConfigReader({self._get_masked_config()})"
    
    def __repr__(self):
        """
        Custom string representation of the object, showing the masked configuration data.
        """
        return f"ConfigReader({self._get_masked_config()})"
