#!/usr/bin/env python3
# Copyright 2026 InsightOS
# SPDX-License-Identifier: Apache-2.0
"""Check required local model files without downloading or licensing any assets."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

REQUIRED = (
    'robot/r1_pro_chassis/config/r1_pro_chassis.xml',
    'robot/r1_pro_chassis/meta.json',
    'robot/r1_pro_tote_gripper/config/r1_pro_tote_gripper.xml',
    'robot/r1_pro_tote_gripper/config/semantic_robot_profile.yaml',
)

def check(root):
    failures = []
    for name in REQUIRED:
        path = root / name
        if not path.is_file():
            failures.append(name + ': missing')
            continue
        with path.open('rb') as stream:
            pointer = stream.read(100).startswith(b'version https://git-lfs.github.com/spec/v1')
        if pointer:
            failures.append(name + ': unresolved LFS pointer')
        elif path.suffix == '.xml':
            try:
                ET.parse(path)
            except (ET.ParseError, OSError):
                failures.append(name + ': invalid XML')
    return failures

if __name__ == '__main__':
    failures = check(Path(__file__).resolve().parent)
    if failures:
        print('R1 Pro models are external and not included. See EXTERNAL_MODELS.md.', file=sys.stderr)
        print('Official source: https://github.com/userguide-galaxea/URDF/tree/galaxea/main/R1Pro', file=sys.stderr)
        for failure in failures:
            print('  ' + failure, file=sys.stderr)
    else:
        print('Local model entry files found; validate meshes, licensing and simulation separately.')
    sys.exit(1 if failures else 0)
