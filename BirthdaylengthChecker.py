from datetime import datetime
now = datetime.now()
next_bday = datetime(now.year, 3, 7)
if next_bday < now:
    next_bday = next_bday.replace(now.year + 1)
diff = next_bday - now
days = diff.days
print(days)
