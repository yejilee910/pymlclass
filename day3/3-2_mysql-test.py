import pymysql


conn = pymysql.connect(
    user='root',
    passwd='Choco1004',
    host='localhost',
    db='mysql')

cur = conn.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("Database version : %s " % data)

cur.execute('DROP TABLE items') # 테이블 첫 생성시에는 실행 필요 없음. 테이블 생성 이후 덮어쓸 경우 이 구문이 들어가야 기존 테이블들을 드롭시키고 새로작성 가능 
cur.execute("""
    create table items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
)
""")

data = [('Banana', 300), ('Mango', 640), ('Kiwi', 280), ('Apple', 700)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s, %s)", i)

cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)

