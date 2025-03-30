import h5py
from pathlib import Path

def hdf5_to_console(hdf5_path: Path):
    with h5py.File(hdf5_path, 'r') as h5file:
        for group_name in h5file:
            grp = h5file[group_name]

            input_file_name = grp['input_file_name'][()].decode('utf-8')
            output_result = grp['output'][()].decode('utf-8')

            print(f"=== {group_name} ===")
            print(f"Input File: {input_file_name}")
            print("Output Result:")
            print(output_result)
            print()

if __name__ == "__main__":
    hdf5_file = Path("output/results.h5")

    hdf5_to_console(hdf5_file)
