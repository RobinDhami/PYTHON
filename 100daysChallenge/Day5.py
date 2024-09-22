l =[34,67,1,90,0,54]
print(max(l))
l.insert(0,0)
l.extend([100,10000])
l.remove(10000)
print(l)
s = "Rabin Dhami"
print(s.count("a"))
s1 = list(s)
st=set()
for i in s1:
    if i!=" ":
        st.add(i)
print(list(st))