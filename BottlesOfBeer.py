# 99 Bottles of Beer (by Gerold Penz)
for quant in range(99, 0, -1):
    if quant > 1:
        print(f"{quant} bottles of beer on the wall, {quant} bottles of beer.")
        if quant > 2:
            suffix = (f"{str(quant - 1)} bottles of beer on the wall.")
        else:
            suffix = (f"1 bottle of beer on the wall.")
    elif quant == 1:
        print(f"1 bottle of beer on the wall, 1 bottle of beer.")
        suffix = (f"no more beer on the wall!")
    print(f"Take one down, pass it around, {suffix}")
    print(f"--")