# MuJoCo Assets

[English](README.md) | [简体中文](README.zh-CN.md)

> Galaxea robot models are excluded. R1 Pro scenes require [external model setup](EXTERNAL_MODELS.md); the public catalog contains only original box/pallet/target assets.

🌐 Scene, robot, and object assets for Semantic's MuJoCo Runtime. This is an asset repository, not an executable application or a Python environment.

## Structure

- `assets/` — reusable object assets.
- `robot/` — robot models and meshes.
- `scene/` — scene packages and layouts.
- `asset-catalog.v1.json` — asset catalog.
- `prototypes/` — experimental asset work.

## Prepare and validate

Install Git LFS before fetching the asset payloads. From this repository:

```bash
git lfs install
git lfs pull
git lfs fsck
python3 -m json.tool asset-catalog.v1.json > /dev/null
```

No executable compilation is required. These checks validate LFS objects and JSON syntax, not all model semantics; the MuJoCo Runtime must also load and validate the selected scenes.

## Use the assets

Set `MUJOCO_ASSET_ROOT` to this repository's absolute path when starting the separate mujoco-runtime project. Quick-start registers that asset root with native MuJoCo. Keep scene/package manifests, referenced meshes, and layouts together.

A tiny text file where a mesh is expected is usually an LFS pointer. Download the payload before troubleshooting rendering or model loading.

## ⚠️ Distribution boundary

Every distributable asset needs a source, license, stable ID, and distribution decision. Entries with unknown provenance, pending licenses, or internal-only distribution status **must not be published as public artifacts**.

The Apache license for first-party code does not relicense third-party models or meshes. Preserve the original notices and licenses, including those in the Franka model bundle.

[Detailed asset reference](README.reference.md) · [License scope](LICENSE_SCOPE.md)

## License

Copyright 2026 InsightOS. First-party code: [Apache-2.0](LICENSE). See [NOTICE](NOTICE) and [license scope](LICENSE_SCOPE.md) for third-party components and assets.
