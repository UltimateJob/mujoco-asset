# Public maintenance snapshot

This repository contains a single source snapshot derived from maintenance tag
`v0.4.0-insightos.2026.2`. Source revision: `9cb8d74958c7bb4f692eed6d34a4763db641228a`.
The source history and earlier tags/branches are not included. Public commit IDs
are therefore different. Use quick-start's public manifest for compatible pins.

This is the existing verified product line, not the latest upstream implementation.
Publication changes are limited to documentation, public configuration/dependency
sources, license notices and exclusion of non-distributable or generated assets.
Existing package/product version strings have not been bumped.

The initial public tag excluded Galaxea robot models. On 2026-09-10 the project
owner confirmed communication with the rights holder and instructed restoration
of the existing baseline via LFS. The subsequent maintenance update provides
these models; see [model downloads](EXTERNAL_MODELS.md) and [provenance](ASSET_PROVENANCE.md).
No prebuilt full-stack archive or newly verified end-to-end R1 Pro deployment is
published by this source snapshot.

中文：本仓库从上述旧业务维护 Tag 导出单次公开快照，不包含原提交历史及旧分支、旧
Tag。公开 SHA 与原仓库不同，请以 quick-start 的公开清单为准。首次公开 tag 排除了
星海图模型；后续维护更新根据项目所有者确认恢复旧业务模型的 LFS 下载，不升级业务模型。
