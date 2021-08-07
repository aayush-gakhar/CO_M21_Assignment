class memory:
    def __init__(self,code):
        self.MEM = code + ['0000000000000000'] * (256-len(code))

    def load(self, ind):
        return self.MEM[ind]

    def store(self, ind, val):
        if type(val) == int:
            val = conv_to_bin(val)
        self.mem[ind] = val


class cpu:
    def __init__(self):
        self.REG = {'000':'0000000000000000','001':'0000000000000000', '010':'0000000000000000','011':'0000000000000000','100':'0000000000000000', '101':'0000000000000000',
        '110':'0000000000000000','111':'0000000000000000'}
        self.PC=0

    def load(self,reg,val):
        pass

def conv_to_bin(n):
    b = bin(n).replace('0b', '')
    return (8 - len(b)) * '0' + b

def conv_to_dec(b):
    return int(b,2)
