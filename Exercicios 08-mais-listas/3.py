def substitui(s, old, new):
    s_new=s
    for i in range(len(s)):
        if s_new[i]==old:
            if i==0:
                s_new=new+s[1:]
            if i==len(s)-1:
                s_new=s_new[:i]+new
            if i>len(s)-1:
                break
            s_new=s_new[:i]+new+s_new[i+1:]
    return s_new
                
