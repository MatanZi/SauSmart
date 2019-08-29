import csv
import os
import random
import pandas as pd


dataset_path = os.path.dirname(os.path.abspath(""))


def build_soya():
    for i in range(1):
        soya = random.randint(10, 20)
        result = []

        while soya < 100:
                choose = random.randint(1, 10)
                break_time = random.randint(1, 10)
                if choose < 3 and break_time < 2:
                    for j in range(random.randint(2, 4)):
                        add = random.randint(1, 5)
                        soya += add
                        if soya > 100:
                            break
                        else:
                            result.append(soya)
                else:
                    result.append(soya)
        df = pd.DataFrame(result, columns=["volume"])
        df.to_csv("soya_"+str(i)+".csv")



def build_ketchup():
    for i in range(11):
        ketchup = random.randint(10,20)
        result = []

        while ketchup < 100:
            choose = random.randint(1, 10)
            break_time = random.randint(1, 10)
            if choose < 6 and break_time < 3:
                for i in range(random.randint(5, 7)):
                    add = random.randint(1, 5)
                    ketchup += add
                    if ketchup > 100:
                        break
                    else:
                        result.append(ketchup)
                else:
                    result.append(ketchup)
        df = pd.DataFrame(result, columns=["volume"])
        df.to_csv("ketchup_"+str(i)+".csv")



def build_mayo():
    for i in range(11):
        mayo  = random.randint(10, 20)
        result = []

        while mayo < 100:
                choose = random.randint(1, 10)
                break_time = random.randint(1, 10)
                if choose < 3 and break_time < 3:
                    for j in range(random.randint(3, 5)):
                        add = random.randint(1, 5)
                        mayo += add
                        if mayo > 100:
                            break
                        else:
                            result.append(mayo)
                else:
                    result.append(mayo )
        df = pd.DataFrame(result, columns=["volume"])
        df.to_csv("mayo_"+str(i)+".csv")



#build_mayo()
build_soya()
#build_ketchup()



