import requests

URL = "https://onionoo.torproject.org/details?type=relay&running=true"

r = requests.get(URL, timeout=30)
r.raise_for_status()
data = r.json()

lines = []
for relay in data.get("relays", []):
    fingerprint = relay.get("fingerprint", "")
    nickname = relay.get("nickname", "")
    address = relay.get("or_addresses", [""])[0]
    country = relay.get("country", "")
    bw = relay.get("observed_bandwidth", 0)

    lines.append(f"{fingerprint} | {nickname} | {address} | {country} | {bw}")

with open("relays.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
