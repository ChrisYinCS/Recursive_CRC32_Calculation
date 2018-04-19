import binascii
import GUIInterface

def crc32(v):
    """ 
    Generates the crc32 hash of the v. 
    @return: str, the str value for the crc32 of the v 
    """
    return '%0*x' % (8, binascii.crc32(v) & 0xffffffff)     # fixed at 8 characters and need leading zeros


def main(Test_string):
    """
    Input the initial value and calculate the CRC32 value recursively.
    :return: None 
    """
    initial_value = '00340000'    # the initial input is 0x320000
    counter = 1   # calculating times of CRC algorithm
    crc_list = []   # used to store the results of recursive CRC values

    crc = crc32(binascii.a2b_hex(initial_value))
    crc_hex = binascii.a2b_hex(crc)
    crc_list.append(crc_hex)

    print("counter=%s, crc=0x%s" % (counter, crc))

    while counter < 196608:  # the total amount of crc is (0x400000-0x340000)/4
        crc = crc32(binascii.a2b_hex(crc))
        print("counter=%s, crc=0x%s" % (counter, crc))
        counter += 1

        crc_hex = binascii.a2b_hex(crc)
        crc_list.append(crc_hex)

    print "\nFinish calculating!"

    try:
        f = open('G:/Pythontest/MyProject/CRC32/CRCoutput.txt', 'wb')
        f.truncate()  # erase the file
        for i in crc_list:
            f.write(i)
        f.close()
        print "CRC values written to CRCOutput.txt!"    # Here could use the function of getting file name
        print Test_string
    except IOError, e:
        print 'IOError:', e
        print "No \"CRCOutput.txt\" found! Please change the file path in program or create the file in the path!"
    return None


if __name__ == '__main__':
    main()


