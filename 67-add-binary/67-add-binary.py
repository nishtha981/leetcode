class Solution:
    def addBinary(self, a: str, b: str) -> str:
        new=int(a,2)+int(b,2)
        return bin(new).replace("0b", "")