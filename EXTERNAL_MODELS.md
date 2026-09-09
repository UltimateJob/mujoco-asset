# R1 Pro models / R1 Pro 模型

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

## 中文

旧业务 R1 Pro 模型现已通过 Git LFS 提供，包括 XML、URDF、配置与 Mesh。
项目所有者已确认与对方沟通并要求发布；来源与声明见上方文档，不以 Apache-2.0
覆盖第三方权利。模型文件保持原有版本，不替换为最新官方模型。

使用 quick-start 更新后的版本清单，依次执行 2.2、2.3、2.4。手动操作请执行上面的
命令。不要继续检出先前不含模型的旧资产 tag，也不要将 GitHub 普通源码 ZIP 中的
LFS 指针当成模型。tote/gripper 依赖 chassis 的网格，请保持目录结构完整。
