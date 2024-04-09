import time
from datetime import date

t = time.time()
scientific_notation = f"{t:.2e}"

t = int(round(t, 4) * 10_000)

md = t // 10**13
ml = (t - md * 10**13) // 10**10
mi = (t - md * 10**13 - ml * 10**10) // 10**7
ce = (t - md * 10**13 - ml * 10**10 - mi * 10**7) // 10**4
de = (t - md * 10**13 - ml * 10**10 - mi * 10**7 - ce * 10**4)
print(f"Seconds since January 1, 1970: {md},{ml},{mi},{ce}.{de}")
print(f" or {scientific_notation} in scientific notation")
date = date.today()
month = date.ctime()[4:7:]
print(f"{month} {date.day} {date.year}")
