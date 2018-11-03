class Model:
    def __init__(self, data, sensitive_data):
        self.data=data
        self.__sensitive_data=sensitive_data
    def __login(self):
        if self.data.get("username")=="user1" and self.data.get("password")=="pwd1":
            return True
        else:
            return False
    def insert(self):
        if self.__login():
            print "insert query: %s, %s"%(self.data, self.__sensitive_data)
        else:
            print "authentication failed"
    def update(self):
        print "update query: %s"%(self.data, self.__sensitive_data)
    def delete(self):
        print "delete query: %s"%(self.data, self.__sensitive_data)
    def browse(self):
        print "select query: %s"%(self.data, self.__sensitive_data)
    def get(self):
        if self.data.get("role")=="manager":
            return self.data, self.__sensitive_data
        else:
            return self.data
anil=Model(data={"name":"anil","age":23,"role":"manager","username":"user1","password":"pwd1"},
           sensitive_data={"pan":"sdfdsfsd"})
ashok=Model(data={"name":"ashok","age":23,"role":"user","username":"user2","password":"pwd1"},
            sensitive_data={"pan":"sdfdsfsd"})
print anil.__login()
print ashok.insert()