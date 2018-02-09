"""
todo 
"""

def erathostene (n):
	""" todo
	"""
	liste_premier = []
	liste_supprime = []
	for i in range(2,n):
		for j in range (i,n):
			liste_supprime.append(i*j)
		if i not in liste_supprime:
			liste_premier.append(i)
	return liste_premier


if __name__=="__main__":
	a = input ()
	print erathostene(a)
