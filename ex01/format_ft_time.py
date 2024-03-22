import time

t = time.time() #float
scientific_notation = f"{t:.2e}"

t = int(round(t, 4) * 10_000)

md = t // 10**13
ml = (t - md * 10**13) // 10**10
mi = (t - md * 10**13 - ml * 10**10) // 10**7
ce = (t - md * 10**13 - ml * 10**10 - mi * 10**3) // 10**4

print(t)
# time_str = str(t)
# a = ["lol", "danil", "elsie"]
# print(time_str[1:4])
print(f"Seconds since January 1, 1970: {md}, {ml}, {mi}, {ce}. {} or {scientific_notation} in scientific notation") 