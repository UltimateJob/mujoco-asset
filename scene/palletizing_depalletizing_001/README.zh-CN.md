# 拆码垛场景资产

[English](README.md) | [简体中文](README.zh-CN.md)

本目录包含三套固定布局。Runtime 通过 `scene_info.yaml` 加载 R1 Pro 和相机，再按
`layout001.yaml`～`layout003.yaml` 创建托盘、箱体和目标区域。

- 长度：米
- 角度：弧度
- 时间：秒
- 资产与 MuJoCo XML 四元数：`[w, x, y, z]`
- Runtime 和 Robot SDK 公共接口四元数：`[x, y, z, w]`
- 坐标系：`world`

`asset-manifest.yaml` 给出每套布局的固定 seed 与预期对象清单。Robot、joint、
Runtime 读取 Profile 后负责两种顺序的转换，公共接口不得直接返回资产顺序。

actuator、site 和 camera 的公共映射位于
`robot/r1_pro_chassis/config/semantic_robot_profile.yaml`。

## 公共场景与 Project Layout

`authoring/` 是公共只读场景的 Layout 编辑输入，不是另一套 Runtime 资产：

- `scene-template.json` 固定 R1 Pro、预览相机和灯光等不可删除节点；
- `layouts/layout001.json`～`layout003.json` 是官方只读 Layout；
- `asset-set.json` 声明 Project Layout 可以使用的兼容素材集合；
- `preview-camera.json` 固定确定性 SVG 和 Runtime 实拍预览的相机参数。

普通用户不能覆盖这些文件，也不能从完全空白世界创建场景。Framework 只会把某个
官方 Layout 或模板内空白 Layout 复制为 Project 草稿；草稿保存时生成 revision
对应的 SVG，构建成功后可以再由 Runtime 固定相机生成 PNG/WebP。robosuite 与
LIBERO 目录不使用本 authoring 输入，第一版保持只读。

本目录从 `origin/feature/openclaw` 整理。发布前必须在 MR 中确认自有模型以及
mesh、材质等外部资产的来源和允许分发范围；未确认前只用于内部开发与测试。
