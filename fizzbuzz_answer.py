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

"""
わからないポイントの解説

return ans
がわからないということで、わからないポイントとして考えられる2つのこと
1:関数について
関数は基本的に
def 関数名(引数,引数,...):
    処理
    return 返り値
という形で成り立ってるんだけど
関数はある計算をやってくれるアプリみたいなものだと考えよう
"n-buna"って引数を入れると"ヨルシカまじいいよね"って返り値が来るみたいな
[1,2,3,4,5,6,7,8,9,10]って引数入れると55(合計)って出るみたいな
なんでも作れるのがこの関数
関数名、引数は予約語以外なら何でもよい。

2:ansについて
この問題でのansの立ち位置は最終的な計算結果を出すためのもの
3行目にて、ansは最初に空の配列として設定した   ans = []
これに計算結果をどんどん入れていくのがfor文での処理だった

配列に要素を入力するには
配列.append(追加要素)
という宣言だったから
今回はans.append(追加要素)、"fizz_buzz"だったりi（数字）だったり
を各処理で入れていったんだね

これによってansには
ans = ['fizz_buzz', 1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizz_buzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizz_buzz', 31, 32, 'fizz', 34, 'buzz', 'fizz', 37, 38, 'fizz', 'buzz', 41, 'fizz', 43, 44, 'fizz_buzz', 46, 47, 'fizz', 49, 'buzz', 'fizz', 52, 53, 'fizz', 'buzz', 56, 'fizz', 58, 59, 'fizz_buzz', 61, 62, 'fizz', 64, 'buzz', 'fizz', 67, 68, 'fizz', 'buzz', 71, 'fizz', 73, 74, 'fizz_buzz', 76, 77, 'fizz', 79, 'buzz', 'fizz', 82, 83, 'fizz', 'buzz', 86, 'fizz', 88, 89, 'fizz_buzz', 91, 92, 'fizz', 94, 'buzz', 'fizz', 97, 98, 'fizz', 'buzz']
という結果が入力されたから
この関数を使うとansの結果が出力されるんだ

"""
