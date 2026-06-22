class Solution:

    def encode(self, strs: List[str]) -> str:
        return "ASHMIT".join(strs) if strs else  "NULLA"

    def decode(self, s: str) -> List[str]:
        return s.split("ASHMIT") if s != "NULLA" else []
