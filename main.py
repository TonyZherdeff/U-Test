class Numbers:
    def __init__(self, plist: list):
        self.plist = plist

    def sum_plist(self):
        return sum(self.plist)

    def avg_plist(self):
        return sum(self.plist) / len(self.plist)

    def max_plist(self):
        return max(self.plist)

    def min_plist(self):
        return min(self.plist)

