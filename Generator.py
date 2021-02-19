# imports
import os
import random

# Custom Errors
class Error(Exception):
    "Base Error Class"
    pass

class MissingFilesError(Error):
    """ Error used when a file from Data directory is missing """
    pass

class EmptyDataError(Error):
    """ Raised when the Names dict or the Email Extensions list is empty """
    pass

class NoGeneratedDataError(Error):
    """ Raised when trying to print to a file and there is not data """
    pass

# Generator
class Generator:
    class Record(object):
        """
        Helper class that holds the Data.
        just like Sessions.
        """
        def __init__(self,i,fname,lname,gender,age,email,salary):
            self.id = i
            self.fname = fname
            self.lname = lname
            self.gender = gender
            self.age = age
            self.email = email
            self.salary = salary
        
        def record_template():
            return "id,fname,lname,gender,age,email,salary"
        
        def __str__(self):
            return f"{self.id},{self.fname},{self.lname},{self.gender},{self.age},{self.email},{self.salary}"
    
    class Reader(object):
        """
        A Helper class that provides first , last and family names and email extensions
        using files in Data folder
        """
        def __init__(self):
            """ 
            Init method checks if its ok to proceed or not if yes it will read the data of the files
            then return it to the Generator
            if not it will raise an error
            """
            self.dir = os.listdir('./Data')
            self.filesneeded = ['EmailsExtensions.txt', 'FamilyNames.txt', 'FemaleNames.txt', 'MaleNames.txt']
            self.__proceed = all(['EmailsExtensions.txt' in self.dir,
                                  'FamilyNames.txt' in self.dir,
                                  'FemaleNames.txt' in self.dir,
                                  'MaleNames.txt' in self.dir])
        
        def Read_files(self):
            """
            readfiles method reads the files in the Data directory 
            returns Dict,List
            dict of names Keys ["Male","Female","Family"] & List of email extensions
            """
            try:
                self.NamesDict = {}
                self.EmailExtensions = []
                if self.__proceed:
                    # Reading Email Extensions 
                    with open("Data/EmailsExtensions.txt",'r') as EExtF:
                        self.EmailExtensions = EExtF.read().strip().split("\n")
                    
                    # Reading Male Names, Female Names, Family Names
                    with open("Data/MaleNames.txt",'r') as MaleNF:
                        self.NamesDict["Male"] = MaleNF.read().strip().split("\n")
                    
                    with open("Data/FemaleNames.txt",'r') as FemaleNF:
                        self.NamesDict["Female"] = FemaleNF.read().strip().split("\n")
                    
                    with open("Data/FamilyNames.txt",'r') as FamilyNF:
                        self.NamesDict['Family'] = FamilyNF.read().strip().split("\n")
                    
                    return self.NamesDict,self.EmailExtensions
                else:
                    L = [(name,True) if name in self.dir else (name,False) for name in self.filesneeded]
                    print(L)
                    msg = "Files : "
                    for name,isfound in L:
                        if not isfound:
                            msg+= name + " "
                    msg += "is/are not Found in Data Directory"        
                    raise MissingFilesError
            except MissingFilesError:
                print(msg)
            
    def __init__(self):
        """
        This is a class that Generates Random Dummy Data        
        """
        self.dataReader = self.Reader()
        self.Names,self.Eextensions = self.dataReader.Read_files()
        self.ListofRecords = []
    
    def GenerateData(self,N=5,showRepresentation=False):
        """
        Function to generate the data using random.choice from the random
        library
        """
        for i in range(N):
            Gender = random.choice(['Male','Female'])
            fName = random.choice(self.Names[Gender])
            lName = random.choice(self.Names['Family'])
            email = fName[0:2]+lName+fName[-2:]+random.choice(self.Eextensions)
            age = random.randint(18,60)
            salary = 0
            if age>=18 and age<24:
                salary = random.randint(10000,30000)
            elif age>=24 and age<45:
                salary = random.randint(30000,75000)
            elif age>=45 and age<61:
                salary = random.randint(90000,120001)
            self.ListofRecords.append(Generator.Record(i,fName,lName,Gender,age,email,salary))
            
        if showRepresentation:
            for record in self.ListofRecords:
                print(record)
    
    def PrinttoFile(self):
        if not self.ListofRecords:
            raise NoGeneratedDataError("Please Generate Data Before using printing Methods")
        
        with open("Records.txt",'w') as outfile:
            outfile.write(Generator.Record.record_template()+"\n")
            for record in self.ListofRecords:
                outfile.write(str(record)+"\n")
        
    def Data_Representation(self):
        """ Prints out a representation of Data that have been read """
        if not self.Names or not self.Eextensions:
            raise EmptyDataError
        print("\t------Data Representation-------")
        print("Email Extensions :",",".join(self.Eextensions[:5]))
        print("Male Names :",",".join(self.Names["Male"][:5]))
        print("Female Names :",",".join(self.Names["Female"][:5]))
        print("Family Names :",",".join(self.Names["Family"][:5]))

if __name__=='__main__':
    X = Generator()
    X.GenerateData(100000)
    X.PrinttoFile()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
