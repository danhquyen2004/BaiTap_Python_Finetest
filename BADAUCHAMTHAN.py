s = input("Nhap chuoi: ")
dem = 0
if(s[len(s)-1]=='!'):
    dem+=1
    if(len(s)>1):
        if(s[len(s)-2]=='!'):
            dem+=1
            if(len(s)>2):
               if(s[len(s)-3]=='!'):
                    dem+=1
if(dem==0):
    s+='!!!'
elif(dem==1):
    s+='!!'
elif(dem==2):
    s+='!'
print(f"Chuoi sau khi bo sung dau cham than: '{s}'")