class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def calc_cover(self, A, B, C, D):
        ms, mx = min(A, B, C, D), max(A, B, C, D)
        if ms == A:
            if mx == B:
                return D-C
            elif C < B:
                return B-C
            else:
                return 0
        else:
            if mx == D:
                return B-A
            elif A < D:
                return D - A
            else:
                return 0
    
    def calc_area(self, A, B, C, D):
        return (C-A)*(D-B)
    
    def computeArea(self, A, B, C, D, E, F, G, H):
        return self.calc_area(A, B, C, D) + self.calc_area(E, F, G, H) - self.calc_cover(A,C,E,G)*self.calc_cover(B,D,F,H)
        