# Copyright 2026 InsightOS
# SPDX-License-Identifier: Apache-2.0
import json
from pathlib import Path
import tempfile
import unittest

from check_external_models import REQUIRED, check


class ExternalModelsTests(unittest.TestCase):
    def test_missing_models_have_explicit_diagnostics(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(len(check(Path(directory))), len(REQUIRED))

    def test_entry_files_do_not_claim_mesh_or_license_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in REQUIRED:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('<mujoco/>' if path.suffix == '.xml' else '{}')
            self.assertEqual(check(root), [])
            (root / REQUIRED[0]).write_text('<broken>')
            self.assertIn('invalid XML', check(root)[0])
            (root / REQUIRED[0]).write_text('version https://git-lfs.github.com/spec/v1\n')
            self.assertIn('LFS pointer', check(root)[0])

    def test_public_catalog_preserves_third_party_scope(self):
        root = Path(__file__).resolve().parents[1]
        catalog = json.loads((root / 'asset-catalog.v1.json').read_text())
        self.assertEqual({e['catalog_id'] for e in catalog['entries']}, {'r1-pro-chassis', 'box', 'pallet', 'target'})
        self.assertTrue(all(e['distribution_status'] == 'redistributable' for e in catalog['entries']))
        robot = next(e for e in catalog['entries'] if e['catalog_id'] == 'r1-pro-chassis')
        self.assertIn('ASSET_PROVENANCE.md', robot['license'])
        self.assertNotEqual(robot['license'], 'Apache-2.0')

    def test_mesh_missing_pointer_and_payload(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in REQUIRED:
                p = root / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('<mujoco/>' if name.endswith('.xml') else '{}')
            model = root / REQUIRED[0]
            model.write_text('<mujoco><compiler meshdir="../meshes"/><asset><mesh file="base.STL"/></asset></mujoco>')
            mesh = model.parent.parent / 'meshes/base.STL'
            self.assertIn('base.STL: missing', check(root)[0])
            mesh.parent.mkdir()
            mesh.write_text('version https://git-lfs.github.com/spec/v1\n')
            self.assertIn('LFS pointer', check(root)[0])
            mesh.write_bytes(b'mesh payload')
            self.assertEqual(check(root), [])

    def test_include_outside_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in REQUIRED:
                p = root / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('<mujoco/>' if name.endswith('.xml') else '{}')
            (root / REQUIRED[0]).write_text('<mujoco><include file="../../../../outside.xml"/></mujoco>')
            self.assertIn('escapes', check(root)[0])

if __name__ == '__main__':
    unittest.main()
