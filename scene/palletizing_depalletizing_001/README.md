# Depalletizing scene assets

[English](README.md) | [简体中文](README.zh-CN.md)

This directory contains three fixed layouts. The Runtime loads the R1 Pro and
cameras via `scene_info.yaml`, then creates the pallets, totes, and target
zones according to `layout001.yaml` through `layout003.yaml`.

- Length: meters
- Angles: radians
- Time: seconds
- Asset and MuJoCo XML quaternions: `[w, x, y, z]`
- Runtime and Robot SDK public interface quaternions: `[x, y, z, w]`
- Coordinate frame: `world`

`asset-manifest.yaml` gives the fixed seed and expected object manifest for
each layout. After reading the Profile, the Robot, joints, and Runtime are
responsible for converting between the two orderings; public interfaces must
not directly return the asset ordering.

The public mapping of actuators, sites, and cameras lives in
`robot/r1_pro_chassis/config/semantic_robot_profile.yaml`.

## Public scenes and Project Layouts

`authoring/` is the Layout editing input for the public read-only scene, not
another set of Runtime assets:

- `scene-template.json` fixes the non-deletable nodes such as the R1 Pro,
  preview cameras, and lights;
- `layouts/layout001.json` through `layout003.json` are the official read-only
  Layouts;
- `asset-set.json` declares the compatible material set that Project Layouts
  may use;
- `preview-camera.json` fixes the camera parameters for the deterministic SVG
  and the Runtime's photographed preview.

Regular users cannot overwrite these files, nor create scenes from a
completely blank world. The Framework only copies an official Layout or the
blank Layout inside the template as a Project draft; saving a draft generates
the SVG for the corresponding revision, and after a successful build the
Runtime can additionally generate PNG/WebP with the fixed camera. The
robosuite and LIBERO directories do not use this authoring input and remain
read-only in the first version.

This directory was organized from `origin/feature/openclaw`. Before release,
the MR must confirm the provenance and permitted distribution scope of the
in-house models as well as external assets such as meshes and materials; until
confirmed, they are for internal development and testing only.
