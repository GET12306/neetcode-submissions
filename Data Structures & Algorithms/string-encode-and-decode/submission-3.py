class Solution:
    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for l_str in strs:
            output_str += str(len(l_str)).zfill(3)
            output_str += l_str
        return output_str

    def decode(self, s: str) -> List[str]:
        pos = 0
        output_list = []
        is_len = True
        str_length: int = 0
        while pos < len(s):
            if is_len:
                str_length = int(s[pos : pos + 3])
                if str_length == 0:
                    output_list.append("")
                    pos += 3
                else:
                    pos += 3
                    is_len = False
            else:
                output_list.append(s[pos : pos + str_length])
                pos += str_length
                is_len = True

        return output_list
