import re
from sys import setrecursionlimit
# setrecursionlimit(10 ** 6) 再帰上限を増やす
from math import ceil, floor, sqrt, pi, factorial, gcd, atan2, degrees
# ceil(x) xの小数点以下を切り上げ
# floor(x) xの小数点以下を切り捨て
    # int() は0への丸め
    # floor() は負の無限大への丸め
# sqrt(x) xの平方根を返す
# pi 利用可能なだけの精度の数学定数π = 3.141592…（円周率）
# factorial(x) xの階乗を整数で返す。負の場合はValueError
# gcd(x, y) xとyの最大公約数を返す
# atan2(y, x) atan(y / x)を、ラジアンで返す。戻り値は-piからpiの間にある。
#             この角度は、極座標平面において原点から(x, y)へのベクトルがX軸の正の方向となす角である。
#             atan2()のポイントは、両辺の入力の符号が既知であるために、位相角の正しい象限を計算できることにある
#             例えば、atan(1)とatan2(1, 1)はいずれもpi/4だが、atan2(-1, -1)は-3*pi/4になる 
# degrees(x) 角xをラジアンから度に変換する
# radians(x) 角xを度からラジアンに変換する

from decimal import Decimal



# -----------------------------------------------------
# リストの最小公倍数を返す
def lcm(a):
    from math import gcd
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x
# -----------------------------------------------------
from copy import deepcopy
from collections import Counter, deque, defaultdict
    # Q = deque()
    # Q.append(x)
    # Q.appendleft(x) xをQの先頭に追加する
    # Q.pop() Qの末尾を取り出し、その値を返す
    # Q.popleft() Qの先頭を取り出し、その値を返す

    # defaultdict() dictの初期化を関数に従って実施する事が出来る
    # そのため存在チェックが不要
    # defaultdict(int) と記述した場合「lambda:int()」と同じ意味
    # 「int()」は「0」を返すので、これは「lambda:0」と同じ動作になる
    # つまり「0を返す関数」になるので、初期値が0になる。

from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
# combinations(iterable, r) 入力iterableの要素からなる長さrの部分列を返す
# permutations(iterable, r) 入力iterableの要素からなる長さrの順列を返す

from bisect import bisect, bisect_left, bisect_right
    # このモジュールは、挿入の度にリストをソートすることなく、リストをソートされた順序に保つことをサポートする。
    # 大量の比較操作を伴うような、アイテムがたくさんあるようなリストでは、より一般的なアプローチに比べて、パフォーマンスが向上する。
    # 動作に基本的な二分法アルゴリズムを使っているので、bisectと呼ばれる。
    # 
    # bisect(a, x, low=0, high=len(a))
        # aに含まれるxのうち、どのエントリーよりも後ろ（右）にくるような挿入点を返す。
        # 返された挿入点iは、配列aを二つに分け、all(val <= x for val in a[low:i])が左側に、
        # all(val > x for val in a[i:high])が右側になるようにする。

    # bisect_left(a, x, low=0, high=len(a))
        # ai >= k であるインデックスiのうち最小のものを返す。
        # もし存在しない場合はlen(a)を返す。

        # ソートされた順序を保ったままxをaに挿入できる点を探し当てる。
        # リストの中から検索する部分集合を指定するには、パラメータのlowとhighを使う。
        # デフォルトでは、リスト全体が使われる。
        # xがすでにaに含まれている場合、挿入点は既存のどのエントリーよりも前（左）になる。
        # 戻り値は、list.insert()の第一引数として使うのに適している。aはすでにソートされているものとする。
        # 
        # 返された挿入点iは、配列aを二つに分け、all(val < x for val in a[low:i])が左側に
        # all(val >= x for val in a[i:high])が右側になるようにする。


    # bisect_right(a, x, low=0, high=len(a))
        # 
        #  






from functools import reduce
from decimal import Decimal, getcontext
    # Decimal(整数) 正確に丸められた十進浮動小数点算術をサポート



# ---------------------------------------------------------
# ord('文字') asciiコードに変換 
# chr(数値) 文字に変換
# T.find(sub[, [start:end]]) 文字列スライスs[start:end] に部分文字列subが含まれる場合、その最小の引数を返す
# 
# bin(x) 数値を2進数に変換する
# oct(x) 数値を8進数に変換する
# hex(x) 数値を16進数に変換する
# それぞれプレフィックス 0b, 0o, 0xがついた文字列（str）を返す
# bin_num = 0b10
# print(bin_num)で2を出力


# 組み合わせの総数を求める
def nCr(n, r):
    if n >= r:
        return factorial(n) // (factorial(r) * factorial(n - r))
    else:
        return 0

# nC2を求める
def choose2(n):
    return n * (n - 1) // 2