from pyscript import when
from js import document

#Function that Converts Decimal to Binary 
def float_to_binary(f):
    integer_part = int(f)
    binary_integer_part = bin(integer_part)[2:]
    
    fractional_part = f - int(f)
    binary_fractional_part = ""
    
    while fractional_part != 0:
        fractional_part *= 2
        binary_fractional_part += str(int(fractional_part))
        fractional_part -= int(fractional_part)
    
    binary_number = binary_integer_part + "." + binary_fractional_part
    
    return binary_number

@when("input", "#input-number")
def main(event):
    n = event.target.value
    if n=="": return
    n = float(n)
    display("",target="output",append=False)
    if n<0:
        s = 1
        n = n*(-1)
    
    else: s = 0
    
    a = float_to_binary(n)
    display("Binary Value:",a,target="output")
    
    if 0<float(a)<1:   #if a = 0.00101

        #Single Precision
        ind = a.index('1') #4
        a = float(a)*(10**(ind-1)) #1.01
        a = str(a) #int-->str
        z = a.replace('.','') #101
        man = z[1:24]  #01
        l = 23-int(len(man))  #21
        k = str(10**l).replace('1','') #000...0-21
        man = man + k  #0100...00
        e1 = 127-(ind-1) #127-(4-1)=124
        e1 = bin(e1).replace("0b", "") #124-1111100
        if len(e1) < 8: e1 = '0'+str(e1)

        display("\n\t\t32-bit Single Precision\n",target="output")
        display("  S","   "," E","              ","M",target="output")
        display(42*'_',target="output")
        display('|',s,'|',e1,'|',man,'|',target="output")
        display(42*'_',target="output")

        #Double Precision
        man = z[1:53]
        l = 52-int(len(man))
        k = str(10**l).replace('1','')
        man = man + k
        e1 = 1023-(ind-1)
        e1 = bin(e1).replace("0b", "")
        if len(e1) < 11: e1 = '0'+str(e1)

        document.getElementById("dp-output").textContent = f"{s},{e1},{man}"
        display("\n\t\t64-bit Double Precision\n",target="output")
        display("  S","   ","   E","        \t\t      ","M",target="output")
        display(74*'_',target="output")
        display('|',s,'|',e1,'|',man,'|',target="output")
        display(74*'_',target="output")


    a = float_to_binary(n)
    
    if float(a)>1:  #a = 1.101
    
        #Single Precision
        z = a.replace('.','') #1101  
        man = z[1:24]         #101                   
        l = 23-int(len(man))  #23-3==20
        k = str(10**l).replace('1','') #000...0-20
        man = man + k  #10100...0
        ind = a.index('.')  #2
        e1 = 127+(ind-1) #127+1==128
        e1 = bin(e1).replace("0b", "") #128-10000000
        if len(e1) < 8: e1 = '0'+str(e1)

        display("\n\t\t32-bit Single Precision\n",target="output")
        display("  S","   "," E","              ","M",target="output")
        display(42*'_',target="output")
        display('|',s,'|',e1,'|',man,'|',target="output")
        display(42*'_',target="output")

        #Double Precision
        man = z[1:53]
        l = 52-int(len(man))
        k = str(10**l).replace('1','')
        man = man + k
        ind = a.index('.')
        e1 = 1023+(ind-1)
        e1 = bin(e1).replace("0b", "")
        if len(e1) < 11: e1 = '0'+str(e1)

        display("\n\t\t64-bit Double Precision\n",target="output")
        display("  S"+"   E","        \t\t      ","M",target="output")
        display(74*'_',target="output")
        display('|',s,'|',e1,'|',man,'|',target="output")
        display(74*'_',target="output" )
