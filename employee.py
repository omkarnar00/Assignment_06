import json

Employee_details=[{"name":"omkar","DOB":"25-08-2000","Height":"5.8","city":"mumbai","state":"MH"},
                  {"name":"pratik","DOB":"24-08-2000","Height":"5.8","city":"pune","state":"Mh"},
                  {"name":"jid","DOB":"23-08-2000","Height":"5.8","city":"bang","state":"MH"},
                  {"name":"vegita","DOB":"27-08-2000","Height":"5.8","city":"tokyo","state":"MH"},
                  {"name":"goku","DOB":"21-08-2000","Height":"5.8","city":"vakanda","state":"MH"}]

with open("employee.json","w") as file:
    json.dump(Employee_details,file)

with open("employee.json")  as file:
    dict_obj=json.load(file) 
    # for d in dict_obj: 
    #      print(d)

class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name=name
        self.dob=dob
        self.height=height
        self.city=city
        self.state=state         
emp=Employee(dict_obj["name"],dict_obj["DOB"],dict_obj["Height"],dict_obj["city"],dict_obj["state"])

print(emp.city)
