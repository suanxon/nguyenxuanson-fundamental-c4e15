code = {
    'ng' : 'Người',
    'stt' : 'status',
    'lm' : 'làm việc'

}
for x in code:
    print(x, end ="    ")
print()
n = input("Enter code?")
if n in code:
    print(code[n])
else:
    m =input("No direction. May co muon them tu moi vao khong (y/n)")
    if m == "y":

        b = input("Enter your translation:")
        code[n] = b
    for x in code:
        print(x, end ="    ")
    print()
