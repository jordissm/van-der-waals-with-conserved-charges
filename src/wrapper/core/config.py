import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.load()

    def load(self):
        with open(self.config_path) as f:
            data = yaml.safe_load(f)
        self.external_cpp_app = Path(data["external_cpp_app"])
        self.cpp_input_dir = Path(data["cpp_input_dir"])
