class Solution:

    def encode(self, strs):
        # Encode each string as: <length>#<string>
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            # Find the position of the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # Extract the string of that length
            word = s[j+1 : j+1+length]
            res.append(word)
            # Move the pointer to the start of the next encoded part
            i = j + 1 + length

        return res
