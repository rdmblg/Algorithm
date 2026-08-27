tree = int(input("나무 조각의 개수 : "))
#인형 한 개를 만들 때 필요한 나무 조각의 개수 = 6개     doll * 6 = 인형을 만들 때 필요한 총 나무 조각의 개수
doll = int(input("만들 인형의 개수 : "))
if doll * 6 > tree :
    print("나무 조각이 %d개 부족해서 %d개를 만들 수 없습니다. 만들 수 있는 인형의 개수는 %d개 입니다." % (doll * 6 - tree,  doll, tree / 6))
else :
    print("만들 수 있는 인형의 개수는 %d개 입니다. 만든 인형은 %d개 입니다." % (tree / 6, doll))
    
 X = input("인형을 만들고 싶으신가요 :")
input("\n엔터를누르세요")
  
