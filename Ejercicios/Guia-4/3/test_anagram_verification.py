from anagram_verification import AnagramVerifier

class TestAnagramVerifier:
    def test_is_anagram(self):
        verifier = AnagramVerifier()

        assert verifier.is_anagram("listen", "silent") == True
        assert verifier.is_anagram("hello", "world") == False
        assert verifier.is_anagram("rail safety", "fairy tales") == True

TestAnagramVerifier().test_is_anagram()
