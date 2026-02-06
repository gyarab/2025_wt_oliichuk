import httpx
from colorama import Fore, Style, Back, just_fix_windows_console
# from datetime import datetime 

# current_date = datetime.now().strftime('%d.%m.%Y')
just_fix_windows_console() 

res = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

print(Style.DIM + "server odpovedel:", res.status_code)
print(Style.RESET_ALL)

lines = res.text.split('\n')
print("Kruzy pro den:", lines[0].split(" ")[0])

line_euro = ""
for line in lines:
    if "EUR" in line:
        line_euro = line
        break

rate_str = line_euro.split('|')[-1].replace(',' , '.')
rate = float(rate_str)

print("Kurz eura je", rate, "Kc")

print("Jaky chces prevod? ")
print() 
print("1) EUR -> CZK") 
print("2) CZK -> EUR")
print() 
mena_choice = input("vyber bud 1 nebo 2: ") 
 
if mena_choice == "1": 
    value_in = float(input("Kolik mas eur? "))
    value_out = value_in * rate
    print(Back.RED)
    print(f"Tak to je {value_out:.2f} korun.")

elif mena_choice == "2": 
    value_in = float(input("Kolik mas korun? "))
    value_out = value_in / rate
    print(Back.RED)
    print(f"Tak to je {value_out:.2f} eur.")

else: 
    print(Fore.RED) 
    print("neplatny vstup")
    
print(Style.RESET_ALL)
