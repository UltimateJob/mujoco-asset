#!/usr/bin/env python3
# Copyright 2026 InsightOS
# SPDX-License-Identifier: Apache-2.0
"""Check downloaded model entry files and their referenced assets; no downloads."""
import json
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
    root = Path(root).resolve()
    failures = []
    seen = set()

    def inspect(path, parse_xml=False):
        path = path.resolve()
        if not path.is_relative_to(root):
            failures.append('model reference escapes asset repository')
            return
        name = path.relative_to(root).as_posix()
        if (name, parse_xml) in seen:
            return
        seen.add((name, parse_xml))
        if not path.is_file():
            failures.append(name + ': missing')
            return
        with path.open('rb') as stream:
            header = stream.read(100)
        if not header:
            failures.append(name + ': empty file')
        elif header.startswith(b'version https://git-lfs.github.com/spec/v1'):
            failures.append(name + ': unresolved LFS pointer')
        elif parse_xml:
            try:
                tree = ET.parse(path).getroot()
            except (ET.ParseError, OSError):
                failures.append(name + ': invalid XML')
                return
            compiler = tree.find('compiler')
            attrs = compiler.attrib if compiler is not None else {}
            for element in tree.iter():
                filename = element.get('file')
                if not filename:
                    continue
                if element.tag == 'include':
                    inspect(path.parent / filename, True)
                elif element.tag in ('mesh', 'skin', 'hfield', 'texture'):
                    directory = attrs.get('texturedir' if element.tag == 'texture' else 'meshdir', attrs.get('assetdir', ''))
                    inspect(path.parent / directory / filename)
        elif path.suffix == '.json':
            try:
                json.loads(path.read_text())
            except (ValueError, OSError):
                failures.append(name + ': invalid JSON')

    for name in REQUIRED:
        inspect(root / name, name.endswith('.xml'))
    return failures

if __name__ == '__main__':
    failures = check(Path(__file__).resolve().parent)
    if failures:
        print('error: R1 Pro model files are missing or invalid. Run git lfs pull -I "" -X ""; see EXTERNAL_MODELS.md.', file=sys.stderr)
        print('Official source: https://github.com/userguide-galaxea/URDF/tree/galaxea/main/R1Pro', file=sys.stderr)
        for failure in failures:
            print('  ' + failure, file=sys.stderr)
    else:
        print('R1 Pro entry files and referenced assets are ready; validate simulation separately.')
    sys.exit(1 if failures else 0)
