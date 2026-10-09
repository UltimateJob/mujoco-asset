[English](MODEL_BUNDLE.md) | [简体中文](MODEL_BUNDLE.zh-CN.md)

# Franka Panda model bundle

This directory is the official kinematic model bundle used by the Robot SDK. It is a standalone asset; it does not come from a `.venv`,
and it does not require the SDK to search for models in robosuite, Isaac Sim, or ROS installation directories.

## Pinned source

- Upstream repository: `https://github.com/frankarobotics/franka_ros`
- Tag: `0.7.0`
- Commit: `17a4ad25ee0581a028e06c41884080896bc28298`
- Upstream package: `franka_description`
- License: Apache-2.0
- Kinematic root frame: `panda_link0`
- SDK end-effector frame: `panda_hand`

`LICENSE` is a verbatim copy of the upstream root license, and `UPSTREAM_NOTICE` is a verbatim copy of the
upstream root NOTICE. The `NOTICE` in this directory preserves the upstream notices while documenting the derived files and the metadata added
by this project.

## Directory contents

```text
model_bundle/
├── robot-model.json
├── LICENSE
├── NOTICE
├── UPSTREAM_NOTICE
└── franka_description/
    ├── package.xml
    ├── meshes/visual/*.dae
    └── robots/
        ├── panda_arm_hand.urdf
        ├── panda_arm_hand.urdf.xacro
        ├── panda_arm.xacro
        └── hand.xacro
```

The collision model is generated from the Cylinders and Spheres in the upstream Xacro, so this bundle does not separately copy
collision meshes. Visual meshes keep their original `package://franka_description/...` references and
directory hierarchy.

The upstream entry sets `safety_distance` to `0.03` meters. After Pinocchio builds all self-collision pairs,
the standard ready posture shows only the enlarged safety-volume fixed overlap of `panda_link1` and `panda_link3`; that pair
is explicitly excluded in the manifest. All other Robot self-collisions and all environment collisions are still checked.

The import includes 17 upstream or derived files in total, and the files totaled 10,555,790
bytes before metadata was written. Each file's byte count and purpose is recorded in `robot-model.json.file_inventory`; the final directory
size can be re-verified with `du -sb model_bundle`.

## URDF generation

The derived URDF was generated with xacro 2.1.1 from the pinned upstream revision. The generation environment must provide
the ament package index for `franka_description`; the repository does not record the build host's temporary directories.

Reproducible generation command:

```bash
cd <franka-ros-root>
AMENT_PREFIX_PATH=<ament-prefix> \
ROS_PACKAGE_PATH=<franka-ros-root> \
uvx --from xacro==2.1.1 xacro \
  franka_description/robots/panda_arm_hand.urdf.xacro \
  -o panda_arm_hand.urdf
```

The xacro version used is `2.1.1`. The header of `panda_arm_hand.urdf` also explicitly marks it as a
Xacro auto-generated file; the generated Robot model content has not been manually modified afterwards.

## SDK verification

In the `semantic-robot-sdk` repo, run:

```bash
FRANKA_MODEL_ROOT=/absolute/path/to/robot/franka_panda/model_bundle \
  make test-franka
```

This gate checks the manifest, official source, license, NOTICE, URDF, mesh package root,
`panda_link0`, and `panda_hand`, then actually runs Pinocchio FK, non-zero IK, and Ruckig trajectories.
