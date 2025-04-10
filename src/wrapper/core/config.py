import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.load()

    def load(self):
        with open(self.config_path) as f:
            data = yaml.safe_load(f)
        self.thermal_fist_executable = Path(data["Thermal-FIST_executable"])
        self.thermal_fist_particle_list_file = Path(data["Thermal-FIST_particle_list_file"])
        self.thermal_fist_vdw_params_dir = Path(data["Thermal-FIST_vdw_params_dir"])
