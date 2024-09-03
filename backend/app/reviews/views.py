from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    
    if request.method == 'POST' and 'add' in request.POST:
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    return render(request, 'review_list.html', {'reviews': reviews, 'form': form})


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return redirect('review_list')

def confirm_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'confirm_delete.html', {'review': review})

