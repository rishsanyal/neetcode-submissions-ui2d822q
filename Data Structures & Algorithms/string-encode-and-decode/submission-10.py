class Solution:
    DELIMITER = "-|-|-"
    def encode(self, strs: List[str]) -> str:
        return self.DELIMITER.join(strs) if strs else ""

    def decode(self, s: str) -> List[str]:
        return s.split(self.DELIMITER) if s else []
