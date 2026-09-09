# Asset provenance and publication scope

## Original assets / 自制资产

The project owner confirmed on 2026-09-10 that the `box`, `pallet`, and `target`
catalog assets are original work. These assets are released under this repository's
[Apache-2.0 license](LICENSE), Copyright 2026 InsightOS. This declaration covers
`assets/objects/box.xml`, `assets/objects/target.xml`, and the corresponding box,
pallet, and target catalog geometry/material definitions. It does not relicense
any robot meshes or other third-party assets.

项目所有者已确认 box、pallet、target 为自制资产，以上明确列出的文件和目录定义
按 Apache-2.0 发布；该声明不适用于机器人 Mesh 或其他第三方资产。

## Galaxea R1 Pro — redistribution review pending

Upstream candidate: [Galaxea Dynamics URDF](https://github.com/userguide-galaxea/URDF),
revision `343902060f14622b6048d63b698423443eb4c26d`.
Its [R1 Pro 2026 package metadata](https://github.com/userguide-galaxea/URDF/blob/343902060f14622b6048d63b698423443eb4c26d/R1Pro/urdf_r1pro_g1z_2026/package.xml)
declares `BSD`, without identifying the BSD variant or supplying a complete license
text in that package. Author/maintainer metadata still contains placeholders.

At this revision, 16 of the 112 local STL/OBJ/URDF files in `robot/r1_pro_chassis`
have identical Git blob hashes to files in the upstream repository. The remaining
files require provenance/conversion verification; a mismatch alone does not mean
they are unrelated or unauthorized. This partial match does not establish the
redistribution terms for the complete local model.

The R1 Pro model directories and catalog entry have been excluded from this
public snapshot. See [local integration instructions](EXTERNAL_MODELS.md). An acknowledgement is not a substitute for the
license terms. No Galaxea endorsement is implied; the repository's Apache-2.0
license does not override Galaxea's asset rights.

已定位官方来源并确认部分文件相同，但 BSD 具体版本、完整许可和本地改造关系仍需
核实。公开快照已排除 R1 Pro 模型目录和对应目录条目，不以自有 Apache-2.0 声明覆盖第三方权利。
