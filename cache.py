
def fifo():
	global requests
	global cache
	for page in requests:
		if page in cache:
			print("hit")
			# pos = cache.index(page)
			# # cache.pop(pos)
			# cache.append(page)
		else:
			print('miss')
			if len(cache) < 8:
				cache.append(page)
			else:
				cache.pop(0)
				cache.append(page)
	print(cache)
	cache.clear()

def lfu():
	# freq = [0] * 8 # {0, 0, 0, 0, 0, 0, 0, 0, 0}
	cache = []
	freq = {}

	for page in requests:
		if page in cache:
			print("hit")
			# pos = cache.index(page)
			if page not in freq:
				freq[page] = 1
			else:
				freq[page] += 1
		else:
			print("miss")
			if len(cache) < 8:
				cache.append(page)
				freq[page] = 1
				# freq[len(cache) - 1] += 1
			else:
				# pos = freq.index(min(freq))

				min_freq = -1
				page_to_evict = -1
				pos = -1

				for i in range(0, len(cache)):
					cached_page = cache[i]
					if cached_page in freq:
						if min_freq == -1 or min_freq > freq[cached_page]:
							min_freq = freq[cached_page]
							page_to_evict = cached_page
							pos = i
							continue
						if min_freq == freq[cached_page]:
							if cached_page < page_to_evict:
								page_to_evict = cached_page
								pos = i

				# cache[pos] = page # evict old and put new page
				del cache[pos]
				cache.append(page)
				if page in freq:
					freq[page] += 1
				else:
					freq[page] = 1

	print(cache)


requests = []
cache = []

while True:
	request = int(input())
	if request == 0:
		cache_mgt = input("Enter 1 for Fifo, 2 for LFU and Q to quit): ")
		if cache_mgt == '1':
			fifo()
		elif cache_mgt == '2':
			lfu()
		elif cache_mgt == 'Q':
			quit()
		else:
			print("type 1, 2, or Q")
	requests.append(request)
