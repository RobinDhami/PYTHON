a = input(" Enter a number:")

try:
    for i in range(1,11):
        print(f"{a}*{i}={int(a)*int(i)}")

except Exception as e:
    print(e)        