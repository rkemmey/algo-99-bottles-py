def bottle_song():
	# write your code here!
	# 99 bottles of beer on the wall, 99 bottles of beer.
	for i in range(99, 0, -1):
		if i == 2:
			print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
			print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
		if i == 1:
			print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
			print(f"Take one down and pass it around, no more bottles of beer on the wall.")
			print("No more bottles of beer on the wall, no more bottles of beer.")
			print("Go to the store and buy some more, 99 bottles of beer on the wall.")
		else:
			print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
			print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")

bottle_song()

####kldjsfalkfdajalskdfjdfls