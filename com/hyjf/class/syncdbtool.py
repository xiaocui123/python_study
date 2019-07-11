import mysql.connector

conn=mysql.connector.connect(host = '47.105.134.236',port = '33306',user='tomcat', password='aAR!Q23AUP!ogk$J', database='hyjf_crm')
cursor=conn.cursor()

cursor.execute('SELECT * FROM `oa_users` where user_realname = %s',('常娟',))

record=cursor.fetchall()
print(record[0])


cursor.close()
conn.close


conn_w=mysql.connector.connect(host = '47.105.196.133',port = '3302',user='user_m', password='aAR!Q23AUP!ogk$J', database='hyjf_user')
cursor_w=conn_w.cursor()
cursor_w.execute('INSERT INTO ht_r_oa_users(id, user_login, user_pass, user_realname, user_email, idcard, avatar, '
               'sex, acc_province, acc_city, acc_address, departmentid, positionid, level, temporary, rework, rework_time, '
               'ispart, payroll_try, payroll, entrydate, reference, education, school, specialty, mobile, last_login_ip, '
               'last_login_time, create_time, bank_address, bank_user, bank_num, user_status, age, hyd_name, hyd_id,'
               ' user_type, entry_success_time, leave_success_time, safety_high)'
               ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)',record[0])

print(cursor_w.rowcount)
conn_w.commit()
cursor_w.close()
conn_w.close()

