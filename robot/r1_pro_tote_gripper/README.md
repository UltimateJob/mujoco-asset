# R1 Pro tote gripper variant

[English](README.md) | [简体中文](README.zh-CN.md)

This directory is an independent Robot asset and does not replace
r1_pro_chassis. Each wrist mounts one fixed-size C-frame tote gripper; the
same gripper fits both tote sizes through a 0–35 mm active pressure-plate
stroke.

- The fixed lower hooks enter the 26 mm gripping recess on the tote's short
  side and latch onto the recess edge.
- The active upper pressure plate only performs low-level open/close and force
  limiting.
- q=0 means clamped; the positive direction opens upward.
- The Runtime only reports position, force, Hook/Clamp contacts, slip, and
  stable carrying.
- Dual-arm alignment, IK, grasp ordering, and failure recovery are implemented
  by the subsequent Robot SDK/Skill.

The mechanical parameters still need to be calibrated against wrist flange,
payload, and tote measurements before real-machine manufacturing.
