def fifo(requests, cache_size):
    cache = []
    for page in requests:
        if page in cache:
            print("hit")
        else:
            print("miss")
            if len(cache) < cache_size:
                cache.append(page)
            else:
                cache.pop(0)
                cache.append(page)
    print(cache)
    cache.clear()

def lfu(requests, cache_size):
    cache = []
    freq = {}
    for page in requests:
        if page in cache:
            print("hit")
            if page not in freq:
                freq[page] = 1
            else:
                freq[page] += 1
        else:
            print("miss")
            if len(cache) < cache_size:
                cache.append(page)
                freq[page] = 1
            else:
                min_freq = float('inf')
                page_to_evict = -1
                for i, cached_page in enumerate(cache):
                    if cached_page not in freq:
                        min_freq = 0
                        page_to_evict = cached_page
                        break
                    elif freq[cached_page] < min_freq:
                        min_freq = freq[cached_page]
                        page_to_evict = cached_page
                cache.remove(page_to_evict)
                cache.append(page)
                freq[page] = 1
    print(cache)

def main():
    requests = []
    while True:
        request = input("Enter a page request (or 'Q' to quit): ")
        if request == 'Q':
            break
        requests.append(request)
    cache_mgt = input("Enter 'FIFO' for FIFO replacement, 'LFU' for LFU replacement: ")
    if cache_mgt == 'FIFO':
        fifo(requests, 8)
    elif cache_mgt == 'LFU':
        lfu(requests, 8)
    else:
        print("Invalid cache management policy")
