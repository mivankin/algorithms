"""
Knuth–Morris–Pratt algorithm
"""

def pi_function(a):
	"""
	pi function implementation
	"""
	p = [0]*len(a)
	i = 1
	j = 0
	while i < len(a):
		if a[i] == a[j]:
			p[i] = j+1
			i += 1
			j += 1
		elif j == 0:
			p[i] = 0
			i += 1
		else:
			j = p[j-1]

	return p

def str_find(t, a, p):
	"""
	Search algorithm O(n+m), where n - string length, m - substring length
	"""
	k = 0
	l = 0
	while k < len(t):
		if t[k] == a[l]:
			k += 1
			l += 1
			if l == len(a):
				return True
		elif l == 0:
			k += 1
			if k == len(t):
				return False
		else:
			l = p[l-1]
	return False
a = 'abcabcd'
t = 'fghgfdfghghabcabjsdjabcabcfjsdjasabcabfghfgherewrabcabcfghgfdfghghabcabjsdjabcabcfjsdjasabcabfghfgherewrabcabc'
out = pi_function(a)
flag = str_find(t,a,out)
print(flag)


