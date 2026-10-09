# R1 Pro tote depalletizing scene

[English](README.md) | [简体中文](README.zh-CN.md)

This scene coexists with the original palletizing_depalletizing_001, using the
independent r1_pro_tote_gripper Robot asset and two parametric hollow tote
sizes.

- layout001: 2×2×3 600×400×340 mm totes on pallet A; keeps acceptance-semantic
  references such as tote-large-l3-r1-c1/c2.
- layout002: 2×2×3 530×410×240 mm totes on pallet A.
- layout003: the two sizes placed on two separate pallets, for compatibility
  and placement regression.
- layout_smoke: a quick physical-stability regression with a single large
  tote; it does not replace full-stack acceptance.
- Tote collision is composed of the bottom, walls, rim, reinforcing ribs, and
  short-side gripping recesses — no solid blocks are used.
- Gripper grasping must rely on real contact between the fixed lower hooks and
  the active upper pressure plate; hidden attachment is not allowed.

Physical acceptance for v0.5.0 only permits approach, contact, stable holding,
lifting, and release through Runtime low-level trajectories and gripper
commands; weld, teleport, or directly rewriting tote poses is forbidden. IK,
navigation, and grasp candidates are still implemented by the R1 Pro Robot
SDK/Ability and do not enter the Runtime.

Previously, the full stack showed QACC divergence due to initial penetration
between adjacent tote rims and the Robot support plate; the current release
parameters have eliminated the initial penetration, and the Runtime runs
finite-value regression on layout001/002/003. If this regresses in the future,
it must be reported as a physics-parameter blocker; automatically degrading to
layout_smoke or silently reducing the tote count is not allowed.
