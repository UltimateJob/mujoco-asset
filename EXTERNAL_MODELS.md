# External robot models / 外部机器人模型

Galaxea R1 Pro models are **not distributed** in this public snapshot, Git LFS,
or a model download mirror. Obtain the models from the
[official Galaxea URDF repository](https://github.com/userguide-galaxea/URDF/tree/galaxea/main/R1Pro)
and review its applicable terms. InsightOS is discussing redistribution permission
separately; attribution alone is not treated as permission.

The reviewed upstream reference is revision
`343902060f14622b6048d63b698423443eb4c26d`, not a verified drop-in replacement for
this release. The upstream 2025/2026 URDFs differ from the Semantic-adapted MuJoCo
models. Do not silently replace the validated robot with a newer model.

## Local integration

For R1 Pro examples, prepare a licensed, compatible local MuJoCo adaptation with
the following layout under this asset repository:

```text
robot/r1_pro_chassis/config/r1_pro_chassis.xml
robot/r1_pro_chassis/meta.json
robot/r1_pro_chassis/meshes/...
robot/r1_pro_tote_gripper/config/r1_pro_tote_gripper.xml
robot/r1_pro_tote_gripper/config/semantic_robot_profile.yaml
robot/r1_pro_tote_gripper/meshes/...
```

The adaptation must preserve the scene's joint/body/site names, mesh references,
actuation and kinematic conventions. A downloaded URDF cannot simply be renamed
to one of these XML files. The prototype tools can generate the project's custom
tote/gripper geometry, but do not supply or license the missing base robot.
Other R1 Pro variants use `robot/r1_pro/` and `robot/r1_pro_no_wheels/`.

These directories are ignored by Git. Keep local models out of commits, LFS,
public archives and mirrors. `python3 check_external_models.py` checks the minimum
local integration files; it is not a license or simulation compatibility validator.
R1 Pro scenes and their source templates remain as integration examples and need
these separately obtained assets. Server/Web/source builds remain available.

## 中文

公开版本不包含星海图 R1 Pro 模型，也不提供网盘或 OSS 镜像。请从上方官方链接
自行获取并遵守其使用条款。官方 URDF 与当前 Semantic 的 MuJoCo 适配模型并不相同，
需要完成关节、坐标系、Mesh 路径、执行器和语义接口的适配，不能直接改后缀使用。

本仓库保留场景和自制对象；R1 Pro 仿真示例需要补齐上述本地模型才能运行。
安装器会检查缺失项并给出指引，不会将未就绪的仿真报告为初始化成功。
模型目录已加入 Git 忽略规则，不应打包进公开制品。
