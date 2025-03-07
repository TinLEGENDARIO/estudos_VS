a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'A={nome2} B={nome1} C={nome1} D={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

############################################

e = "E"
f = "F"
g = 1.2
formato = "E={} F={} G={}".format(e, f, g)

print(formato)