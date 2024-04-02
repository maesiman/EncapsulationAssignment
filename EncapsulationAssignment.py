


class Protected:
    # initialize protected and private attributes
    def __init__(self):
        self._protectedFName = "Unknown Fname"
        self.__privateLName = "Unknown Lname"

     # protected function
    def setProtectedFName(self, protected):
        self._protectedFName = protected
        return self._protectedFName

    # private function
    def setPrivateLName(self, private):
        self.__privateLName = private
        return self.__privateLName

    

    




if __name__ == "__main__":
    obj = Protected()
    fname = obj.setProtectedFName("Ma Elenia")
    print(fname)

    lname = obj.setPrivateLName("Siman")
    print(lname)

    
