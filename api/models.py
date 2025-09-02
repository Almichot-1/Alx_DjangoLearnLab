from django.db import models

# Model to represent an Author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores the author's name

    def __str__(self):
        return self.name

# Model to represent a Book, linked to an Author
class Book(models.Model):
    title = models.CharField(max_length=200)  # Stores the book's title
    publication_year = models.IntegerField()  # Stores the year of publication
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Foreign key to Author

    def __str__(self):
        return self.title