from pathlib import Path
import datetime
import pytz

import feedparser

def update_footer():
    timestamp = datetime.datetime.now(pytz.timezone("Europe/Berlin")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)

readme = Path('../README.md').read_text()

with open('../README.md', "w+") as f:
    f.write(readme + update_footer())
