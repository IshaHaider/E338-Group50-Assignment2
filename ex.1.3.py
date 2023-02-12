def improved_func(n, memo={}):
  if n == 0 or n == 1:
    return n
  if n not in memo:
    memo[n] = improved_func(n-1, memo) + improved_func(n-2, memo)
  return memo[n]
