from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(
                f"Illegal argument for countWordsWithSuffix: pattern = {strings} must be a non-empty list of strings"
            )

        for i, string in enumerate(strings):
            self.put(string, i)

        longest_common_word = ""
        current_preffix = ""
        trie_size = self.size
        # for string in strings: # Dont need to iterate over all strings because finding common prefix, it must be included in all strings
        for i in strings[0]:  # Iterate over the first element
            current_preffix += i
            if len(self.keys_with_prefix(current_preffix)) == trie_size:
                longest_common_word = current_preffix

        return longest_common_word


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
