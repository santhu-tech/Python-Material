class Employee:
    def __init__(self,name,salary,emp_id):
        self.name=name #public variable
        self._salary=salary #protected variable
        self.__emp_id=emp_id #private variable
    @property  #read
    def name(self):
        return self.name
    @name.setter #write
    def name(self,new_name):
        #if () do some validation
        #else
    @property
    def salary(self):
            return self.name
    @salary.setter
        def name(self, new_name):
    # if () do some validation
    # else

@final
