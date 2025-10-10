A = {x for x in range(1, 11, 2)}

B = {x for x in range(2, 11, 2)}
print("A =", A)
print("B =", B)

# C = {1,2,3,4,5}
# D = {4,5,6,7}
# irisan = C&D
# gabungan = C|D
# selisih_1 = C-D
# selisih_2 = D|C
# beda_setangkup = D^C
# print ('irisan himpunan a dan b=', irisan)
# print ('gabungan himpunan a dan b=', gabungan)
# print ('selisih himpunan a dan b=', selisih_1)
# print ('selisih himpunan b dan a=', selisih_2)
# print ('beda setangkup himpunan a dan b=', beda_setangkup)

import matplotlib.pyplot as plt
from matplotlib_venn import venn2,venn2_circles
A = {1,2,3,4,5}
B = {4,5,6,7}
S = {1,2,3,4,5,6,7,8,9,10}
irisan = A & B
gabungan = A|B
selisih_1 = A-B
selisih_2 = B-A
beda_setangkup = A^B
komplemenA = S-A
komplemenB = S-B
print("irisan himpunan A dan B=", irisan)
print("gabungan himpunan A dan B=",gabungan)
print("selisih himpunan A dan B=", selisih_1)
print("selisih himpunan B dan A=", selisih_2)
print("beda setangkup himpunan A dan B=", beda_setangkup)
print("komplemen dari himpunan A=", komplemenA)
print("komplemen dari himpunan B=", komplemenB)
venn=venn2(subsets=(len(A-B),len(B-A),len(irisan)),set_labels=('A','B'))
plt.show()