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
        self._mask_passwords()  # Automatically mask passwords on initialization
        
        
    def _mask_passwords(self):
        """
        Masks the password fields in the loaded configuration data by replacing their
        values with '****'.
        """
        for db, values in self.config_data.items():
            if "password" in values:
                values["password"] = "****"
                
    def __repr__(self):
        """
        Custom string representation of the object, showing the masked configuration data.
        """
        return f"ConfigReader({self.config_data})"
    
    def _load_config(self):
        """
        Loads the YAML configuration file.
        
        :return: Parsed YAML data as a dictionary.
        # Assume the YAML config file is named "db_config.yaml" and looks like this:
        my_database:
             host: localhost
             user: admin
             password: secret
             name: my_database
         other_database:
             host: 192.168.1.10
             user: user2
             password: password2
             name: other_db

        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def get_database_config(self, db_name):
        """
        Retrieves the database configuration for a specific database name.
        
        :param db_name: Name of the database (key in the YAML file).
        :return: Dictionary containing database connection parameters (host, user, password, name).
        """
        if db_name not in self.config_data:
            raise ValueError(f"Database configuration for '{db_name}' not found in the config file.")

        return self.config_data[db_name]

