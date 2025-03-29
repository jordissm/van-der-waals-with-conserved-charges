import subprocess
from pathlib import Path
from rich.progress import track
from .config import Config
from .io import HDF5Handler

class CPPRunner:
    def __init__(self, config: Config, output_file: Path):
        self.thermal_fist_executable = config.thermal_fist_executable
        self.vdw_params_dir = config.vdw_params_dir
        self.output_file = output_file

    def run(self):
        input_files = sorted(self.vdw_params_dir.glob('*.txt'))

        if not input_files:
            raise RuntimeError(f"No input files found in {self.vdw_params_dir}")

        with HDF5Handler(self.output_file) as h5:
            for input_file in track(input_files, description="Running Thermal-FIST application..."):
                result = self.execute_thermal_fist(input_file)
                h5.save_result(input_file.stem, input_file, result)

    def execute_thermal_fist(self, input_file: Path) -> str:
        cmd = [str(self.thermal_fist_executable), '1', str(input_file)]
        proc = subprocess.run(cmd, capture_output=True, text=True)

        if proc.returncode != 0:
            raise RuntimeError(f"Thermal-FIST execution failed for {input_file.name}:\n{proc.stderr}")

        return proc.stdout
