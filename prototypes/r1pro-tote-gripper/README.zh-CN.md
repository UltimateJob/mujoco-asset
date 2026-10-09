# R1 Pro 周转箱夹具工程原型

[English](README.md) | [简体中文](README.zh-CN.md)

本目录用于机械和仿真联合评审，不属于正式场景目录。模型确认前不得把这里的
资产登记到 `asset-catalog.v1.json`，也不得替换三套正式拆码垛 Layout。

## 目标

- 用同一参数模型生成 600×400×340 mm 与 530×410×240 mm 两种中空周转箱。
- 两个短边各有一个由箱体壁板自身形成的水平抓取凹槽，不存在独立横条。
- 表达箱沿、中空壁板和主要加强筋，而不是使用实心方块替代箱体。
- 夹具使用紧凑腕部适配板、45° 下沉连接件、前端 C 型框、成对下钩和顶部主动压板。
- 下钩完整水平进入凹槽后短距离向上贴合槽沿内侧，上压片再压住箱沿。
- 夹具是一个固定尺寸型号，两种箱体共享同一凹槽接口；不得按箱体尺寸缩放或重建夹具。
- 同时生成工程评审 STEP、浏览器 GLB、可视 STL、凸体碰撞 STL 和独立 MuJoCo 原型。

照片对比结论、当前推测项和待测尺寸见 [MODEL-REVIEW.md](MODEL-REVIEW.md)。

## 生成

```bash
uv run --python 3.10 \
  --with cadquery==2.5.2 --with trimesh==4.6.13 \
  --with scipy==1.15.3 --with pyyaml==6.0.2 \
  python authoring/generate_models.py
```

CadQuery 当前固定使用 Python 3.10，避免宿主 Python/NumPy ABI 影响模型生成。所有生成物
写入 `generated/`。STEP 使用毫米；供 MuJoCo/浏览器加载的 STL/GLB 已转换为米。
该目录由 Git 忽略；评审确认后再选择需要进入 LFS
的制品，避免反复生成的中间模型污染仓库。

## 快速外形评审

生成模型后，用 MuJoCo 官方交互窗口同时查看两种箱体和左右完整夹具：

```bash
uv run --with mujoco==3.4.0 python authoring/preview_mujoco.py
```

- 左键拖动：旋转；
- Shift + 右键拖动：平移；
- 滚轮：缩放。

该窗口只用于外形、比例和安装方向评审，不代表夹具机构控制已经接入。
关闭窗口即可结束，不会启动 Framework 或正式 Runtime。

## 当前验证边界

两种周转箱均已通过独立的真实接触台架验证。台架只使用 MuJoCo 接触、
夹具关节和执行器完成接近、压紧、抬升、稳定保持与释放；不会创建 weld/equality，
也不会在仿真步进期间直接修改箱体位姿。可重复运行：

```bash
uv run --with mujoco==3.4.0 --with imageio==2.37.0 --with pyyaml==6.0.2 \
  python authoring/verify_mujoco.py --variant tote-600x400x340
uv run --with mujoco==3.4.0 --with imageio==2.37.0 --with pyyaml==6.0.2 \
  python authoring/verify_mujoco.py --variant tote-530x410x240
```

该台架证明箱体接口与固定夹具的接触拓扑可完成物理夹持，不代替 R1 Pro 整机的
IK、路径规划、双臂同步和导航验收；这些能力由 Runtime、Robot SDK 与 Ability 链路验证。

## 坐标与单位

- 长度：米（YAML 中工程尺寸明确使用 mm）。
- 质量：kg；力：N；时间：s。
- 世界坐标：右手系、Z-up。
- 公共四元数：xyzw；MuJoCo XML 边界：wxyz。
- 夹具局部坐标：+X 指向箱体，+Z 向上，主动压紧件沿 -Z 运动。

## 固定夹具兼容规则

- 左右臂安装的是同一尺寸夹具，只允许镜像安装变换不同。
- 固定下钩脚上表面到主动上压片闭合接触面的名义跨度为 86 mm；下钩脚
  进入箱体侧面凹槽后贴住槽内上表面，箱体不存在独立“承力条”。
- 主动上压片从打开位置沿 -Z 闭合：35 mm 用于打开行程，闭合端另保留
  4 mm 机械预压行程，因此 Runtime 暴露的完整关节范围为 0–39 mm；这不是
  夹具宽度调节，也不能用软件阈值替代真实接触力。
- 两种箱体均通过相同的箱沿和侧面凹槽兼容该夹具；后续新增箱体也不得改变夹具模型尺寸。

## 评审限制

`engineering-parameters.yaml` 中标记为 `assumed` 的参数必须在真机制造前实测。
`crystal天猫.stp` 只用于估算现有末端安装包络，不复制其几何。
