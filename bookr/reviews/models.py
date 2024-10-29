from django.contrib import admin
from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    """A company that publishes books."""
    name = models.CharField(
        max_length=50,
        help_text="The name of the Publisher.")
    website = models.URLField(
        help_text="The Publisher's website.")
    email = models.EmailField(
        help_text="The Publisher's email address.")

    def __str__(self):
        return self.name

class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor, coauthor."""
    first_names = models.CharField(
        max_length=50,
        help_text="The contributor's first name or names.")
    last_names = models.CharField(
        max_length=50,
        help_text="The contributor's last name or names.")
    email = models.EmailField(help_text="The contact email for the contributor.")

    def initialled_name(self):
        initials = ''.join([name[0].upper() for name in self.first_names.split()])
        return f"{self.last_names}, {initials}"

    def __str__(self):
        return self.initialled_name()

class Book(models.Model):
    """A published book."""
    title = models.CharField(
        max_length=70,
        help_text="The title of the book.")
    publication_date = models.DateField(
        verbose_name="Date the book was published.")
    isbn = models.CharField(
        max_length=20,
        verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        Contributor,
        through="BookContributor")

    def __str__(self):
        return "{} ({})".format(self.title, self.isbn)

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE)
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.PROTECT)
    role = models.CharField(
        verbose_name="The role this contributor had in the book.",
        choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(
        null=True, blank=True,
        help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(
        auth.get_user_model(),
        on_delete=models.CASCADE,
        help_text="The user who created the review.")

    def __str__(self):
        return f"Review for {self.book.title} by {self.id}"

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')

    @admin.display(ordering='isbn', description='ISBN-13', empty_value='-/-')
    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4],
                                       obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])

    @admin.display(boolean=True, description='Has ISBN')
    def has_isbn(self, obj):
        """ '9780316769174' => True """
        return bool(obj.isbn)
