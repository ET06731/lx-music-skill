import sqlite3, sys, json

LX_DATA = r"%APPDATA%/lx-music-desktop/LxDatas/lx.data.db"


def get_playlists():
    conn = sqlite3.connect(LX_DATA)
    conn.text_factory = str
    c = conn.cursor()
    c.execute("SELECT id, name, source, sourceListId FROM my_list ORDER BY position")
    result = []
    for row in c.fetchall():
        result.append(
            {"id": row[0], "name": row[1], "source": row[2], "sourceId": row[3]}
        )
    conn.close()
    return result


def get_playlist_songs(list_id):
    conn = sqlite3.connect(LX_DATA)
    conn.text_factory = str
    c = conn.cursor()
    c.execute(
        f'SELECT m.name, m.singer FROM my_list_music_info_order o JOIN my_list_music_info m ON o.musicInfoId = m.id WHERE o.listId = ? ORDER BY o."order"',
        (list_id,),
    )
    result = [{"name": r[0], "singer": r[1]} for r in c.fetchall()]
    conn.close()
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps(get_playlists(), ensure_ascii=False, indent=2))
    elif sys.argv[1] == "songs" and len(sys.argv) >= 3:
        print(json.dumps(get_playlist_songs(sys.argv[2]), ensure_ascii=False, indent=2))
    elif sys.argv[1] == "play" and len(sys.argv) >= 3:
        import subprocess

        list_id = sys.argv[2]
        conn = sqlite3.connect(LX_DATA)
        conn.text_factory = str
        c = conn.cursor()
        c.execute("SELECT source, sourceListId FROM my_list WHERE id = ?", (list_id,))
        row = c.fetchone()
        conn.close()
        if row:
            source, sid = row
            if source == "wy":
                subprocess.run(
                    [
                        "powershell",
                        "-Command",
                        f'Start-Process "lxmusic://songlist/play/wy/{sid}"',
                    ]
                )
            elif source == "tx":
                subprocess.run(
                    [
                        "powershell",
                        "-Command",
                        f'Start-Process "lxmusic://songlist/play/tx/{sid}"',
                    ]
                )
            elif source == "kg":
                subprocess.run(
                    [
                        "powershell",
                        "-Command",
                        f'Start-Process "lxmusic://songlist/play/kg/{sid}"',
                    ]
                )
            elif source == "mg":
                subprocess.run(
                    [
                        "powershell",
                        "-Command",
                        f'Start-Process "lxmusic://songlist/play/mg/{sid}"',
                    ]
                )
            else:
                print("Unsupported source:", source)
        else:
            print("Playlist not found:", list_id)
