even=[] #配列の用意
odd=[]
ans=0 #わかんない　引数を配列にするとエラー
for i in range(1,10001):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
for i in range(int(10000/2)): #0,5000とかにすると0をintできずエラー.
    ans +=even[i]*odd[i]  #+=わかんない
print(ans)
