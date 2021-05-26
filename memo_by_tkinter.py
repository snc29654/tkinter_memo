############################################
import datetime
import tkinter

import sqlite3
from contextlib import closing
dbname = 'memo.db'

root = tkinter.Tk()


def getTextInput():
    result=textExample.get("1.0","end")
    print(result)



textExample=tkinter.Text(root, height=30)
textExample.pack()
textExample.place(x=90, y=40)

btnRead=tkinter.Button(root, height=1, width=10, text="Clear", 
                    command=getTextInput)


#検索
def btn_click():

    data_exist =0

    get_data =txt2.get()

    match_word = get_data

    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        select_sql = 'select * from items where mean like '+'"%'+str(match_word)+'%"'

        data=[]
        print (select_sql )
        try:

            for row in c.execute(select_sql):
                data_exist = 1;
                print(row)
                print(type(row))
                text = "-".join(map(str, row))
                #text.replace("\}","\:")
                print(text)
                print(type(text))
                data.append(text)
                text2="".join(map(str, data))
            conn.commit()

        except:

            print("data exception")

    
    textExample.delete("1.0",tkinter.END)

    textExample.insert(tkinter.END,text2)

    return data_exist

#追加
def btn_click2():
    txt.delete(0,tkinter.END)
    now = datetime.datetime.now()
    txt.insert(tkinter.END,now)

    get_data =txt.get()
    get_mean =textExample.get('1.0', 'end')


    #if btn_click() == 0:

    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table items (item_id INTEGER PRIMARY KEY,word TEXT,mean TEXT)'''
        try:
            c.execute(create_table)
        except:
            print("database already exist")

        insert_sql = 'insert into items (word, mean) values (?,?)'
        items = [
        (get_data, get_mean)
        ]
        c.executemany(insert_sql, items )
        conn.commit()
    #else:
    #    print("既に登録済")

    #    textExample.delete("1.0",tkinter.END)

    #    textExample.insert(tkinter.END,"既に登録済")

#テキストボックスクリア
def btn_click3():

    textExample.delete("1.0",tkinter.END)

#削除
def btn_click4():

    get_data =txt.get()

    match_word = get_data


    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        select_sql = 'delete from items where item_id = '+'"'+str(match_word)+'"'

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
btn.place(x=300, y=10)

btn2 = tkinter.Button(root, text='追加', command=btn_click2)
btn2.place(x=10, y=110)

btn3 = tkinter.Button(root, text='入力フィールドクリア', command=btn_click3)
btn3.place(x=500, y=450)

btn4 = tkinter.Button(root, text='削除', command=btn_click4)
btn4.place(x=10, y=150)


# 画面サイズ
root.geometry('700x500')
# 画面タイトル
root.title('メモデータベース')

# ラベル
lbl = tkinter.Label(text='キー')
lbl.place(x=10, y=10)

lbl2 = tkinter.Label(text='メモ')
lbl2.place(x=10, y=50)



# テキストボックス
txt = tkinter.Entry(width=30)
txt.place(x=90, y=10)
txt.insert(tkinter.END,"")

# テキストボックス
txt2 = tkinter.Entry(width=50)
txt2.place(x=350, y=10)
txt2.insert(tkinter.END,"")




# 表示
root.mainloop()