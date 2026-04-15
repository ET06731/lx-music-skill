# LX Music OpenCode Skill

LX Music 桌面版播放器控制技能，用于 OpenCode / Claude AI 助手。

通过本地 HTTP API 控制音乐播放、获取播放状态和歌词。

## 安装

复制到你的技能目录：

```bash
# OpenCode
cp -r lx-music ~/.openclaw/workspace/skills/lx-music

# 或符号链接
ln -s /path/to/lx-music ~/.openclaw/workspace/skills/lx-music
```

## 前置条件

LX Music 桌面版需开启「开放 API 服务」：
1. 打开 LX Music 设置
2. 找到「开放 API」→「启用」
3. 默认地址：`http://127.0.0.1:23330`

需要 LX Music **v2.7.0+**

## 使用示例

### 播放控制

```
"播放"
"暂停"
"上一曲"
"下一曲"
"跳到30秒"
"音量调到80"
"静音"
```

### 获取状态

```
"现在播放什么歌"
"当前播放状态"
"获取当前歌词"
```

### 收藏控制

```
"收藏当前歌曲"
"取消收藏这首歌"
```

## API 端点

| 端点 | 说明 |
|------|------|
| `GET /status` | 获取播放器状态 |
| `GET /lyric` | 获取 LRC 歌词 |
| `GET /lyric-all` | 获取所有类型歌词 |
| `GET /subscribe-player-status` | SSE 实时状态订阅 |
| `GET /play` | 播放 |
| `GET /pause` | 暂停 |
| `GET /skip-next` | 下一曲 |
| `GET /skip-prev` | 上一曲 |
| `GET /seek?offset=N` | 跳转进度 |
| `GET /volume?volume=N` | 设置音量 |
| `GET /mute?mute=true/false` | 静音控制 |
| `GET /collect` | 收藏 |
| `GET /uncollect` | 取消收藏 |

## 技术细节

- **协议**: HTTP GET
- **默认端口**: `23330`
- **无需认证**
- **工具依赖**: `curl`

## License

MIT
