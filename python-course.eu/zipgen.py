def zipgen():
	count=0
	while True:
		print("count:%d" % count)
		try:
			if count % 2 == 0:
				yield "first"[count]
				#yield "second"[count]
			else:
				yield "second"[count]
				#yield "first"[count]
		except:
			return
		count += 1
