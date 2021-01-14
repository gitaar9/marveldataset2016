from urllib.request import urlopen, Request


sourceLink = "http://www.shipspotting.com/gallery/photo.php?lid="
ID = "1495125"
url = sourceLink + ID

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req, timeout=300).read()
