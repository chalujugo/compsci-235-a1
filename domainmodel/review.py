from book import Book


class Review:

    def __init__(self, book, review_text, rating, timestamp=None):
        if not isinstance(book, Book):
            self.__book = None
        else:
            self.__book = book
        if not isinstance(review_text, str) or review_text.strip() == "":
            self.__review_text = "N/A"
        else:
            self.__review_text = review_text.strip()
        if not isinstance(rating, int) or rating < 0 or rating > 5:
            raise ValueError
        else:
            self.__rating = rating

        self.__timestamp = timestamp

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__book == other.__book and self.__review_text == self.__review_text and self.__rating == other.__rating and self.__timestamp == other.__timestamp


book = Book(2675376, "Harry Potter")
review_text = "  This book was very enjoyable.   "
rating = 4
review = Review(book, review_text, rating)

print(review.book)
print("Review: {}".format(review.review_text))
print("Rating: {}".format(review.rating))
