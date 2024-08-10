#Topics:Class,Object,Inheritance,private attribute,getter setter

#Challenge: Create a class called Book that has three attributes: title, author,
# and year_published
# . Then create an instance of the class and print out the attributes.
#challenge 2
#Extend the Book class to include a method called description that returns a string
# describing the book.
#challenge 3
#Modify the EBook class to make the file_size attribute private.
# Add getter and setter methods to access and modify the file_size.
#here we have use @property to declare the getter and setter for the attributes

class Book :
   # title='title of the Book'
   # author='author of the book'
    #year_published='year published'
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year

    #challenge2
    def description(self):
        return f'{self.title} is the name,{self.author} wrote it and {self.year} is the year'





book = Book('My Life','Anu','1994')
print(book.title,book.author,book.year)
print(book.description())


#Challenge: Create a subclass called EBook that inherits from the Book class and adds an attribute
# for file size in MB. Override the description method to include the file size.

#Ebook(Book) is the way to inherit from a class
class Ebook(Book):
    def __init__(self, title, author, year, filesize):
        #need to initialise the superclass attributes aswell
        super().__init__(title, author, year)
        #remaining attribute is initiated separately.The underscores make it a private attribute
        self.__filesize=filesize

#this is the getter method for the attribute filesize
    @property
    def filesize(self):
        return self.__filesize
    @filesize.setter
    def filesize(self,value):
        if value>0 :
         self.__filesize=value
        else:
          print('invalid size')



    def description(self):
         return (f'{self.title} is the name,{self.author} wrote it and'
                       f' {self.year} is the year  and size is {self.filesize}')

ebook=Ebook('A','B','2000',12)
print(ebook.description())
print(ebook.filesize)
ebook.filesize=0
print(ebook.filesize)


