def merge(a,b):
    c,m,n = [],len(a),len(b)
    i,j = 0,0
    while i+j < m+n :
        if i == m:
            c.append(b[j])
            j = j+1
        elif j == n:
            c.append(a[i])
            i = i+1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1


def mergesort(a,left,right):
    if right - left <= 1:
        return a[left:right]
    if right - left > 1:
        mid = (left + right)//2
        l = mergesort(a, left,mid)
        r = mergesort(a,mid,right)
        return merge(l,r)

lst = [2,6,5,1,3,4]
print(mergesort(lst,3,3))
