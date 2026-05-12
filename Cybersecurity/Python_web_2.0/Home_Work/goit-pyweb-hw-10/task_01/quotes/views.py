##quotes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Quote, Tag, Author
from .services import ScraperService
from .forms import AuthorForm, QuoteForm

def get_top_tags():
    """Повертає Топ-10 тегів (DRY)."""
    return Tag.objects.annotate(num_quotes=Count('quotes')).order_by('-num_quotes')[:10]

def quote_list(request, tag_name=None):
    """Головна сторінка з усіма цитатами та пагінацією."""
    quotes = Quote.objects.select_related('author').prefetch_related('tags').all()

    if tag_name:
        quotes = quotes.filter(tags__name=tag_name)

    paginator = Paginator(quotes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'top_tags': get_top_tags(),
        'current_tag': tag_name,
    }
    return render(request, 'quotes/quote_list.html', context)

def author_detail(request, pk):
    """Сторінка деталей автора (Доступна всім)."""
    author = get_object_or_404(Author, pk=pk)
    # Отримуємо всі цитати цього автора для відображення
    quotes = author.quotes.all()
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})

@login_required
def add_author(request):
    """Додавання автора (Тільки для авторизованих)."""
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.added_by = request.user
            author.save()
            messages.success(request, f"Автора {author.fullname} успішно додано!")
            return redirect('quotes:quote_list')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    """Додавання цитати (Тільки для авторизованих)."""
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.added_by = request.user
            quote.save()

            # Обробка тегів (введених через кому)
            tags_str = form.cleaned_data.get('tags_input', '')
            if tags_str:
                tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
                for name in tag_names:
                    tag_obj, _ = Tag.objects.get_or_create(name=name)
                    quote.tags.add(tag_obj)

            messages.success(request, "Цитату успішно додано!")
            return redirect('quotes:quote_list')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

@login_required
def scrape_quotes(request):
    """Ендпоінт для запуску скрапінгу."""
    if request.method == 'POST':
        success, message = ScraperService.scrape_and_save(user=request.user)
        if success:
            messages.success(request, message)
        else:
            messages.error(request, message)
    return redirect('quotes:quote_list')
