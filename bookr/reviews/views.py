from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Book, Contributor, Publisher, Review
from .forms import PublisherForm, SearchForm, ReviewForm  # Import ReviewForm
from .utils import average_rating

def index(request):
    return render(request, "base.html")

def book_search(request):
    form = SearchForm(request.GET)
    search_text = ''
    books = []

    if form.is_valid():
        search_text = form.cleaned_data.get('search', '')
        search_in = form.cleaned_data.get('search_in', 'title')

        if search_in == 'title' and search_text:
            books = Book.objects.filter(title__icontains=search_text)
        elif search_in == 'contributor' and search_text:
            contributors = Contributor.objects.filter(
                first_names__icontains=search_text) | Contributor.objects.filter(last_names__icontains=search_text)
            books = Book.objects.filter(contributors__in=contributors).distinct()

    return render(
        request,
        'search_results.html',
        {'form': form, 'search_text': search_text, 'books': books}
    )

def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book, 'book_rating': book_rating, 'number_of_reviews': number_of_reviews})
    context = {'book_list': book_list}
    return render(request, 'reviews/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def publisher_edit(request, pk=None):
    if pk:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            publisher = form.save()
            messages.success(request, f'Publisher {"updated" if pk else "created"} successfully.')
            return redirect("publisher_detail", pk=publisher.pk) # Redirect sau khi cập nhật
            #messages.success(request, f'Publisher {"updated" if pk else "created"} successfully.')
            #return redirect('publisher_detail', pk=publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    context = {
        'form': form,
        'instance': publisher,
        'model_type': 'Publisher'
    }
    return render(
        request,
        'reviews/instance-form.html', context)



def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)
    if review_pk:
        review = get_object_or_404(Review, pk=review_pk, book=book)
    else:
        review = None

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            if review_pk:
                review.date_edited = timezone.now()
            review.save()
            messages.success(request, f'Review for {book.title} created')
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'instance': review,
        'model_type': 'Review',
        'related_model_type': 'Book',
        'related_instance': book,
    }
    return render(request, 'reviews/instance-form.html', context)
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'reviews/publisher_detail.html', {'publisher': publisher})
