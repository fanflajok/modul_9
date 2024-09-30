def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        count = 0
        for i in range(1, res+1):
            if res % i == 0:
                count +=1
        if count <= 2:
            print(f'{res} - простое число')
        else:
            print(f'{res} - составное число')
        return res
    return wrapper

@is_prime
def sum_three(*nums):
    sm = sum(nums)
    return sm

result_sum = sum_three(600,2,3,4,543,800017465)
print(result_sum)

