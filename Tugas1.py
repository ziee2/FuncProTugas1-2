# kode 1
def Kode1_sijawir(start, stop):
    x = []
    for i in range(start, stop+1):
        x.append(i)
    return x

### UBAH KODE JADI SATU BARIS
sequenceGenerator = lambda start, stop : [i for i in range(start, stop+1)]

# kode 2
def Kode2_sijawir(a,b):
    x = []
    for num in range(a,b):
        if num % 3 == 0 and num % 5 == 0:
            x.append('fizzbuzz')
        elif num % 3 == 0:
            x.append('fizz')
        elif num % 5 == 0:
            x.append('buzz')
        else:
            x.append(num)
    return x

### UBAH KODE JADI SATU BARIS
fizzBuzz = lambda a, b: ['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(a, b)]

# kode 3
def kode3_sijawir(l):
    res = []
    for i in l:
        if l.index(i) == len(l) - 1 :
            break
        z = i + l[i+1]
        res.append(z)
    return res

### UBAH KODE JADI SATU BARIS
twoNumber = lambda l : list(filter(lambda l : True if l != None else None,list(map(lambda x : None if l.index(x) == len(l)-1 else x + l[l.index(x) + 1], l))))


print(sequenceGenerator(1, 10))
print(fizzBuzz(1, 11))
print(twoNumber([2, 4, 0, 7]))