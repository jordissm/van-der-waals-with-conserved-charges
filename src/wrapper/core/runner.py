import subprocess
from pathlib import Path
from rich.progress import track
from .config import Config
from .io import HDF5Handler

class CPPRunner:
    def __init__(self, config: Config, output_file: Path):
        self.cpp_executable = config.external_cpp_app
        self.input_dir = config.cpp_input_dir
        self.output_file = output_file

    def run(self):
        input_files = sorted(self.input_dir.glob('*.txt'))

        if not input_files:
            raise RuntimeError(f"No input files found in {self.input_dir}")

        with HDF5Handler(self.output_file) as h5:
            for input_file in track(input_files, description="Running C++ application..."):
                result = self.execute_cpp(input_file)
                h5.save_result(input_file.stem, input_file, result)

    def execute_cpp(self, input_file: Path) -> str:
        cmd = [str(self.cpp_executable), str(input_file)]
        proc = subprocess.run(cmd, capture_output=True, text=True)

        if proc.returncode != 0:
            raise RuntimeError(f"C++ execution failed for {input_file.name}:\n{proc.stderr}")

        return proc.stdout
