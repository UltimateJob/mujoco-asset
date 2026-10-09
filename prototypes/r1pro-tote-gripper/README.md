# R1 Pro tote gripper engineering prototype

[English](README.md) | [简体中文](README.zh-CN.md)

This directory is for joint mechanical and simulation review; it is not an
official scene directory. Before the models are confirmed, the assets here must
not be registered in `asset-catalog.v1.json`, nor may they replace the three
official depalletizing Layouts.

## Goals

- Generate both 600×400×340 mm and 530×410×240 mm hollow totes from the same
  parametric model.
- Each short side has one horizontal gripping recess formed by the tote wall
  panels themselves; there is no separate crossbar.
- Represent the rim, hollow wall panels, and main reinforcing ribs instead of
  substituting a solid block for the tote body.
- The gripper uses a compact wrist adapter plate, a 45° drop connector, a front
  C-frame, paired lower hooks, and a top active pressure plate.
- After the lower hooks fully enter the recess horizontally, they travel a
  short distance upward to seat against the inner edge of the recess, and the
  upper pressure plate then presses down on the tote rim.
- The gripper is a single fixed-size model; both tote sizes share the same
  recess interface. The gripper must not be scaled or rebuilt per tote size.
- Also generate engineering-review STEP, browser GLB, visual STL, convex
  collision STL, and a standalone MuJoCo prototype.

See [MODEL-REVIEW.md](MODEL-REVIEW.md) for photo comparison conclusions,
current assumptions, and dimensions still to be measured.

## Generation

```bash
uv run --python 3.10 \
  --with cadquery==2.5.2 --with trimesh==4.6.13 \
  --with scipy==1.15.3 --with pyyaml==6.0.2 \
  python authoring/generate_models.py
```

CadQuery is currently pinned to Python 3.10 to avoid host Python/NumPy ABI
effects on model generation. All generated artifacts are written to
`generated/`. STEP uses millimeters; the STL/GLB for MuJoCo/browser loading
have been converted to meters. This directory is Git-ignored; after review
confirms them, select the artifacts that should enter LFS, so that repeatedly
regenerated intermediate models do not pollute the repository.

## Quick shape review

After generating the models, use the official MuJoCo interactive window to
view both tote sizes and the complete left and right grippers at once:

```bash
uv run --with mujoco==3.4.0 python authoring/preview_mujoco.py
```

- Left-button drag: rotate;
- Shift + right-button drag: pan;
- Scroll wheel: zoom.

This window is only for reviewing shape, proportions, and mounting
orientation; it does not mean gripper mechanism control is integrated. Closing
the window ends the session — it does not start the Framework or the official
Runtime.

## Current verification boundaries

Both tote sizes have passed standalone real-contact test-rig verification. The
rig uses only MuJoCo contacts, gripper joints, and actuators to complete
approach, clamping, lifting, stable holding, and release; it does not create
weld/equality constraints and does not directly modify tote poses during
simulation stepping. Reproducible runs:

```bash
uv run --with mujoco==3.4.0 --with imageio==2.37.0 --with pyyaml==6.0.2 \
  python authoring/verify_mujoco.py --variant tote-600x400x340
uv run --with mujoco==3.4.0 --with imageio==2.37.0 --with pyyaml==6.0.2 \
  python authoring/verify_mujoco.py --variant tote-530x410x240
```

This rig proves that the contact topology of the tote interface and the fixed
gripper can complete a physical grasp; it does not replace the whole-robot
R1 Pro acceptance of IK, path planning, dual-arm synchronization, and
navigation — those capabilities are verified through the Runtime, Robot SDK,
and Ability chain.

## Coordinates and units

- Length: meters (engineering dimensions in YAML explicitly use mm).
- Mass: kg; force: N; time: s.
- World coordinates: right-handed, Z-up.
- Public quaternions: xyzw; MuJoCo XML boundary: wxyz.
- Gripper local coordinates: +X points toward the tote, +Z points up, and the
  active clamping piece moves along -Z.

## Fixed-gripper compatibility rules

- The left and right arms mount the same-size gripper; only the mirrored
  mounting transforms may differ.
- The nominal span from the upper surface of the fixed lower-hook foot to the
  closed contact face of the active upper pressure plate is 86 mm; after the
  lower-hook foot enters the tote side recess it seats against the recess's
  inner upper surface — the tote has no separate "load-bearing bar".
- The active upper pressure plate closes along -Z from the open position:
  35 mm is used for the opening stroke, and the closed end additionally
  reserves 4 mm of mechanical pre-load travel, so the full joint range exposed
  by the Runtime is 0–39 mm; this is not gripper width adjustment, and software
  thresholds cannot replace real contact force.
- Both tote sizes are compatible with this gripper through the same rim and
  side recesses; totes added later must not change the gripper model
  dimensions either.

## Review limitations

Parameters marked `assumed` in `engineering-parameters.yaml` must be measured
before real-machine manufacturing. `crystal天猫.stp` is only used to estimate
the existing end-effector mounting envelope; its geometry is not copied.
