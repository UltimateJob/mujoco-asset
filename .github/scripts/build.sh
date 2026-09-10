#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
set -euo pipefail
mkdir -p .output/payload
git lfs fsck
python3 check_external_models.py
python3 -m json.tool asset-catalog.v1.json >/dev/null
python3 ../automation/.github/scripts/data.py
