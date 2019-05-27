def maxoftwo(x,y):
  if x > y:
    return x
  else:
    return y
def maxofthree(x,y,z):
  return maxoftwo(x, maxoftwo(y,z))
print(maxofthree(14,9,8))