# disc01

### 1. Control

#### If statements and Boolean operators

```py
def wears_jacket_with_if(temp, raining):
	"""
	>>> wears_jacket_with_if(90, False)
	False
	>>> wears_jacket_with_if(40, False)
	True
	>>> wears_jacket_with_if(100, True)
	True
	"""
	if temp <= 60 or raining:
		return False
	else:
		return True
```

```py
def wears_jacket(temp, raining):
	return temp < 60 and not raining
```

#### While loops

no answer

```py
def is_prime(n):
	i = 2
	while i < n / 2 + 1:
		if n % i == 0:
			return True
	return False
```

