import sys
import importlib


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computations",
    "matplotlib.pyplot": "Visualization",
    "requests": "Network access"
}


def check_dependencies() -> dict:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    all_found = True
    found_packages = {}

    for pkg, desc in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {desc} ready")
            found_packages[pkg] = module
        except ImportError:
            print(f"[ERROR] {pkg} is MISSING - {desc} OFFLINE")
            all_found = False

        if not all_found:
            print("\n\033[91m[!] MISSION "
                  "FAILURE: Missing dependencies.\033[0m")
            print("To load via pip:    pip install -r requirements.txt")
            print("To load via Poetry:  poetry install")
            sys.exit(1)

    return found_packages


def run_analysis(modules: dict) -> None:
    pd = modules['pandas']
    np = modules['numpy']
    plt = modules['matplotlib.pyplot']

    print("\nAnalyzing Matrix data...")
    data = pd.DataFrame({
        'Sentinel_Activity': np.random.rand(100),
        'Signal_Strength': np.random.normal(0, 1, 100)
    })
    print(f"Processing {len(data)} data points...")
    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.scatter(data['Sentinel_Activity'],
                data['Signal_Strength'], color='lime', alpha=0.5)
    plt.title("Matrix Sentinel Activity Analysis", color='green')
    plt.xlabel("Activity level")
    plt.grid(True, linestyle='--', alpha=0.6)

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    print(f"Analysis complete!\nResults saved to: {output_file}")


if __name__ == "__main__":
    loaded_modules = check_dependencies()
    run_analysis(loaded_modules)
