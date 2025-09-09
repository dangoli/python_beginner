n = int(input())
n_= n * 1000000
s = n_ # 落地时经历的路程
h = n_ * 0.03125 # 第五次落地后反弹高度
sum_s = n_ * 2.875 # 总路程
sum_fs = sum_s/1000000
print(f"{sum_fs:.6f}".rstrip('0').rstrip('.') if '.' in f"{sum_fs:.6f}" else f"{sum_fs:.6f}")
fh = h/1000000
print(f"{fh:.6f}".rstrip('0').rstrip('.') if '.' in f"{fh:.6f}" else f"{fh:.6f}")