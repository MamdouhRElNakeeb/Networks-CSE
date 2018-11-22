class Utils:

    """
        /*
         * @function: xor(a,b)
         * @desc: Xor Between two operands => [a,b]
         * @param { String } a
         * @param { String } b
         * @return { String } result
         * 
         **/
    """
    def xor(self,a,b):
        # initialize result 
        result = [] 
        # Traverse all bits, if bits are 
        # same, then XOR is 0, else 1 
        for i in range(1, len(b)): 
            if a[i] == b[i]: 
                result.append('0') 
            else: 
                result.append('1') 
    
        return ''.join(result) 
    """
        /*
         * @function: mod2div(a,b)
         * @desc: Modulo 2 Divison between divident & divisor | Used for verification of the message
         * @param { String } divident | A Slice of the Appended Message
         * @param { String } divisor | k Bits
         * @return { String } checkword
         * 
         **/

    """    
    def mod2div(self,divident, divisor): 
        # Number of bits to be XORed at a time. 
        pick = len(divisor) 
    
        # Slicing the divident to appropriate 
        # length for particular step 
        tmp = divident[0 : pick] 
    
        while pick < len(divident): 
    
            if tmp[0] == '1': 
    
                # replace the divident by the result 
                # of XOR and pull 1 bit down 
                tmp = self.xor(divisor, tmp) + divident[pick] 
    
            else:   
                # If leftmost bit is '0' 
                # If the leftmost bit of the dividend (or the 
                # part used in each step) is 0, the step cannot 
                # use the regular divisor; we need to use an 
                # all-0s divisor. 
                tmp = self.xor('0'*pick, tmp) + divident[pick] 
    
            # increment pick to move further 
            pick += 1
    
        # For the last n bits, we have to carry it out 
        # normally as increased value of pick will cause 
        # Index Out of Bounds. 
        if tmp[0] == '1': 
            tmp = self.xor(divisor, tmp) 
        else: 
            tmp = self.xor('0'*pick, tmp) 
    
        checkword = tmp 
        return checkword

    """
        /**
            @function: verifyMessage
            @desc: verify if the message is correct or not by comparing the modMessage(remindar) with 0s as length as divisor
            @param { ClassProp } self
            @param { String } msg
            @param { String } divisor
            @return { Void } -> Prints in console [Correct or not]
        */

    """
    def verifyMessage(self, msg, divisor):
        modMessage = self.mod2div(msg, divisor)
        checker = "0" * (len(divisor) - 1)
        if modMessage == checker:
            print('Congratulations! Message is Correct! :)')
        else:
            print('Oops! Message is worng :(')
    """
        /**
            @function: alterMessage
            @desc: Invert the TargetBit in a given message
            @param { ClassProp } self
            @param { Number } targetBit
            @param { String } msg | EncodedMessage
            @return { String } alteredMessage
        */

        message -> 01100
        targetBit -> 2
        expectedOutput -> 00100
        Steps : 
            message -> 1) Split it to 3 parts
                            - Part 1 : Before the Target Bit
                            - Part 2 : Target Bit
                            - Part 1 : After the Target Bit
                        2) Convert Part 2 to number then Invert Part 2
                        3) Concatenate the Message Again with Part 2 Change

    """
    def alterMessage(self, targetBit, msg):

        # 1) Split Message
        beforeTargetBit = msg[:targetBit - 1]
        targetBit = int(msg[targetBit - 1])
        afterTargetBit = msg[targetBit:]
        # 2) Invert the Bit
        targetBit = targetBit ^ 1

        # 3) Concatenate the Message
        alteredMessage = beforeTargetBit + str(targetBit) + afterTargetBit
        return alteredMessage


    """
        /**
            @function: writeFile
            @desc: Write file in directory with a given data
            @param { ClassProp } self
            @param { String } fileName
            @param { String } data
            @return { Void } Just write the file  
        */

    """
    def writeFile(self,fileName, data):
        file_name = fileName if fileName.find('.') != -1 else fileName + '.txt'
        with open(file_name, 'w') as FD:
            FD.write(data)

