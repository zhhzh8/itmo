try:
    c = True
    nums = [1, 2, 3, 4]
    target = 7
    for n in range(len(nums)):
        n1 = nums[n]
        for nn in range(len(nums)):
            if nn == n:
                pass
            else:
                n2 = nums[nn]
                if n1 + n2 == target:
                    print(n, nn)
                    c = False
    else:
        if c:
            print("Такой пары нет")

except Exception as e:
    print("Error:", e)
