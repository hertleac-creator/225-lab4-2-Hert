#!/usr/bin/env python3
import sqlite3
import os

DATABASE = "/nfs/demo.db"

# ===========================
#  Connect to the Database
# ===========================
def connect_db():
    return sqlite3.connect(DATABASE)


# ===========================
#  Initialize Table if Missing
# ===========================
def init_db():
    db = connect_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS warhammer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            faction TEXT NOT NULL,
            painted INTEGER NOT NULL,
            models_owned INTEGER NOT NULL
        );
    """)
    db.commit()
    db.close()


# ===========================
#  Generate Selenium-Friendly Warhammer Data
# ===========================
def generate_test_data(num_records):
    db = connect_db()

    print("\n⚔️ Generating test models for Selenium…\n")

    for i in range(num_records):
        model = f"Test Model {i}"
        faction = f"Faction {i}"
        painted = 1  # Always painted for simplicity
        owned = 10   # Arbitrary number

        db.execute(
            "INSERT INTO warhammer (model_name, faction, painted, models_owned) VALUES (?, ?, ?, ?)",
            (model, faction, painted, owned)
        )

        print(f"  ✔ Added {model} ({faction}) — Painted: {painted}, Owned: {owned}")

    db.commit()
    db.close()

    print(f"\n🛡️ Test data generation complete — {num_records} entries added.\n")


# ===========================
#  Main Execution
# ===========================
if __name__ == "__main__":
    # Ensure database folder exists
    if not os.path.exists(os.path.dirname(DATABASE)):
        os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    init_db()
    generate_test_data(10)
