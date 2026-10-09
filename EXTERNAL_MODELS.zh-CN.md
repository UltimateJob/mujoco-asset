[English](EXTERNAL_MODELS.md) | [简体中文](EXTERNAL_MODELS.zh-CN.md)

# R1 Pro 模型

旧业务 R1 Pro 模型现已通过 Git LFS 提供，包括 XML、URDF、配置与 Mesh。
项目所有者已确认与对方沟通并要求发布（2026-09-10）；来源与范围见
[ASSET_PROVENANCE.md](ASSET_PROVENANCE.md)，许可范围见 [LICENSE_SCOPE.md](LICENSE_SCOPE.md)，
不以 Apache-2.0 覆盖第三方权利。模型文件保持原有版本，不替换为最新官方模型。

## 下载

按 quick-start 锁定的资产修订版本选择后：

```bash
git lfs install
git lfs pull -I "" -X ""
git lfs fsck
python3 check_external_models.py
```

使用 quick-start 更新后的版本清单，依次执行 2.2、2.3、2.4。GitHub 普通源码 ZIP 可能只含
LFS 指针，本流程请使用 Git + Git LFS。不要继续检出先前不含模型的旧资产 tag。

恢复的四个目录为 `robot/r1_pro/`、`robot/r1_pro_chassis/`、`robot/r1_pro_no_wheels/` 和
`robot/r1_pro_tote_gripper/`。请保持它们在一起：tote/gripper 依赖 chassis 的网格，
请保持目录结构完整。这些文件是现有 Semantic 兼容基线，并非更新模型的替代品。

官方上游参考：[Galaxea Dynamics URDF](https://github.com/userguide-galaxea/URDF)。
官方 URDF 不一定是这些 MuJoCo XML 的直接替代品。启动仿真前必须修复缺失的载荷或未解析的指针。
