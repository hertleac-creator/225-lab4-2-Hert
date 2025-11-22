#!/usr/bin/env python3
import sqlite3
import random
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
#  Generate Warhammer Data
# ===========================
def generate_test_data(num_records):
    db = connect_db()

    factions = [
        "Space Marines",
        "Astra Militarum",
        "Tyranids",
        "Necrons",
        "Orks",
        "Adeptus Mechanicus",
        "Chaos",
        "Tau Empire",
        "Eldar"
    ]

    print("\n⚔️ The Forge of Data is Lit — Generating models for the battlefield...\n")

    for i in range(num_records):
        model = f"Model Squad {i+1}"
        faction = random.choice(factions)
        painted = random.randint(0, 1)
        owned = random.randint(1, 50)

        db.execute(
            "INSERT INTO warhammer (model_name, faction, painted, models_owned) VALUES (?, ?, ?, ?)",
            (model, faction, painted, owned)
        )

        print(f"  ✔ Deployed {model} for {faction} — "
              f"{'Painted' if painted else 'Unpainted'}, {owned} models owned.")

    db.commit()
    db.close()

    print(f"\n🛡️ Deployment Complete — {num_records} new entries logged in the Chapter Records.\n")


# ===========================
#  Main Execution
# ===========================
if __name__ == "__main__":
    if not os.path.exists(os.path.dirname(DATABASE)):
        os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    init_db()
    generate_test_data(10)
