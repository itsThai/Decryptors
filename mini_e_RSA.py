# Without padding, encryption of m is m^e mod n: the message m is interpreted as an integer, then raised to exponent e, and the result is reduced modulo n. 
# If e = 3 and m is short, then m^3 could be an integer which is smaller than n, in which case the modulo operation is a no-operation. 
# In that case, you can just compute the cube root of the value you have. 
# However, we cannot simply compute c^(1/3) (where c is the ciphertext) because there is a slight amount of padding to the message to make m^e larger than n, which makes the modulo operation take effect.
# With a short m slightly wider than n^(1/e), which is what we have, we are given c = m^e mod n and can find by enumeration k such that k * n + c is an eth power: then m = (k * n + c)^(1/e). 




from decimal import *
from tqdm import tqdm

N = Decimal(29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331)
e = Decimal(3)
c = Decimal(6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717)


def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:-1]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii


# Find padding
getcontext().prec = 280  # Increase precision
padding = 0
for k in tqdm(range(0, 10_000)):
    m = pow(k * N + c, 1 / e)

    m_ascii = int_to_ascii(m)

    if "pico" in m_ascii:
        padding = k
        break

print("Padding: %s" % padding)

# Increase precision further to get entire flag
getcontext().prec = 700

m = pow(padding * N + c, 1 / e)
m_ascii = int_to_ascii(m)
print("Flag: %s" % m_ascii.strip())