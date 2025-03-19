fruits = {'apple', 'orange', 'pear', 'grape'} # 集合是无序的
counts = [10, 3, 5, 4]
for f, c in zip(fruits, counts):
    match f, c:
        case 'apple', 10:
            print('10个苹果')
        case 'orange', 3:
            print('3个橘子')
        case 'pear', 5:
            print('4个梨')
        case 'grape', 4:
            print('5串葡萄')