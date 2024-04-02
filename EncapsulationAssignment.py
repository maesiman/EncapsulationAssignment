


class Protected:
    def __init__(self):
        self._protectedFName = "Unknown Fname"
        self.__privateLName = "Unknown Lname"

    def setProtectedFName(self, protected):
        self._protectedFName = protected
        return self._protectedFName

    def setPrivateLName(self, private):
        self.__privateLName = private
        return self.__privateLName

    

    




if __name__ == "__main__":
    obj = Protected()
    fname = obj.setProtectedFName("Ma Elenia")
    print(fname)

    lname = obj.setPrivateLName("Siman")
    print(lname)

    
