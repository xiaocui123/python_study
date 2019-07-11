import pandas
from business_calendar import Calendar, MO, TU, WE, TH, FR
from datetime import datetime,time

def calc(df,employee_id):
    myDf=df[df['序号'] == employee_id]

    cal = Calendar()
    # TODO 参数外部配置
    date1 = datetime(2019,6,1)
    date2 = datetime(2019,6,30)

    # 工作日字符串列表
    my_date_key_list=[date_time.strftime('%Y-%m-%d') for date_time in list(cal.range(date1,date2))]

    # 初始化{工作日：打卡记录}字典
    d={k:[] for k in my_date_key_list}
    for date_key in my_date_key_list:
        d[date_key].extend(myDf[myDf['日期'] == date_key]['打卡时间'].tolist())

    # 遍历字典判断
    weidaka_date_list=[]
    shangban_weidaka_date_list=[]
    xiaban_weidaka_date_list=[]

    chidao_count=0
    chidao_date_list=[]

    zaotui_count=0
    zaotui_date_list=[]

    jiaban_count=0
    jiaban_date_list=[]

    shangban_time=time(9,0,0)
    xiaban_time=time(18,0,0)

    jiaban1_time=time(19,30,0)
    jiaban2_time=time(21,30,0)

    for date_key in my_date_key_list:
        if len(d[date_key]) == 0:
            weidaka_date_list.append(date_key)
        elif len(d[date_key]) == 1:
            value=d[date_key][0]
            if shangban_time >= value or (shangban_time < value and value<xiaban_time):
                xiaban_weidaka_date_list.append(date_key)
            elif value>=xiaban_time:
                shangban_weidaka_date_list.append(date_key)

                if value>=jiaban1_time and value<jiaban2_time:
                    jiaban_count+=1
                    jiaban_date_list.append(date_key)
                elif value>=jiaban1_time:
                    jiaban_count+=2
                    jiaban_date_list.append(date_key)
        else:
            starttime=d[date_key][0]
            endtime=d[date_key][-1]

            if starttime>shangban_time:
                chidao_count+=1
                chidao_date_list.append(date_key)
            elif endtime < xiaban_time:
                zaotui_count+=1
                zaotui_date_list.append(date_key)

            if endtime>=jiaban1_time and endtime<jiaban2_time:
                jiaban_count+=1
                jiaban_date_list.append(date_key)
            elif endtime>=jiaban1_time:
                jiaban_count+=2
                jiaban_date_list.append(date_key+'*2')

    print("未打卡：", weidaka_date_list)
    print("上班未打卡：",shangban_weidaka_date_list)
    print("下班未打卡：",xiaban_weidaka_date_list)
    print("迟到次数%s,日期：%s：" %(chidao_count,chidao_date_list))
    print("早退次数%s,日期：%s：" %(zaotui_count,zaotui_date_list))

    print("加班次数%s,日期：%s：" %(jiaban_count,jiaban_date_list))


if __name__ == '__main__':

    df=pandas.read_excel("G:/技术部6月打卡记录.xlsx",sheet_name='Sheet1',skiprows=0)

    employee=df.set_index("序号").to_dict()['姓名']

    print(employee.items())

    for employee_id,employee_name in employee.items():
        print("*"*32,employee_name,'*'*32)
        calc(df,employee_id)













