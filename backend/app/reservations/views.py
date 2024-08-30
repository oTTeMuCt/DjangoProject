
from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation


PRICE_PER_PERSON = 50.00

def book_table(request):
    success_message = None  

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.total_price = reservation.num_people * PRICE_PER_PERSON
            reservation.save()

            next_action = request.POST.get('next_action')

            if next_action == 'success':
                success_message = "Ваше бронирование успешно подтверждено!"
            elif next_action == 'cancel':
                success_message = "Бронирование отменено."

    else:
        form = ReservationForm()

    return render(request, 'book_table.html', {
        'form': form,
        'price_per_person': PRICE_PER_PERSON,
        'success_message': success_message  
    })
