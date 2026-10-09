[English](MODEL_BUNDLE.md) | [简体中文](MODEL_BUNDLE.zh-CN.md)

# Franka Panda 模型包

这个目录是 Robot SDK 使用的正式运动学模型包。它是独立资产，不来自 `.venv`，
也不要求 SDK 在 robosuite、Isaac Sim 或 ROS 安装目录中搜索模型。

## 固定来源

- 上游仓库：`https://github.com/frankarobotics/franka_ros`
- Tag：`0.7.0`
- Commit：`17a4ad25ee0581a028e06c41884080896bc28298`
- 上游包：`franka_description`
- 许可证：Apache-2.0
- 运动学根坐标系：`panda_link0`
- SDK 末端坐标系：`panda_hand`

`LICENSE` 是上游根许可证的原样副本，`UPSTREAM_NOTICE` 是上游根 NOTICE 的
原样副本。本目录的 `NOTICE` 在保留上游声明的同时，说明了派生文件和本项目新增
的元数据。

## 目录内容

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

碰撞模型由上游 Xacro 中的 Cylinder 和 Sphere 生成，因此本包没有另行复制
collision mesh。Visual Mesh 保持原有 `package://franka_description/...` 引用和
目录层级。

上游入口把 `safety_distance` 设为 `0.03` 米。Pinocchio 建立全部自碰撞对后，
标准 ready 姿态只出现 `panda_link1` 与 `panda_link3` 的扩大安全体固定重叠；该对
在 manifest 中被明确排除。其他 Robot 自碰撞和所有环境碰撞仍继续检查。

导入时共包含 17 个上游或派生文件，元数据写入前的文件总大小为 10,555,790
字节。每个文件的字节数和用途记录在 `robot-model.json.file_inventory`；最终目录
大小可使用 `du -sb model_bundle` 重新核对。

## URDF 生成

派生 URDF 使用 xacro 2.1.1 从固定上游 revision 生成。生成环境必须提供
`franka_description` 的 ament package index；仓库不记录构建主机的临时目录。

可复现生成命令：

```bash
cd <franka-ros-root>
AMENT_PREFIX_PATH=<ament-prefix> \
ROS_PACKAGE_PATH=<franka-ros-root> \
uvx --from xacro==2.1.1 xacro \
  franka_description/robots/panda_arm_hand.urdf.xacro \
  -o panda_arm_hand.urdf
```

使用的 xacro 版本为 `2.1.1`。`panda_arm_hand.urdf` 的文件头也明确标记它是
Xacro 自动生成文件；生成后的 Robot 模型内容没有再手工修改。

## SDK 验证

在 `semantic-robot-sdk` 仓执行：

```bash
FRANKA_MODEL_ROOT=/absolute/path/to/robot/franka_panda/model_bundle \
  make test-franka
```

该门控会检查 manifest、官方来源、许可证、NOTICE、URDF、Mesh package root、
`panda_link0` 和 `panda_hand`，然后真实运行 Pinocchio FK、非零 IK 与 Ruckig 轨迹。
