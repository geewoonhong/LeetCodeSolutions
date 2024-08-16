def move_zeroes(nums):
    rd = 0
    wrt = 0
    nums_size = len(nums)

    if nums_size == 0:
        return

    while rd < nums_size:
        if nums[rd] != 0:
            nums[wrt] = nums[rd]
            wrt += 1
        rd += 1

    while wrt < nums_size:
        nums[wrt] = 0
        wrt += 1

nums = [0,1,0,3,12]
move_zeroes(nums)
print(nums)
