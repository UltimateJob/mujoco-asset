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

## Galaxea R1 Pro — approved baseline publication

On 2026-09-10, the project owner confirmed communication with the rights holder
and instructed publication of the required model files via Git LFS. This update
restores only the existing maintenance baseline from source asset revision
`9cb8d74958c7bb4f692eed6d34a4763db641228a`, not a newer upstream model:

- `robot/r1_pro/`
- `robot/r1_pro_chassis/`
- `robot/r1_pro_no_wheels/`
- `robot/r1_pro_tote_gripper/` (including its chassis mesh dependencies)

This records the owner's publication instruction, not the text of an agreement
or a new license grant to downstream users. Company-level permission records are
maintained separately. Preserve Galaxea attribution and applicable original terms;
this repository does not label these third-party assets Apache-2.0.

项目所有者于 2026-09-10 确认已与对方沟通，并要求通过 Git LFS 发布上述旧业务模型。
这里只记录发布范围，不编造授权协议内容，也不以 Apache-2.0 重新授权第三方模型。
公司层面的沟通与授权记录另行保管；使用者应保留来源声明并遵守适用的原始条款。

### Upstream reference

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

The initial public tag excluded these models while communication was pending.
The maintenance update restores them following the owner's instruction above.
See [download instructions](EXTERNAL_MODELS.md). No Galaxea endorsement is implied;
the repository's Apache-2.0 license does not override Galaxea's asset rights.
