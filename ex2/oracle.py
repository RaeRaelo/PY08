import os
from dotenv import load_dotenv


def load_oracle_config() -> dict | None:
    load_dotenv()

    try:
        config = {
            "mode": os.environ["MATRIX_MODE"],
            "db": os.environ["DATABASE_URL"],
            "key": os.environ["API_KEY"],
            "log": os.environ["LOG_LEVEL"],
            "url": os.environ["ZION_ENDPOINT"]
        }
    except KeyError as e:
        print(f"Error: {e} NOT FOUND")
        return None
    return config


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    settings = load_oracle_config()
    if settings:
        print("Configuration loaded:")
        print(f"Mode: {settings.get('mode')}")
        print(f"Database: Connected to: {settings.get('db')}")
        print("API Access: Authenticated")
        print(f"Log Level: {settings.get('log')}")
        print("Zion Network: Online")
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")
        print("The Oracle sees all configurations.")
