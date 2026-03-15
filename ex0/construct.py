import sys
import os
import site


def is_venv():
    if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
        return True
    if hasattr(sys, 'real_prefix'):
        return True
    if 'VIRTUAL_ENV' in os.environ:
        return True
    return False


def main():
    if not is_venv():
        print("MATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("\033[91m[!] WARNING: You're in the global environment! \033[0m")
        print("The machines can see everithing you install.")
        print("\nTo initialize the environment, run:")
        print(" python3 -m venv matrix_env")
        print(" source matrix_env/bin/activate  # On Unix")
        print(" matrix_env\\Scripts\\activate   # On Windows")
        print('\nThen run this program again.')
    else:
        venv_name = os.path.basename(sys.prefix)
        package_path = (site.getsitepackages()[0]
                        if hasattr(site, 'getsitepackages') else "N/A")
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\n\033[32m SUCCESS: You're in an isolated environment! \033[0m")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(f"{package_path}")


if __name__ == "__main__":
    main()
