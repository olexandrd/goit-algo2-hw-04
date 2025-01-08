from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(
                f"Illegal argument for countWordsWithSuffix: pattern = {strings} must be a non-empty list of strings"
            )

        for i, string in enumerate(strings):
            self.put(string, i)

        longest_common_word = strings[0]
        for string in strings[1:]:
            current_prefix = ""
            for i in range(min(len(longest_common_word), len(string))):
                if longest_common_word[i] == string[i]:
                    current_prefix += longest_common_word[i]
                else:
                    break
            longest_common_word = current_prefix
            if not longest_common_word:
                break

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
