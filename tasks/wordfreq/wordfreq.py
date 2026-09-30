import re
from collections import Counter

def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most frequent words in text.
    - Words are maximal runs of [a-z0-9] after lowercasing the text;
      split on anything else.
    - n <= 0 returns [].
    - Ties in frequency are broken by alphabetical order (ascending).
    - Empty text returns [].
    """
    if n <= 0:
        return []

    words = re.findall(r'[a-z0-9]+', text.lower())

    if not words:
        return []

    counter = Counter(words)
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[:n]
