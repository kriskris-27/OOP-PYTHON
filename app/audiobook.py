from app.book import Book


class Audiobook(Book):
    def __init__(self,title,author,isbn,duration_hours, narrator):
        super().__init__(title,author,isbn)
        self._duration_hours = duration_hours
        self._narrator = narrator

    @property
    def duration_hours(self):
        return self._duration_hours

    @property
    def narrator(self):
        return self._narrator

    def play(self):
        if self._is_checked_out:
            print(f"Playing '{self._title}' narrated by {self._narrator}")
            print(f"Duration: {self._duration_hours} hours")
        else:
            print("Cannot play - audiobook is not checked out")

    def display_info(self):
        super().display_info()
        print(f"Duration: {self._duration_hours} hours")
        print(f"Narrator: {self._narrator}")