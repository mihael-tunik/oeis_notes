storage = set()

def dfs(a, k):
    if k == 0:
        #print(a)
        storage.add(tuple(a))
        return
        
    n = len(a)
            
    for i in range(n):
        tmp = a[i]
        a[i] = max(a[i], k)
        dfs(a, k-1)
        a[i] = tmp

for n in range(1, 8):
    a = [0]*n
    storage.clear()
    dfs(a, n) 
    print(len(storage))
