[English](EXTERNAL_MODELS.md) | [简体中文](EXTERNAL_MODELS.zh-CN.md)

# R1 Pro models

The approved maintenance models are stored in Git LFS, including their XML/URDF,
metadata, profiles and meshes. The project owner confirmed communication with the
rights holder and instructed their publication on 2026-09-10. See
[provenance and scope](ASSET_PROVENANCE.md) and [license scope](LICENSE_SCOPE.md).
Galaxea assets are not relicensed under the repository's Apache-2.0 license.

## Download

After selecting the asset revision pinned by quick-start:

```bash
git lfs install
git lfs pull -I "" -X ""
git lfs fsck
python3 check_external_models.py
```

Quick-start steps 2.2–2.4 select the revision, fetch all payloads and verify the
required model files. GitHub's ordinary source ZIP may contain LFS pointers; use
Git + Git LFS for this workflow. Do not use the older model-free asset tag.

The four restored directories are `robot/r1_pro/`, `robot/r1_pro_chassis/`,
`robot/r1_pro_no_wheels/` and `robot/r1_pro_tote_gripper/`. Keep them together:
the tote/gripper model references meshes in the chassis directory. The files are
the existing Semantic-compatible baseline, not a replacement with newer models.

Official upstream reference: [Galaxea Dynamics URDF](https://github.com/userguide-galaxea/URDF).
An official URDF is not necessarily a drop-in replacement for these MuJoCo XMLs.
Missing payloads or unresolved pointers must be fixed before starting simulation.
