import sys

input = sys.stdin.readline
N, K = map(int, input().split())
products = list(map(int, input().split()))
multi_tab = [0] * N
ans = 0
change = maximum = 0

while products:
    product = products[0]
    # 멀티탭에 동일한 제품이 꽂혀있을 경우
    if product in multi_tab:
        products.remove(product)
        continue

    # 멀티탭에 빈자리가 있을 경우
    if 0 in multi_tab:
        multi_tab[multi_tab.index(0)] = product
        products.remove(product)
        continue

    for mt in multi_tab:
        # 멀티탭에 꽂혀있는 제품 중 이후에 꽂는 제품이 없는 경우
        # 이후에 꽂는 제품이 없는 제품을 빼주고 탐색중인 제품을 꽂는다.
        if mt not in products:
            change = mt
            break

        # 멀티탭에 꽂혀있는 제품 중 가장 나중에 사용하는 제품을 고름.
        # -> 가장 나중에 사용하는 제품을 뽑고 탐색하고 있는 제품을 꽂는다.
        elif products.index(mt) > maximum:
            maximum = products.index(mt)
            change = mt

    # 선택된 제품 꽂아주고, products에서 제거해주기
    multi_tab[multi_tab.index(change)] = product
    products.remove(product)
    maximum = 0
    ans += 1

print(ans)