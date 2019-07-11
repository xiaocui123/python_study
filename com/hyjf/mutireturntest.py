def profile():
    name='zhangsan'
    age=99
    return name,age

if __name__ == '__main__':
    name,age=profile()
    print("name = "+name +' age= '+str(age))