from app.book import Book


class Ebook(Book):
    def __init__(self,title,author,isbn,file_size_mb,format_type):
        super().__init__(title,author,isbn)
        self._file_size_mb = file_size_mb
        self._format_type = format_type

    @property
    #the above line is used to get the value in protected (_varible_name) variable(getter) so this prevent modifying the value in that variable or remove direct access
    def file_size_mb(self):
        return self._file_size_mb

    @property
    def format_type(self):
        return self._format_type

    def download(self):
        if self._is_checked_out:
            print(f"Downloading '{self._title}' ({self._format_type}, {self._file_size_mb}MB)...")
            print("Download complete!")
        else:
            print("Cannot download - book is not checked out")

    def display_info(self):
        super().display_info()
        print(f"File Size: {self._file_size_mb}MB")
        print(f"Format: {self._format_type}")
