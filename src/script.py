from pathlib import Path
import datetime
import pytz
import requests

def update_footer():
    url = "https://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote"
    response = requests.request("GET",url,verify=False)
    quote = response.json()["content"]
    readme = Path('../README.md').read_text()
    timestamp = datetime.datetime.now(pytz.timezone("Europe/Berlin")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp,quote=quote)



with open('../README.md', "w+") as f:
    f.write(readme[:readme.find("<hr>")] + update_footer())
