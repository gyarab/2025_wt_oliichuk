import httpx

r = httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/index.html?date=15.01.2026")
lines = r.text.splitlines()

print(lines[0])