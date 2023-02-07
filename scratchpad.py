import random

def ssp():
    s = 0
    m = 0
    while s < 3 or m < 3:
        maskinSsp = random.choice(["stein", "saks", "papir"])
        print(maskinSsp)
        velgSsp = input("Stein, saks, papir\n").lower()
        print(velgSsp)
        if maskinSsp == velgSsp:
            print("Uavgjort")
        elif maskinSsp == "stein" and velgSsp == "saks" or maskinSsp == "saks" and velgSsp == "papir" or maskinSsp == "papir" and velgSsp == "stein":
            print("Maskin vant.\n Maskin:", str(m), "\nSpiller:", str(s))
            m += 1
        elif velgSsp == "stein" and maskinSsp == "saks" or velgSsp == "saks" and maskinSsp == "papir" or velgSsp == "papir" and maskinSsp == "stein":
            print("Spiller vant.\n Maskin:", str(m), "\nSpiller:", str(s))
            s += 1
    if s == 3:
        print("Spiller vant.")
    elif m == 3:
        print("Maskin vant.")
ssp()