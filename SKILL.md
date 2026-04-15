---
name: lx-music
description: |
  LX Music 桌面版播放器控制工具。通过本地 HTTP API 控制音乐播放、获取播放状态和歌词。
  触发场景：
  - "控制 LX Music 播放"、"暂停"
  - "LX Music 播放状态"、"现在播放什么歌"
  - "获取当前歌词"、"查看当前歌词"
  - "LX Music 上一曲/下一曲"
  - "调整 LX Music 音量"、"音量调大/调小"
  - "LX Music 收藏当前歌曲"、"收藏这首歌"
  - "播放一首歌"、"放一首周杰伦的歌"、"搜索并播放"
  - "跳到30秒"、"快进到1分钟"
  - "播放歌单"、"打开歌单"、"播放我的收藏歌单"
allowed-tools: Bash(curl *), PowerShell(Start-Process *)
---

# LX Music 控制

基于 LX Music 开放 API 的 HTTP 控制接口。**所有信息已内嵌，无需查阅在线文档。**

## 前置条件

LX Music 桌面版需开启「开放 API 服务」（设置 → 开放 API → 启用）。默认地址：`http://127.0.0.1:23330`

可通过环境变量 `LX_API_URL` 覆盖地址。

## 快速命令索引

| 操作 | 命令 |
|------|------|
| 播放 / 暂停 | `curl $LX_API_URL/play` / `curl $LX_API_URL/pause` |
| 上一曲 / 下一曲 | `curl $LX_API_URL/skip-prev` / `curl $LX_API_URL/skip-next` |
| 获取状态 | `curl $LX_API_URL/status` |
| 获取歌词 | `curl $LX_API_URL/lyric` |
| 音量控制 | `curl $LX_API_URL/volume?volume=80` |
| 静音 | `curl $LX_API_URL/mute?mute=true` |
| 收藏 | `curl $LX_API_URL/collect` |
| 搜索播放 | `powershell Start-Process "lxmusic://music/searchPlay/歌曲名-歌手"` |
| 跳转进度 | `curl $LX_API_URL/seek?offset=30` |

## API 详情

### 状态查询

```bash
# 获取完整状态
curl "$LX_API_URL/status"

# 过滤字段
curl "$LX_API_URL/status?filter=status,name,singer,progress"
```

响应字段：
- `status` — `playing` | `paused` | `stoped` | `error`
- `name` — 歌曲名
- `singer` — 艺术家
- `albumName` — 专辑名
- `duration` — 总时长（秒）
- `progress` — 当前进度（秒）
- `volume` — 音量 0-100
- `mute` — `true` | `false`
- `collect` — `true` | `false`

### 歌词获取

```bash
# LRC 歌词（纯文本）
curl "$LX_API_URL/lyric"

# 所有歌词类型（JSON）
curl "$LX_API_URL/lyric-all"
# 返回: {"lyric": "...", "tlyric": "...", "rlyric": "...", "lxlyric": "..."}
```

### 播放控制

```bash
curl "$LX_API_URL/play"              # 播放
curl "$LX_API_URL/pause"             # 暂停
curl "$LX_API_URL/skip-next"         # 下一曲
curl "$LX_API_URL/skip-prev"         # 上一曲
curl "$LX_API_URL/seek?offset=30"    # 跳到第 30 秒
curl "$LX_API_URL/volume?volume=80"  # 音量 1-100
curl "$LX_API_URL/mute?mute=true"   # 静音
curl "$LX_API_URL/mute?mute=false"  # 取消静音
curl "$LX_API_URL/collect"           # 收藏
curl "$LX_API_URL/uncollect"         # 取消收藏
```

### 搜索播放（Scheme URL）

**Windows 上需用 PowerShell：**

```powershell
# 搜索并播放（格式：歌曲名-歌手，留空则只搜索）
powershell -Command "Start-Process 'lxmusic://music/searchPlay/晴天-周杰伦'"

# 仅搜索（打开搜索面板）
powershell -Command "Start-Process 'lxmusic://music/search/kw/周杰伦'"
```

### 歌单操作（Scheme URL）

歌单需要歌单 ID，不同源的 ID 获取方式不同（通常在歌曲详情页 URL 中可见）。

```powershell
# 打开歌单（仅打开，不播放）
powershell -Command "Start-Process 'lxmusic://songlist/open/kw/歌单ID'"

# 播放歌单
powershell -Command "Start-Process 'lxmusic://songlist/play/kw/歌单ID'"

# 播放歌单并指定播放第几首（从 0 开始）
powershell -Command "Start-Process 'lxmusic://songlist/play/kw/歌单ID?index=0'"
```

URL 方式传参格式：
```
lxmusic://songlist/open/{source}/{id}
lxmusic://songlist/play/{source}/{id}
lxmusic://songlist/play/{source}/{id}?index=N
```

**source 取值**：`kw`（酷狗）| `kg`（酷我）| `tx`（QQ）| `wy`（网易）| `mg`（咪咕）

> 注意：歌单 ID 需要从 LX Music 界面中获取（例如在歌单页面 URL 或分享链接中）。不同源的 ID 不可混用。

Scheme URL 不需要 API 服务开启也可使用。

## 常见问题

- **API 返回空**：确认 LX Music 已开启「开放 API 服务」（需要 v2.7.0+）
- **Scheme URL 无法打开**：Windows 上必须用 `powershell -Command "Start-Process '...'"`，不要直接用 `start ""`（PowerShell 不支持）
- **端口被占用**：LX Music 设置中可修改 API 端口
