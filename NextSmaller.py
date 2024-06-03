nums = [3,2,1,4,8]
result = [0]*len(nums)
st = []
k = len(result)-1

for n in reversed(nums):
    while st and st[-1] >= n:
        st.pop()
    if not st:
        result[k] = -1
        k -= 1
    else:
        result[k] = st[-1]
        k -= 1
    st.append(n)
for i in result:
    print(i)