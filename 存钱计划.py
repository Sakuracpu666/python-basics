余额=0
month=0
while 余额<8000:
    month+=1
    if month==6:
        print('第6个月不存钱')
        continue
    else:
        余额+=1000
    if 余额>=8000:
        print(f'第{month}个月存够了，余额：{余额}元')
        print(f'总共用了{month}个月')
        break