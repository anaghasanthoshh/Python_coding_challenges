#Create classes Employee and Manager. The Manager class should
# inherit from both Employee and a new class Leader.
# Implement methods to demonstrate how multiple inheritance works.

class Employee :
    def __init__(self,fname,lname,EmpId,IsManager,**kwargs):#added **kwargs
        self.fname=fname
        self.lname=lname
        self.EmpId=EmpId
        self.IsManager=IsManager
        self.Totaleaves=12
        super().__init__(**kwargs)#added **kwargs,calls the next class in MRO
        print(IsManager)

    def EmpDetails(self):
        return f'Name is{self.fname+self.lname} and EmpId is {self.EmpId}'

class Leader:
    def __init__(self,rating,**kwargs):#added **kwargs
        self.rating=rating
        if self.rating>3.5 :
            self.feedback='Good Job'
        else :
            self.feedback='Needs Improvement'
        super().__init__(**kwargs)#added **kwargs,calls the next class in MRO

    def LeaderFeedback(self):
        return f'Has a rating of {self.rating} and feed back is {self.feedback}'

class Manager(Employee,Leader):
    def __init__(self,fname,lname,EmpId,IsManager,rating):
        #**Employee.__init__(self,fname,lname,EmpId,IsManager)
        super().__init__(fname=fname, lname=lname, EmpId=EmpId, IsManager=IsManager,rating=rating)
        #**Leader.__init__(self,rating)
        if self.IsManager==True :
            self.projects=['A','B','C']
            self.Reporting_Teams=2

    def CompleteReport(self):
        Nameanddetails=f'{self.fname} is a manager and has {self.Reporting_Teams}teams'
        Projects=f'They are handling  {self.projects} projects.'



manager=Manager('Anu','Santhosh','123',True,4)
print(manager.LeaderFeedback())
print(manager.EmpDetails())


#***Here we have initially used the Class names to call each of parent class init function but it is
# less adviced to do so.Hence ,lets try with super()
"""
.	Use of **kwargs:
	•	The **kwargs is used to allow passing any extra keyword arguments to the next class in the
	    MRO. This is essential for making super() work correctly in multiple inheritance.
	2.	Calling super().__init__(**kwargs):
	•	In each class, after handling its own parameters, super().__init__(**kwargs) 
	is called to pass the remaining arguments down the chain. 
	This ensures that every class in the MRO gets the parameters it expects.
"""




