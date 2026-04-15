# LX Music OpenCode Skill

LX Music 桌面版播放器控制技能，用于 OpenCode / Claude AI 助手。

通过本地 HTTP API + SQLite 歌单数据库实现播放控制、搜索播放、歌单查询。**所有 API 已内嵌，无需查阅在线文档。**

## 安装

```bash
git clone https://github.com/ET06731/lx-music-skill.git
cp -r lx-music-skill ~/.openclaw/workspace/skills/lx-music
```

## 前置条件

- LX Music 桌面版 v2.7.0+
- 开启「开放 API 服务」（设置 → 开放 API → 启用）
- Python 3（用于歌单查询脚本）

## 快速使用

### 播放控制

| 操作 | 命令 |
|------|------|
| 播放 / 暂停 | `curl $LX_API_URL/play` / `curl $LX_API_URL/pause` |
| 上一曲 / 下一曲 | `curl $LX_API_URL/skip-prev` / `curl $LX_API_URL/skip-next` |
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

```powershell
# 搜索并播放（格式：歌曲名-歌手）
powershell -Command "Start-Process 'lxmusic://music/searchPlay/晴天-周杰伦'"
```

### 歌单查询与播放

```bash
# 列出所有歌单
python scripts/playlist.py

# 查看歌单中的歌曲
python scripts/playlist.py songs <list_id>

# 播放歌单
python scripts/playlist.py play <list_id>
```

歌单 ID 可通过列表命令获取。

## 完整 API

| 端点 | 说明 |
|------|------|
| `GET /status` | 获取播放器状态 |
| `GET /lyric` | 获取 LRC 歌词 |
| `GET /lyric-all` | 获取所有歌词 |
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
- **工具**: `curl`（Bash）, `Start-Process`（PowerShell）, `python`
- **跨平台**: Windows/macOS/Linux 自动检测数据目录
