def float_to_binary(f):
    integer_part = int(f)
    binary_integer_part = bin(integer_part)[2:]
    
    fractional_part = f - integer_part
    binary_fractional_part = ""
    
    count = 0
    while fractional_part != 0 and count < 52:
        fractional_part *= 2
        binary_fractional_part += str(int(fractional_part))
        fractional_part -= int(fractional_part)
        count += 1
    
    binary_number = binary_integer_part + "." + binary_fractional_part
    return binary_number


n = input("Enter a decimal number: ").strip()
if n == "":
     print("No input given.")
n = float(n)

if n < 0:
    s = 1
    n = -n
else:
    s = 0

a = float_to_binary(n)
print("Binary Value:", a)

if 0 < n < 1:
    # Single Precision
    ind = a.index('1')
    a_scaled = float(a.replace(".", "")) * (10 ** (ind - 1))
    a_str = str(a_scaled)
    z = a_str.replace('.', '')
    man = z[1:24]
    l = 23 - len(man)
    man += '0' * l
    e1 = bin(127 - (ind - 1))[2:].zfill(8)

    print("\n\t\t32-bit Single Precision")
    print("  S   E                M")
    print("_" * 42)
    print(f'|{s}|{e1}|{man}|')
    print("_" * 42)

    # Double Precision
    man = z[1:53]
    l = 52 - len(man)
    man += '0' * l
    e1 = bin(1023 - (ind - 1))[2:].zfill(11)

    print("\n\t\t64-bit Double Precision")
    print("  S     E                             M")
    print("_" * 74)
    print(f'|{s}|{e1}|{man}|')
    print("_" * 74)

elif n >= 1:
    # Single Precision
    ind = a.index('.')
    z = a.replace('.', '')
    man = z[1:24]
    l = 23 - len(man)
    man += '0' * l
    e1 = bin(127 + (ind - 1))[2:].zfill(8)

    print("\n\t\t32-bit Single Precision")
    print("  S   E                M")
    print("_" * 42)
    print(f'|{s}|{e1}|{man}|')
    print("_" * 42)

    # Double Precision
    man = z[1:53]
    l = 52 - len(man)
    man += '0' * l
    e1 = bin(1023 + (ind - 1))[2:].zfill(11)

    print("\n\t\t64-bit Double Precision")
    print("  S     E                             M")
    print("_" * 74)
    print(f'|{s}|{e1}|{man}|')
    print("_" * 74)


