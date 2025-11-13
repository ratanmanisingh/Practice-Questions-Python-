def replace(s):
    vowels = "AEIOUaeiou"
    d = {"A":1,"a":1,"E":5,"e":5,"I":9,"i":9,"O":15,"o":15,"U":21,"u":21}
    result = ""
    for ch in s:
        if ch in d:
            result += str(d[ch])
        else:
            result += ch
    return result
print(replace("Then is not Possible"))
print(replace("tehe is oue sonus qiioe uvnmouz eooiox"))