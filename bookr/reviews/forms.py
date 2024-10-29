from django import forms
from .models import Publisher, Review  # Import model Publisher và Review từ models.py

# Tạo form cho model Publisher
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher  # Sử dụng model Publisher
        fields = ['name', 'website', 'email']  # Sử dụng các trường cần thiết

# Tạo form cho model Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['date_edited', 'book']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5}),
        }
# Tạo form tìm kiếm
class SearchForm(forms.Form):
    SEARCH_IN_CHOICES = [
        ('title', 'Title'),
        ('contributor', 'Contributor'),
    ]
    search = forms.CharField(
        required=False,
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'Search...'})
    )
    search_in = forms.ChoiceField(
        choices=SEARCH_IN_CHOICES,
        required=True,
        initial='title'
    )
