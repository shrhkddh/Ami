import os, pymysql

target_db_name = 'ami'

sqlusr = 'root'

# 각자 비밀번호 입력
sqlpwd = ''

app = [
    'order'
]

def migrating():

    conn = pymysql.connect(
            host='localhost',
            user= sqlusr,
            password=sqlpwd,
            db=target_db_name,
            charset='utf8mb4'
        )

    curs = conn.cursor()

    curs.execute('drop database '+ target_db_name)
    curs.execute('create database ' + target_db_name + ' character set utf8mb4 collate utf8mb4_general_ci')
    conn.close()

    os.system('find . -path "*/migrations/*.py"')
    os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')

    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')

    return
    

migrating()

os.system('python /Users/nogwang-o/ami/9-WE_T_S-backend/initialize_total_databasenew_db.py')

