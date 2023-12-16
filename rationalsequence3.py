for _ in range(int(input())):
    k,n=map(int,input().split())
    st=[]
    while n>1:
        if n%2:
            st.append('Right')
        else:
            st.append('Left')
        n//=2
    p,q=1,1
    while st:
        if st[-1]=='Left':
            q=p+q
        else:
            p=p+q
        st.pop()
    print(str(k)+' '+str(p)+'/'+str(q))
    
        