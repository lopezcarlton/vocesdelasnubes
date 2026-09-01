#!/usr/bin/env python3
"""Small consistency checks for artifacts explicitly migrated to the repo."""

from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GENERATOR_DIR = ROOT / "dispositivo" / "generator"
RUNTIME_DIR = ROOT / "dispositivo" / "runtime" / "v0_2_15_3"
ANALYZER_DIR = ROOT / "dispositivo" / "analyzer"
sys.path.insert(0, str(GENERATOR_DIR))

from generator_v0_5_migrated_adapter import migrated_execution_state  # noqa: E402


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class MigratedStateTests(unittest.TestCase):
    def test_exact_sqlite_and_critical_tables(self) -> None:
        path = RUNTIME_DIR / "BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite"
        self.assertEqual(
            sha256(path),
            "2379773426baf4e3eace87c61ec17f7a1e1b9164421e56cf736d35eb64a5ebed",
        )
        connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        try:
            self.assertEqual(connection.execute("PRAGMA integrity_check").fetchone()[0], "ok")
            self.assertEqual(connection.execute("PRAGMA foreign_key_check").fetchall(), [])
            self.assertEqual(
                connection.execute("SELECT COUNT(*) FROM canonical_state_v17").fetchone()[0],
                22,
            )
            tables = {
                row[0]
                for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                )
            }
            self.assertIn("verb_lexeme_class_v023", tables)
            self.assertIn("person_possession_exact_v0214", tables)
        finally:
            connection.close()

    def test_exact_verb_inventory(self) -> None:
        path = ANALYZER_DIR / "DIC_VERB_2385_v0_1.csv"
        self.assertEqual(
            sha256(path),
            "2bdf4afd4b61234c54585cda17ad648bfb71194e9463d193eb04a5a06aa3183d",
        )
        with path.open(encoding="utf-8-sig", newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertEqual(len(rows), 2385)
        self.assertEqual(len({row["entry_id"] for row in rows}), 2385)

    def test_generator_migrated_subset_instantiates(self) -> None:
        state = migrated_execution_state()
        self.assertEqual(state["status"], "MIGRATED_SUBSET_INSTANTIATES")
        self.assertEqual(state["paradigm_cells"], 72)
        self.assertEqual(state["construction_inventory"], 6)
        self.assertEqual(state["generation_licenses"], 6)
        self.assertEqual(state["active_license_constructions"], ["C01", "C02"])
        self.assertEqual(sorted(state["integration_blockers"]), ["C03", "C04", "C05", "C06"])
        self.assertFalse(state["research_authority_assertion"])

    def test_release_manifest_records_sqlite_and_known_integrity_mismatch(self) -> None:
        manifest = json.loads(
            (RUNTIME_DIR / "RELEASE_FILE_MANIFEST_v0_2_15_3.json").read_text(encoding="utf-8")
        )
        expected = manifest["sha256"]
        sqlite_name = "BASE_CORRECTOR_DIDXAZA_SURFACE_SEMANTICS_v2_20.sqlite"
        integrity_name = "DB_INTEGRITY_v0_2_15_3.json"
        self.assertEqual(sha256(RUNTIME_DIR / sqlite_name), expected[sqlite_name])
        self.assertEqual(
            sha256(RUNTIME_DIR / integrity_name),
            "bcd0cf4046eb0d949dce29f098bd5d5f5e9e657f2636ce592f76ddcbd082eae4",
        )
        self.assertNotEqual(sha256(RUNTIME_DIR / integrity_name), expected[integrity_name])


if __name__ == "__main__":
    unittest.main()
