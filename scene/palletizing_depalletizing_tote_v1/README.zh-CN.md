# R1 Pro 周转箱拆码垛场景

[English](README.md) | [简体中文](README.zh-CN.md)

该场景与原有 palletizing_depalletizing_001 并存，使用独立的
r1_pro_tote_gripper Robot 资产和两种参数化中空周转箱。

- layout001：托盘 A 上 2×2×3 个 600×400×340 mm 周转箱；保留
  tote-large-l3-r1-c1/c2 等验收语义引用。
- layout002：托盘 A 上 2×2×3 个 530×410×240 mm 周转箱。
- layout003：两种规格分别位于两个托盘，用于兼容性与放置回归。
- layout_smoke：单个大箱的物理稳定性快速回归，不替代完整垛验收。
- 箱体碰撞由底、壁、箱沿、加强筋和短边抓取凹槽组成，不使用实心方块。
- 夹具抓取必须依靠固定下钩与主动上压片的真实接触，不允许隐藏附着。

v0.5.0 的物理验收只允许通过 Runtime 低层轨迹与夹具命令完成接近、接触、
稳定持有、抬升和释放；禁止 weld、teleport 或直接改写箱体 pose。IK、导航和
抓取候选仍由 R1 Pro Robot SDK/Ability 实现，不进入 Runtime。

此前完整堆垛因相邻箱沿和 Robot 支撑板的初始穿透出现 QACC 发散；当前发布参数
已消除初始穿透，并由 Runtime 对 layout001/002/003 执行有限值回归。后续若回归，
必须报告为物理参数阻塞，不允许自动退化到 layout_smoke 或静默减少箱体数量。
