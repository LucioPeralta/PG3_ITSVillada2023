class AnagramVerifier:
    def is_anagram(self, word1, word2):
        word1 = word1.replace(" ", "").lower()
        word2 = word2.replace(" ", "").lower()

        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}

        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1

        return freq1 == freq2
