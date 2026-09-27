class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r += s + "./=+-"
        return r

    def decode(self, s: str) -> List[str]:
        r = s.split("./=+-")
        return r[:-1]
