T = int(input())
def count(a,ans = 0):
    a = bin(a).replace("0b","")
    for i in range(len(a)):
        if a[i] == '1':
            ans = ans + 1
    return ans
for _ in range(T):
    N, A ,B = map(int , input().split())
    ans = min(count(A) , N - count(B)) + min(count(B) , N - count(A))
    final =''
    for _ in range(ans):
        final = final + '1'
    for _ in range(N - ans):
        final = final + '0'
    print(int(final , 2))