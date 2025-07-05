

def merge(nums1, m, nums2, n):
     
        for i in range(m,n+m):
            nums1.append(nums2[n-i])
        return nums1
    


print(merge([0,3],2,[5,6],2))

'''
class student():
    def __init__(self,name,age,grade):
        self.name=name
        self.grade=grade
        self.age=age

    def display_details(self):
        print({self.name},{self.grade},{self.age})

    def update_grade(self,updated_grade):
        self.grade=updated_grade


student1 = student("Rohan", 21, "A")
student1.display_details()  # Output: Name: Rohan, Age: 21, Grade: A
student1.update_grade("A+")

student1.display_details()

'''


'''
class bankaccount():
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    

    def deposit(self,deposit):
        self.balance=self.balance+deposit
        print(f"Balance: ",self.balance)

    def withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        if (self.balance<0):
           print(f'Insufficient funds')
        else :
           print(f'Balance: ',self.balance)

account1 = bankaccount("12345", 1000)
account1.deposit(500)  # Balance: 1500
account1.withdraw(300) # Balance: 1200
account1.withdraw(2000) # Output: Insufficient funds




class Product():
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def display(self):
         print(f"Product Name: {self.name}, Price: ${self.price}, Stock: {self.stock}")       
    
    def update_stock(self,quantity):
        if (self.stock>quantity):
            self.stock=self.stock-quantity
            return True
        else :
           print("not neough stock")
           return False

class ShoppingCart():
    def __init__(self):
        self.items = {}
    
     
    def display(self):
        for a,p in self.items.items():
            pro=p['product']
            qua=p['quantity']

            print(f"product'{pro},'quan'{qua}")
        
        print(f"Product Name: {self.items}")     


    def add_product(self,Product,quantity):
        if  Product.update_stock(quantity):
            if  Product.name in self.items :
                self.items[Product.name]['quantity']=+quantity
            else :
                self.items[Product.name]={'product':Product ,'quantity':quantity}
        else:
            print("not neough stock")



    
    def calculate_total(self):
        t=0
        for vlues in self.items.values():
            q=vlues['quantity']
            p=vlues['product']
            t+=q*(p.price)
        print(f"Total cost is ${t}")
        return t

         

product1 = Product("Laptop", 1500, 10)


product3=Product("keyboaed", 1500, 10)


cart = ShoppingCart()

cart.add_product(product1, 2) # Add 2 laptops
cart.add_product(product3, 2) # Add 2 laptops
cart.display()
product3.price=3000
Product.display(product1)


cart.calculate_total()  # Output: Total cost is 3000
'''
'''
class book():
        def __init__(self,title,author,is_borrowed,stock):
            self.title=title
            self.author=author
            self.is_borrowed=is_borrowed
            self.stock=stock

class Library():
        def __init__(self):
            self.items = {}
               
        def add_book(self,title,author):
            new_book=book(title,author,1,1)
            if title in self.items.keys():
                if author in self.items[title]:
                    self.items[title]['stock']=+stock
                else:
                    self.items[title]={'author':author,'stock':1,'is_borrowed':0}
            else :
                self.items[title]={'author':author,'stock':1,'is_borrowed':0}
        
        def borrow_book(self,title):
            if title in self.items.keys():
                if self.items[title]['stock']>0:
                    self.items[title]['stock']-=1
                    self.items[title]['is_borrowed']+=1

                    print(f"{title},book borrowed")
                    print(self.items.items())
                else:
                    print("no stock")
            else:
                print("book not available in library")
            
        def return_book(self,title):
            if title in self.items.keys():
                self.items[title]['stock']+=1
                self.items[title]['is_borrowed']-=1
                print(f"{title},Book returned")
                print(self.items.items())


            else:
                print("please input the correct book")

library = Library()
library.add_book("Python Programming", "Author A")
library.add_book("Python Programming", "Author A")
library.borrow_book("Python Programming") # Output: Book borrowed
library.borrow_book("Python Programming") 

library.return_book("Python Programming") # Output: Book returned

'''
               


            


        
     
   

    

        
    


        

    