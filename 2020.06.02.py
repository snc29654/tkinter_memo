import tkinter
import sqlite3
from contextlib import closing
dbname = '../memo2.db'
root = tkinter.Tk()
def getTextInput():
    result=textExample.get("1.0","end")
    print(result)
textExample=tkinter.Text(root, height=10)
textExample.pack()
textExample.place(x=90, y=40)
btnRead=tkinter.Button(root, height=1, width=10, text="Clear",
                    command=getTextInput)
#検索
def btn_click():
    data_exist =0
    get_data =txt.get()
    match_word = get_data
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        select_sql = 'select * from items where word like '+'"%'+str(match_word)+'%"'
        data=[]
        print (select_sql )
        try:
            for row in c.execute(select_sql):
                data_exist = 1;
                print(row)
                data.append(row)
            conn.commit()
        except:
            print("data not found")
    textExample.delete("1.0",tkinter.END)
    textExample.insert(tkinter.END,data)
    return data_exist
#追加
def btn_click2():
    get_data =txt.get()#キーワードエリアの読み込み
    get_mean =textExample.get('1.0', 'end')#説明エリアの読み込み
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table items (item_id INTEGER PRIMARY KEY,word TEXT,mean TEXT,level INTEGER DEFAULT 0)'''
        try:
            c.execute(create_table)
        except:
            print("database already exist")
        insert_sql = 'insert into items (word, mean, level) values (?,?,?)'
        items = [
        (get_data, get_mean, 0)
        ]
        c.executemany(insert_sql, items )
        conn.commit()
#テキストボックスクリア
def btn_click3():
    textExample.delete("1.0",tkinter.END)
#削除
def btn_click4():
    get_data =txt.get()
    match_word = get_data
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        select_sql = 'delete from items where word = '+'"'+str(match_word)+'"'
        data=[]
        print (select_sql )
        try:
            for row in c.execute(select_sql):
                print(row)
                data.append(row)
            conn.commit()
        except:
            print("data not found")
    textExample.delete("1.0",tkinter.END)
    textExample.insert(tkinter.END,"削除しました")
# ボタン
btn = tkinter.Button(root, text='検索', command=btn_click)
btn.place(x=10, y=80)
btn2 = tkinter.Button(root, text='追加', command=btn_click2)
btn2.place(x=10, y=110)
btn3 = tkinter.Button(root, text='入力フィールドクリア', command=btn_click3)
btn3.place(x=500, y=10)
btn4 = tkinter.Button(root, text='削除', command=btn_click4)
btn4.place(x=10, y=150)
# 画面サイズ
root.geometry('700x200')
# 画面タイトル
root.title('メモデータベース')
# ラベル
lbl = tkinter.Label(text='キーワード')
lbl.place(x=10, y=10)
lbl2 = tkinter.Label(text='説明')
lbl2.place(x=10, y=50)
# テキストボックス
txt = tkinter.Entry(width=20)
txt.place(x=90, y=10)
txt.insert(tkinter.END,"initial")
# 表示
root.mainloop()
