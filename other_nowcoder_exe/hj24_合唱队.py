n = input()
heights = input().split(' ') # 输入身高

def main(): #  
    nums = list(map(int, input().split()))
    n = len(nums)
    if n == 0:
        print(0)
        return
        
    left_inc = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if left_inc[j] + 1 > left_inc[i]:
                    left_inc[i] = left_inc[j] + 1
                    
    right_dec = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                if right_dec[j] + 1 > right_dec[i]:
                    right_dec[i] = right_dec[j] + 1
                    
    max_length = 0
    for i in range(n):
        current_length = left_inc[i] + right_dec[i] - 1
        if current_length > max_length:
            max_length = current_length
            
    min_deletions = n - max_length
    print(min_deletions)

if __name__ == '__main__':
    main()