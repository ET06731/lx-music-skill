# LX Music OpenCode Skill

LX Music 桌面版播放器控制技能，用于 OpenCode / Claude AI 助手。

通过本地 HTTP API 控制音乐播放、获取播放状态和歌词。**所有 API 已内嵌，无需查阅在线文档。**

## 安装

```bash
# 克隆到本地
git clone https://github.com/ET06731/lx-music-skill.git

# 复制到技能目录
cp -r lx-music-skill ~/.openclaw/workspace/skills/lx-music
```

## 前置条件

LX Music 桌面版需开启「开放 API 服务」（设置 → 开放 API → 启用）。需要 v2.7.0+

默认地址：`http://127.0.0.1:23330`

## 快速使用

### 播放控制

| 操作 | 命令 |
|------|------|
| 播放 | `curl $LX_API_URL/play` |
| 暂停 | `curl $LX_API_URL/pause` |
| 上一曲 | `curl $LX_API_URL/skip-prev` |
| 下一曲 | `curl $LX_API_URL/skip-next` |
| 跳转进度 | `curl $LX_API_URL/seek?offset=30` |
| 音量调节 | `curl $LX_API_URL/volume?volume=80` |
| 静音 | `curl $LX_API_URL/mute?mute=true` |
| 收藏 | `curl $LX_API_URL/collect` |

### 查询

| 操作 | 命令 |
|------|------|
| 播放状态 | `curl $LX_API_URL/status` |
| 当前歌词 | `curl $LX_API_URL/lyric` |
| 所有歌词 | `curl $LX_API_URL/lyric-all` |

### 搜索播放

Windows 上必须用 PowerShell：

```powershell
# 搜索并播放（格式：歌曲名-歌手）
powershell -Command "Start-Process 'lxmusic://music/searchPlay/晴天-周杰伦'"
```

Scheme URL 不需要开启开放 API 服务。

## 完整 API

| 端点 | 说明 |
|------|------|
| `GET /status` | 获取播放器状态 |
| `GET /lyric` | 获取 LRC 歌词 |
| `GET /lyric-all` | 获取所有歌词（翻译/罗马音等）|
| `GET /subscribe-player-status` | SSE 实时状态订阅 |
| `GET /play` | 播放 |
| `GET /pause` | 暂停 |
| `GET /skip-next` | 下一曲 |
| `GET /skip-prev` | 上一曲 |
| `GET /seek?offset=N` | 跳转进度（秒）|
| `GET /volume?volume=N` | 音量 1-100 |
| `GET /mute?mute=true/false` | 静音控制 |
| `GET /collect` | 收藏 |
| `GET /uncollect` | 取消收藏 |

## 技术细节

- **协议**: HTTP GET
- **默认端口**: `23330`
- **无需认证**
- **工具**: `curl`（Bash）, `Start-Process`（PowerShell，用于 Scheme URL）
