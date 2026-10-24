from uzay_oyunu.fibonacci import fib_say, fib_say_cache, fib_cache_say


fib_say.cagri = 0
fib_say_cache.cagri = 0
fib_say_cache.__wrapped__.cache_clear()
fib_cache_say.cache_clear()
fib_cache_say.__wrapped__.cagri = 0

print("Fibonacci:", fib_say(20), fib_say_cache(20), fib_cache_say(20))
print("Yalnızca @say:", fib_say.cagri)
print("@say üstte, @lru_cache altta:", fib_say_cache.cagri)
print("@lru_cache üstte, @say altta:", fib_cache_say.__wrapped__.cagri)