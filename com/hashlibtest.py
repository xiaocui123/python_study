import hashlib

db= {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    passwordmd5=md5.hexdigest()
    print(passwordmd5)
    print("password %s value %s" %(password,passwordmd5))
    for key,values in  db.items():
        if key == user:
            print (key,values)
            if values == passwordmd5:
                return True
            else:
                return False
        else:
            continue
    return False

if __name__ == '__main__':
    print(login('michael', '123456'))
    print(login('bob', 'abc999'))
    print(login('alice', 'alice2008'))
    print(login('michael', '1234567'))
    print(login('bobassert', '123456'))
    print(login('alice', 'Alice2008'))
