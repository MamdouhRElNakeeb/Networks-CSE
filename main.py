

"""
/**
 * Fininte State Automota(Machine) 
 *      user input ---------> split the input 
 *                                 | 
 *                                 | 
 *                                 | 
                            -------  --------------------------
                           |                                 | 
                           |                                 | 
                           |                                 | 
                     (gen., verify)               (gen.,alter, verify)          
                           |        
                           |        
                           |        
                           |        
          (Generator Class , Utils.verify)
                           |             
                           |             
                           |             
       (Write File with O/p & Message [Corrent, Uncorrect])
**/
"""


from Utils import Utils
from Generator import Generator

# instantiate Utils Class
utils = Utils()


inputLine = input('Your Command Please => ')

splittedInput = inputLine.split('|')
FileName = splittedInput[0].split('<')[1].strip()
inputParamLength = len(splittedInput)

file_name = FileName
if FileName.find('.') == -1:
    file_name = FileName + '.txt'

fileData = open(file_name, 'r')
# Read M Bits & Clean Its Data
mBits = fileData.readline()
mBits = mBits if mBits.find('\n') == -1 else mBits[:-1]

# Read K Bits & Clean Its Data
kBits = fileData.readline()
kBits = kBits if kBits.find('\n') == -1 else kBits[:-1]

# Length == 2 -> Generator & Verfiy
# Case Of Generation & Verification
if inputParamLength == 2:
    gen = Generator(mBits, kBits)
    encodedData = gen.encodeData()
    utils.writeFile('transmitted_msg', encodedData)
    # Verification Part
    utils.verifyMessage(encodedData, kBits)



# Length == 3 -> Generator & Alter & Verify
# Case Of Generation & Alter & Verification
if inputParamLength == 3:
    # get the alter Bit
    alterBit = int(splittedInput[1].strip().split(' ')[1])
    print('2nd Case', alterBit)














