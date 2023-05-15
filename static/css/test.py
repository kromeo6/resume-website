def isPossible(nums) -> bool:
    last_rep_ind = -1
    first_big_step = -1
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            last_rep_ind = i
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            first_big_step = i
            break
    if last_rep_ind > first_big_step and first_big_step >= 0:
        return False

    last_a = nums[0]
    len_a = 1
    last_b = False
    len_b = 0
    for i in range(1, len(nums)):
        print(last_a, last_b)
        if (nums[i] == last_a +1 and len_a < 3) or (nums[i] == last_a +1 and i <= last_rep_ind) or (nums[i] == last_a +1 and i <= first_big_step):
            last_a += 1
            len_a += 1
        elif (len_b == 0) or (nums[i] == last_b +1):
            last_b = nums[i]
            len_b += 1
        else:
            return False
    if len_a > 2 and len_b > 2:
        return True
    else:
        return False

nums = [1,2,3]
print(isPossible(nums))