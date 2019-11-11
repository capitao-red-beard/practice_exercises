def min_coins(cents):
	dict_coins = {25: 0, 10: 0, 5: 0, 1: 0}

	for c in dict_coins:
		if cents < 1:
			return dict_coins
		while cents / c >= 1:
			cents -= c
			dict_coins[c] += 1
			if cents == 0:
				return dict_coins

print(min_coins(35))
