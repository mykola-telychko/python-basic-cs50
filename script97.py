def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

# print(total(100, 50, 25), "Knuts")
# print(total(coins[0], coins[1], coins[2]), "Knuts")
# print(total(galleons=45, sickles=67, knuts=4), "Knuts")

coins2 = {"galleons": 45, "sickles": 67, "knuts": 4}
print(total(**coins2), "Knuts")

# coins1 = [100, 50, 25]
# print(total(*coins1), "Knuts")
