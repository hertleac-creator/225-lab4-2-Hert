import unittest
import sqlite3
import os

DB_PATH = '/nfs/demo.db'  # Your SQLite database


class DatabaseLightTests(unittest.TestCase):

    def test_database_exists(self):
        """Check that the SQLite database file exists"""
        self.assertTrue(
            os.path.exists(DB_PATH),
            f"Database file not found at {DB_PATH}"
        )

    def test_warhammer_table_exists(self):
        """Check that the 'warhammer' table exists in the database"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' 
            AND name='warhammer';
        """)
        table = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(
            table,
            "warhammer table does NOT exist in the database"
        )

    def test_warhammer_has_required_columns(self):
        """Ensure required fields exist"""
        required_columns = {
            'id',
            'model_name',
            'faction',
            'painted',
            'models_owned'
        }

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(warhammer);")
        columns = {row[1] for row in cursor.fetchall()}
        conn.close()

        missing = required_columns - columns

        self.assertTrue(
            len(missing) == 0,
            f"Missing required columns in warhammer table: {missing}"
        )

    def test_sample_data_exists(self):
        """Check at least one row exists in warhammer table"""
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM warhammer LIMIT 1;")
        row = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(
            row,
            "No rows found in warhammer table — did data-gen.py run?"
        )


if __name__ == "__main__":
    unittest.main()
