
def power(N, P):

	if P == 0:
		return 1

	return (N*power(N, P-1))



print(power(5, 2))
