import h5py
from pathlib import Path

class HDF5Handler:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)  # Ensures the directory exists

    def __enter__(self):
        self.h5file = h5py.File(self.filepath, 'w')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.h5file.close()

    def save_result(self, label: str, input_file: Path, result: str):
        grp = self.h5file.create_group(label)
        grp.create_dataset("input_file_name", data=input_file.name)
        # Filter out header, warning, and blank lines
        cleaned_lines = []
        for line in result.splitlines():
            stripped_line = line.strip()
            if not stripped_line or stripped_line.startswith('#') or stripped_line.startswith('**'):
                continue
            cleaned_lines.append(line)
        cleaned_result = "\n".join(cleaned_lines)
        grp.create_dataset("output", data=cleaned_result.encode('utf-8'))
