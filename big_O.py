def a(n):
  return (1000 * n) + 10 ** 6

def b(n):
  return 10 + n ** 2

def c(n):
  return 0.01 * n ** 3

def check(fun_1, fun_2, n):
  while fun_1(n)<fun_2(n):
    n+=1
  return n

result_1 = check(c, b, 0)
result_2 = check(b, a, result_1)
print("f(0.01*n**3) < f(10+n**2), if n: [ 0:",result_1-1,"]")
print("f(10+n**2) < f((1000*n)+10**6), if n: [",result_1,":",result_2-1,"]")
print("f((1000*n)+10**6) < f(10+n**2), if n: [",result_2,": ∞]")