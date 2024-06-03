nums = [3,2,1,4,8]
result = [0] * len(nums)
st = []
k = 0

for num in nums:
    while st and st[-1] >= num:
        st.pop()
    if not st:
        result[k] = -1
        k += 1
    else:
        result[k] = st[-1]
        k += 1
    st.append(num)

for i in result:
    print(i)