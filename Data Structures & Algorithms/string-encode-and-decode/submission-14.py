class Solution:
    DELIMITER = "-}]])"
    def encode(self, strs: List[str]) -> str:
        return self.DELIMITER.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(self.DELIMITER)
