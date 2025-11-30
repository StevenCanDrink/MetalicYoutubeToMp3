def ydl_opts(download_dir):

    return {
        "format": "bestaudio/best",
        "outtmpl": f"{download_dir}/%(title)s.%(ext)s",
        "noplaylist": True,
        "ignoreerrors": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "retries": 5,
        "fragment_retries": 10,
        "quiet": False,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.youtube.com/",
        },
        "extract_flat": False,
        "ignore_no_formats_error": False,
        "cookiefile": "cookies.txt",  # Optional: Use if you have cookies
        "socket_timeout": 30,
        "extractor_args": {
            "youtube": {
                "player_client": ["android"],  # Bypass some restrictions
                "skip": ["dash", "hls"],  # Avoid problematic formats
            },
        },
        "throttled_rate": "1M",  # Slow down to avoid bans
        "retry_sleep_functions": {
            "http_403": lambda n: 5 + 2 * n,  # Wait longer on 403 errors
        },
        "force_ipv4": True,  # Avoid IPv6 issues
        "sleep_interval": 2,  # Add delay between requests
    }
