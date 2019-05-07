def fizz_buzz(n):  #関数の定義開始
    n=n+1 #nの最後がカットされるので追加
    ans=[] #変数ansと配列の用意
    for i in range(0,n): #無いとnの値のみの判定になる
        if i%15==0:　#先に公倍数を除かないとfizzにもbuzzにも引っかかる
            ans.append('fizz_buzz')
        elif i%3==0:
            ans.append('fizz')
        elif i%5==0:
            ans.append('buzz')
        else:
            ans.append(i)　#それ以外の数字をそのまま出力する
    return ans　#まだわかん無い
#ここから関数の利用
ans=fizz_buzz(100) 
print(ans)


