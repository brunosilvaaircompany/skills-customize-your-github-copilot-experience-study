from pathlib import Path
import shutil
import sys


def extension_category(file_path):
    """Return a lowercase extension without its dot."""
    pass


def organize_folder(folder_path):
    """Organize files in folder_path and return moved and conflict counts."""
    pass


def main():
    if len(sys.argv) != 2:
        print("Uso: python starter-code.py <pasta>")
        return

    folder_path = Path(sys.argv[1])
    moved_count, conflict_count = organize_folder(folder_path)
    print(f"Arquivos movidos: {moved_count}")
    print(f"Conflitos: {conflict_count}")


if __name__ == "__main__":
    main()
