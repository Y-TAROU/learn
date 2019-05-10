even=[] #配列の用意
odd=[]
ans=0 #わかんない　引数を配列にするとエラー
for i in range(1,10001):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

for i in range(0,5000): #0,5000とかにすると0をintできずエラー.
    ans +=even[i]*odd[i]  #+=わかんない
print(ans)

"""
１：3行目のans = 0について
先ほどのfizz_buzzではansが配列だったのになぜに0なん？しかもなぜにエラー出るん！？
って思ったでしょう(笑)
それはansの役割が違うからなのさ

先ほどのfizz_buzzでは出力の結果を配列で出したかった。だからans = []と配列で準備して追加していった
でも今回はすべてを掛け算（内積）した整数値（int）で出力したかったからans = 0と初期値を用意したんだ

もちろん名前はansじゃなくてkekkaでもnaisekiでもdotでもいい

次に配列にするとエラーになる理由。
それは11行目、ans +=even[i]*odd[i]の説明で記述することにしよう

２：10行目について
fot i in range(0,5000)になるとエラーになるって書いてあるけど、多分エラーにならないよ
エラーになるのはfor i in range(0,5001)とかかな、これに変えて実行してみると
Error:list index out of range
って出てくるはず、これは用意されている配列よりもはみ出てますよ、参照できる配列の要素がありませんよって意味
これが出るときは基本for文で多めにやってたり配列の用意する桁が違ってたりするから配列の処理をするところを確認しよう

３：12行目、ans +=even[i]*odd[i]について
これは ans = ans + even[i]*odd[i]をしてるって意味
ややこしいけど、ans(これは結果を入れてる値)自身の値を更新してるって意味

数学Bを思いだしてほしいんだけど、漸化式ってあったよね
x_n+1 = x_n + 1 (N>=1,x_1 = 0)
みたいな、これをやってるのと同じことなんだよね
この漸化式だと
x_(n+1) = x_(n) + 1 = x_(n-1) + 1 + 1 = x_(n-2) + 1 + 1 + 1 = ... =x_(1) + 1 + 1 + 1 + ... + 1 = n
こんな感じで今回のans も次々に値を入れて更新してるのさ

ややこしい感じで書いたけど、結局それぞれの配列の掛け算の結果を足しているにすぎないのさ
[1,3,5,7,9,11,...]
 * * * * * * ...
[2,4,6,8,10,12,]
 = = = = = = ...
 2,12,30,56,90,132,...←これがそれぞれの要素の掛け算
これを足していく
ans = 2+12+30+56+90+132...
ってやっていった答えが166691665000なんだね

ans = 0
ans = ans + 2 #ans = 2
ans = ans + 12 #ans = 14
ans = ans + 30 #ans = 44
ans = ans + 56 #ans = 100
ans = ans + 90 #ans = 190
ans = ans + 132 #ans = 322
...
ans = ans + 99*100 #ans = 166691665000
"""
