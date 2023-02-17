def generate(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

n=int(input())
r=[str(i) for i in generate(n)]
print(", ".join(r))