from Utils import Utils

utils = Utils()

class Generator:

    def __init__(self, msg , divisor):
        self.msg = msg
        self.divisor = divisor
    

    """
        Getters
    """
    def divisor(self):
        return self.divisor
    
    def msg(self):
        return self.msg

    """
        Setters
    """
    def setDivisor(self, divisor):
        self.divisor = divisor

    def setMsg(self, msg):
        self.msg = msg


    def encodeData(self):
        l_key = len(self.divisor) 
    
        # Appends n-1 zeroes at end of data 
        appended_data = self.msg + '0'*(l_key-1) 
        # Cyclic Redundancy Check & Verification
        remainder = utils.mod2div(appended_data, self.divisor)
        codeword = self.msg + remainder 
        return codeword    




