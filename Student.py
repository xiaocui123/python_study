#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月9日

@author: lei.wang
'''

def diff(listA,listB):
    #求差集，在A中但不在B中
    retD = list(set(listA).difference(set(listB)))
    print ("我的数据减去他的数据 is: ",retD)
    print("size:",len(retD))

    retE = list(set(listB).difference(set(listA)))
    print ("他的数据减去我的数据 is: ",retE)
    print("size:",len(retE))
def main():

    listMine=[]
    with open('G:/admin.txt', 'r',encoding='gbk') as f:
        for line in f.readlines():
            listMine.append(line)

    listOther=[]
    with open("G:/crm.txt",'r',encoding='gbk') as ff:
        for line1 in ff.readlines():
            listOther.append(line1)

    diff(listMine,listOther)

if __name__ == '__main__':
    main()
