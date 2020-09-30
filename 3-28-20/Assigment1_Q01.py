class book: 
    def __init__(self): 
        self.title="" 
        self.author="" 
    def set_book_details(self,TITLE,AUTHOR): 
            self.title=TITLE 
            self.author=AUTHOR 
class student: 
    def __init__(self): 
        self.name="" 
        self.number_of_books_issued=0
        self.book_list=[]
    def set_student_details(self,NAME):
        self.name=NAME
    def issue_book(self,TITLE,AUTHOR):
        temp=book() 
        temp.set_book_details(TITLE,AUTHOR) 
        self.book_list.append(temp) 
        self.number_of_books_issued+=1 
    def display_books(self): 
        for i in range(len(self.book_list)): 
            print(" Book-",i+1," with title ",self.book_list[i].title," and Author",self.book_list[i].author); 
class library:
    def __init__(self): 
        self.Issues=[] 
    def issue(self,NAME,TITLE,AUTHOR): 
        for i in self.Issues: 
            if(i.name==NAME): 
                i.issue_book(TITLE,AUTHOR) 
                break 
            else: 
                temp=student() 
                temp.set_student_details(NAME) 
                temp.issue_book(TITLE,AUTHOR) 
                self.Issues.append(temp) 
    def display_issues(self):
        j=97; 
        for i in self.Issues: 
            print("(",chr(j),") Student ",i.name," has borrowed ",i.number_of_books_issued ," and the details are as follows:") 
            j+=1 
            i.display_books() 
        
        
lib=library() 
lib.issue("Alia","Python Programming","Jason Rees") 
lib.issue("Alia","Networking","Tanenbaum") 
lib.issue("Ahmad","Database","Korth") 
lib.display_issues()
