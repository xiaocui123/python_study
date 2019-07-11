# s="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s='map'

new_s=''
for ch in s:
    if ch>'a' and ch<='x':
        ch=chr(ord(ch)+2)
    elif ch == 'y':
        ch='a'
    elif ch =='z':
        ch='b'
    new_s+=ch
# print(new_s)


from string import ascii_lowercase

transTab=str.maketrans(ascii_lowercase,ascii_lowercase[2:]+ascii_lowercase[:2])

print(s.translate(transTab))