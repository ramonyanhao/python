from sqlserver import con
from sqlserver import remotecon

def localcon():
    cur = con()
    cur.execute('sp_columns Employee')  # sp_columns查看表结构，等于mysql的desc
    for i in cur:
        print(i)
    cur.execute('select * from Employee')
    for i in cur:
        print(i)

def remoteconn():
    remotecur = remotecon()
    remotecur.execute("select * from Employee where EmpName = '延浩'")
    for i in remotecur:
        print(i)

if __name__ == '__main__':
    localcon()
    # remoteconn()

    '''
    sqlserver最好使用事务来提交任务，可以达到回滚的目的，防止误操作造成数据丢失，最后确认没问题再执行commit
    begin tran t1
    use AAI
    go
    select * from Employee where EmpId=1202
    update Employee set ActionFlg=1 where EmpId=1202
    select * from Employee where EmpId=1202
    go
    rollback tran
    go
    commit
    '''