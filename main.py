# args are for entering as many arguments as possible
# def a_sum(*args):
#   for num in args:
#     print(num)


# print(a_sum(1))
# print(a_sum(1, 3))
# print(a_sum(1, 2, 3, 4, 5, 6))
list=[3,4,5,6,7,8,9,45,67]

def a_sum(*args):
  # total = 0
  # for num in args:
  #   total += num
  # return total
  return sum (args)
print(a_sum(4,56,77,88,9,45,76))