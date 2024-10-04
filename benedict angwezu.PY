class registration:
    def __init__(self,name,reg_no,course,year):
        self.name=name
        self.reg_no=reg_no
        self.course=course
        self.year=year

    def __str__(self):
        return(f"name:{self.name} reg_no:{self.reg_no} course:{self.course} year:{self.year}")

student1=registration("BENEDICT ANGWEZU","S23B13/115","Bsit","2024")
print(student1)    

student1=registration("IMANI DOMADO PETER","S23B14/200","Dit","2024")
print(student1) 

student1=registration("FOADEBN KATONGOLE","S23B13/023","BHD","2024")
print(student1)    

student1=registration("SODEAL MAHARAK","S23B13/197","Bscs","2024")
print(student1)    
       
        