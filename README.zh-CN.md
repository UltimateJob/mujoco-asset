# MuJoCo Assets

[English](README.md) | [简体中文](README.zh-CN.md)

> 已确认发布的旧业务 R1 Pro 模型通过 Git LFS 下载。参见[模型下载与来源说明](EXTERNAL_MODELS.md)。第三方模型权利不由本仓库 Apache-2.0 许可证覆盖。

🌐 Semantic MuJoCo Runtime 使用的场景、机器人与物体资产。本仓库不是可执行程序，也不是 Python 环境。

## 工程结构

- `assets/`：可复用物体资产。
- `robot/`：机器人模型与网格。
- `scene/`：场景包与布局。
- `asset-catalog.v1.json`：资产目录。
- `prototypes/`：实验性资产。

## 准备与校验

先安装 Git LFS，再从本仓库拉取资产：

```bash
git lfs install
git lfs pull
git lfs fsck
python3 check_external_models.py
python3 -m json.tool asset-catalog.v1.json > /dev/null
```

无需编译可执行程序。这些命令校验 LFS 对象与 JSON 语法，不验证全部模型语义；选定场景还需由 MuJoCo Runtime 加载验证。

## 使用方式

启动独立的 mujoco-runtime 项目时，将 `MUJOCO_ASSET_ROOT` 设置为本仓库绝对路径。quick-start 会将资产根目录登记到原生 MuJoCo。场景 / 包清单、引用的网格与布局应保持完整。

如果网格文件实际只有少量文本，通常是 LFS 指针。先完成下载，再排查渲染或模型加载问题。

## ⚠️ 分发边界

每项可分发资产都应具备来源、许可证、稳定 ID 与分发结论。来源不明、许可待确认或标记为仅内部使用的资产，**不能作为公开制品发布**。

自有代码的 Apache 许可证不改变第三方模型或网格的许可。请保留原始声明与许可证，包括 Franka 模型包内的相关文件。

[详细资产参考](README.reference.md) · [许可范围](LICENSE_SCOPE.md)

## 许可证

Copyright 2026 InsightOS。自有代码采用 [Apache-2.0](LICENSE)；第三方组件与资产请查看 [NOTICE](NOTICE) 和[许可范围](LICENSE_SCOPE.md)。

## 三个平台的构建复现

参见 [glibc、musl 与 macOS 构建说明](README.build.md)：包含已锁定的源码版本、实际脚本入口、工具要求、本地与 CI 指令、产物位置和平台验证范围。
