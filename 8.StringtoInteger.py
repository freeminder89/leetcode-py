__author__ = 'amow'
class Solution:
    # @return an integer
    def atoi(self, str):
        if not str:
            return 0
        sim = "+"
        numing = False
        base = 0
        for s in str:
            if s ==" " and not numing:
                continue
            if s in ('+','-') and not numing:
                sim = s
                numing = True
                continue
            numing = True
            if s not in ('0123456789') and numing:
                break
            base *= 10
            base += int(s)
        base = base*int(sim+"1")
        if base > 2147483647:
            return 2147483647
        elif base < -2147483648:
            return -2147483648
        else :
            return base