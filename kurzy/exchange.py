import httpx

res = httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/index.html?date=22.01.2026")

print("Server answered", res.status_code)
lines = res.text.split('\n')
print("kurzy pro den", lines[0].split(' ')[0])  # první řádek tabulky