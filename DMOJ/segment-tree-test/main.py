import sys
sys.stdin = open("dt.txt")
input = sys.stdin.readline

N,M = map(int,input().split())
SEG = [0] * (N<<2+1)

def build(arr,tree,v,l,r): 	# Recursively build into tree with array arr				
	if l == r: 				# at current vertex v and corresponding [l,..,r]
		tree[v] = arr[l]
	else:
		mid = (l+r) >> 1
		build(arr,val<<1,l,mid)
		build(arr,val<<1 + 1,mid+1,r)
		tree[val] = tree[val<<1] + tree[val<<1+1]
#build(a,SEG,1,0,n-1)

def getmin(tree=SEG,val,tl,tr,l,r): # Current bounds l,r, subtree bounds tl tr
	if l > r:
		return 0
	elif tl == l and tr == r:
		return tree[val]
	else:
		mid = (tl + tr) >> 1
	return min(getmin(tree,val<<1,tl,mid,l,min(r,mid)), getmin(tree,val<<2+1,mid+1,tr,max(l,mid+1),r))

def update(tree=SEG,i,tl,tr,pos,new): # Updates tree[i] to new
	if tl == tr:
		tree[val] = new
	else:
		mid = (tl+tr) >> 1
		if pos <= mid:
			update(tree,val<<2,tl,mid,pos,new)
		else:
			update(tree,val<<2+1,mid + 1,tr,pos,new)
		tree[val] = min(tree[val<<2],tree[val<<2+1])

