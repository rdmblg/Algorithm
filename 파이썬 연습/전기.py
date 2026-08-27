base = 270
use = int(input("전기 사용량 : "))
if use > 100 :
  cost = (use * base) + (use * base) * 0.2
else :
  cost = use * base
print("전기 사용량 : %dkW" % (use))
print("전기 요금 : %d원" % (cost))
input("\n엔터를누르세요")
