import os
import sys
import csv

def print_error_and_files(path):
    print(f"Error: '{path}' does not exist or is not a file.")
    dir_path = os.path.dirname(path) or '.'
    print("Files in directory:")
    for fname in os.listdir(dir_path):
        print(fname)

def main():
    if len(sys.argv) < 4:
        print("Usage: python reader.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        print_error_and_files(src)
        sys.exit(1)

    with open(src, newline='') as f:
        reader = list(csv.reader(f))

    for change in changes:
        try:
            col, row, value = change.split(',', 2)
            col = int(col)
            row = int(row)
            if row < 0 or row >= len(reader):
                print(f"Invalid row index in change '{change}'. Skipping.")
                continue
            if col < 0 or col >= len(reader[row]):
                print(f"Invalid column index in change '{change}'. Skipping.")
                continue
            reader[row][col] = value
        except Exception as e:
            print(f"Invalid change argument '{change}': {e}. Skipping.")

    for row in reader:
        print(','.join(row))

    try:
        with open(dst, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(reader)
        print(f"Modified CSV saved to {dst}")
    except Exception as e:
        print(f"Error saving to '{dst}': {e}")

if __name__ == "__main__":
    main()