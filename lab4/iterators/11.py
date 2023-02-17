def generate(n):
    for i in range(n,0,-1):
        yield i

n=int(input())
r=[str(i) for i in generate(n)]
print(",".join(r))