from collections import defaultdict
import sqlite3
contact_lst = []


class Contact:
    def __init__(self):
        self.conn=sqlite3.connect('book.db')
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS CONTACT(id INTEGER PRIMARY KEY, name text, number INTEGER, nickname text, email text)")
        self.conn.commit()
    def add(self,name, number, nickname, email):
        self.cur.execute("INSERT INTO contact values(NULL,?,?,?,?)",(name,number,nickname,email))
        self.conn.commit()

    def show_list(self):
        self.cur.execute("SELECT * FROM contact")
        rows=self.cur.fetchall()
        for row in rows:
            print(f"----->Name= {row[1]}, Number= {row[2]}, Nickname= {row[3]}, Email= {row[4]}" )
        print("***********Complete***********")
        
    def search(self, name):
        try:
            self.cur.execute("SELECT * FROM contact where name=?",(name,))
            rows=self.cur.fetchall()
            for row in rows:
                print(f"----->Name= {row[1]}, Number= {row[2]}, Nickname= {row[3]}, Email= {row[4]}" )
            print("***********Complete***********")
            return rows
        except:
            print("----->Data not avaliable!")

    def delete(self, name):
        try:
            self.cur.execute("DELETE FROM contact WHERE name=?",(name,))
            self.conn.commit()
        except:
            print("----->Data not avaliable!")

    def update(self, name):
        update_number = self.search(name)
        print("-------->What you want to update name or number or both")
        option = input()
        if option == "name" or option == "number":
            name_or_number = input(f'-------->Enter {option}') if option == 'name' else int(input(f'-------->Enter {option}'))
            
            self.cur.execute(f"UPDATE contact SET {'name' if option == 'name' else 'number'}=? WHERE id=?",(name_or_number,update_number[0][0]))
            self.conn.commit()
        elif option == "both":
            update_number["name"] = input('-------->Enter update name')
            update_number["number"]= input('-------->Enter update number')
        print("-------->Upadte successfully!")
if __name__ == '__main__':
    while True:
        print("Add new contact press 1")
        print("Search contact press 2")
        print("Delete contact press 3")
        print("List all contact press 4")
        print("Update contact press 5")
        print("Quit press 0")
        try:
            input_opration = int(input())
        except:
            print("-------------->Support only number")
            break
        u1 = Contact()
        if input_opration == 1:
            for j in range(int(input('--->Number of Contact do want to insert?'))):
                name = input('----->Name')
                number = int(input('----->Number'))
                nickname = input('----->Nickname')
                email = input('----->Email')
                u1.add(name, number, nickname, email)
        elif input_opration == 2:
            u1.search(input("--->Enter name that you are looking for"))
        elif input_opration == 3:
            u1.delete(input("--->Enter name that you want to delete"))
            print('----->Delete Successfully!')
        elif input_opration == 4:
            u1.show_list()
        elif input_opration == 5:
            u1.update(input("--->Enter name that you want to update"))
        elif input_opration == 0:
            break
        else:
            print("---------------->Bad input, You can input only one this option")
