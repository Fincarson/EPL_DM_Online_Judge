Routes = {}
N = int(input())

End = ""
for n in range(N):
    Ca = input()
    Cb = input()
    Routes[Ca] = Cb
    if End == "": End = Ca

resolved = {}

def resolve(key):
    if key in resolved:
        return resolved[key]
    
    if key not in Routes:
        resolved[key] = key
        return key
    
    resolved[key] = resolve(Routes[key])
    return resolved[key]

print(resolve(End))