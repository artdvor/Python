mone = 5787.98
mone2 = mone

contribution = 6500
percent_bank = 0.16

def day_percent(mony, percent = percent_bank):
    return round(mony * percent/365)

print(day_percent(mone,0.22))


result = mone

for i in range(365*13):
    result += day_percent(result)
    if (i + 1) % 7 == 0:
        result += contribution
        print("+ " + str(contribution) + "рублей")
        mone2 += contribution
    print (str(i) +"    " + str(result) + "     " + str(day_percent(result)))

percent = result-mone2
print("Процент = " + str(percent)) 

print("Новый комит")