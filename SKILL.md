---
name: lx-music
description: |
  LX Music 桌面版播放器控制工具。通过本地 HTTP API 控制音乐播放、获取播放状态和歌词。
  触发场景：
  - "控制 LX Music 播放"
  - "LX Music 播放状态"
  - "获取当前歌词"
  - "LX Music 上一曲/下一曲"
  - "调整 LX Music 音量"
  - "LX Music 收藏当前歌曲"
allowed-tools: Bash(curl *)
---

# LX Music 控制

基于 [LX Music 开放 API](https://lxmusic.toside.cn/desktop/open-api) 的 HTTP 控制接口。

## 前置条件

LX Music 桌面版需开启「开放 API 服务」（设置 → 开放 API → 启用）。默认地址：`http://127.0.0.1:23330`

可通过环境变量 `LX_API_URL` 覆盖地址。

## API 基础

- **Base URL**: `http://127.0.0.1:23330`（可设置 `LX_API_URL` 覆盖）
- 所有接口均为 HTTP GET 请求
- 响应格式：JSON（除 `/lyric` 返回纯文本）

## 播放器状态

```bash
# 获取完整状态
curl "$LX_API_URL/status"

# 过滤返回字段（status, name, singer, albumName, lyricLineText, duration, progress, playbackRate 默认）
curl "$LX_API_URL/status?filter=status,name,singer,progress"
```

关键字段：
| 字段 | 值 | 说明 |
|------|-----|------|
| `status` | `playing`, `paused`, `stoped`, `error` | 播放状态 |
| `name` | 字符串 | 歌曲名 |
| `singer` | 字符串 | 艺术家 |
| `albumName` | 字符串 | 专辑名 |
| `duration` | 数字 | 总时长（秒） |
| `progress` | 数字 | 当前进度（秒） |
| `volume` | 数字 0-100 | 音量 |
| `mute` | `true/false` | 静音状态 |
| `collect` | `true/false` | 是否已收藏 |

## 歌词获取

```bash
# 获取当前 LRC 歌词（纯文本）
curl "$LX_API_URL/lyric"

# 获取所有类型歌词（JSON）
curl "$LX_API_URL/lyric-all"
# 返回: {"lyric": "...", "tlyric": "...", "rlyric": "...", "lxlyric": "..."}
```

## 播放控制

```bash
curl "$LX_API_URL/play"      # 播放
curl "$LX_API_URL/pause"     # 暂停
curl "$LX_API_URL/skip-next" # 下一曲
curl "$LX_API_URL/skip-prev" # 上一曲
curl "$LX_API_URL/seek?offset=30"        # 跳转到第 30 秒
curl "$LX_API_URL/volume?volume=80"     # 设置音量 1-100
curl "$LX_API_URL/mute?mute=true"       # 静音
curl "$LX_API_URL/mute?mute=false"      # 取消静音
curl "$LX_API_URL/collect"              # 收藏当前歌曲
curl "$LX_API_URL/uncollect"             # 取消收藏
```

## 实时状态订阅（SSE）

播放状态变更时自动推送，避免轮询：

```bash
curl -N "$LX_API_URL/subscribe-player-status"
```

事件格式：
```
event: status
data: "playing"

event: name
data: "交换余生"
```

## 配合 Scheme URL 使用

可通过 [Scheme URL](https://lxmusic.toside.cn/desktop/scheme-url) 实现搜索播放：

```bash
# 搜索并播放（需参考 Scheme URL 文档构建 URL）
start "" "lxmusic://search?keyword=周杰伦"
```

## 常见问题

- **API 无响应**：确认 LX Music 已开启「开放 API 服务」（需要 v2.7.0+）
- **端口被占用**：LX Music 设置中可修改 API 端口
- **SSE 测试**：`curl -N http://127.0.0.1:23330/subscribe-player-status`
