from collections import deque
from itertools import product
from string import ascii_lowercase, digits

def generate_words(start, length, _chars=ascii_lowercase + digits):
    remainder = length - len(start)
    if remainder < 1:
        yield start
        return
    for letters in product(_chars, repeat=remainder):
        combo = deque(letters + (start,))
        for _ in range(remainder + 1):
            yield ''.join(combo)
            combo.rotate()

def main():
	for word in generate_words('np', 4):
		print word

if __name__ == '__main__':
    main()
	