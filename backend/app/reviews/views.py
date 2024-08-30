from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    
    return render(request, 'review_list.html', {'reviews': reviews, 'form': form})
