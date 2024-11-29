import subprocess
import sys
import os
from pathlib import Path

class EnvSetupManager:
    def __init__(self, venv_name="venv", requirements_file="requirements.txt"):
        """
        Initialize the environment manager.

        :param venv_name: Name of the virtual environment directory.
        :param requirements_file: Path to the requirements file.
        """
        self.venv_dir = Path(venv_name)
        self.requirements_file = Path(requirements_file)
        self.python_executable = (
            self.venv_dir / "bin" / "python"
            if os.name != "nt"
            else self.venv_dir / "Scripts" / "python.exe"
        )

    def create_venv(self):
        """Creates a virtual environment in the specified directory."""
        if self.venv_dir.is_dir():
            print(f"Virtual environment already exists at {self.venv_dir}. Skipping creation.")
            return

        print("Creating virtual environment...")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", str(self.venv_dir)])
            print(f"Virtual environment created at {self.venv_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")
            sys.exit(1)

    def update_pip(self):
        """Updates pip in the virtual environment."""
        print("Updating pip...")
        try:
            subprocess.check_call([str(self.python_executable), "-m", "pip", "install", "--upgrade", "pip"])
            print("pip updated successfully.")
        except subprocess.CalledProcessError:
            print("Failed to upgrade pip. Proceeding with existing version.")

    def install_requirements(self):
        """Installs packages from requirements.txt using pip in the virtual environment."""
        if not self.requirements_file.is_file():
            print(f"{self.requirements_file} not found. Skipping package installation.")
            return

        print(f"Installing packages from {self.requirements_file}...")
        try:
            subprocess.check_call([str(self.python_executable), "-m", "pip", "install", "-r", str(self.requirements_file)])
            print("Packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install packages: {e}")

    def setup_environment(self):
        """Sets up the virtual environment and installs requirements."""
        self.create_venv()
        self.update_pip()
        self.install_requirements()