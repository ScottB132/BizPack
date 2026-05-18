from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from .forms import TripForm
from packing.models import PackingCategory, PackingItem
from packing.claude_service import generate_packing_list
import traceback


def trip_list(request):
    trips = Trip.objects.all().order_by('-created_at')
    return render(request, 'trips/trip_list.html', {'trips': trips})


def trip_create(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save()
            try:
                data = generate_packing_list(trip)
                for cat_data in data.get('categories', []):
                    category, _ = PackingCategory.objects.get_or_create(
                        name=cat_data['name'],
                        defaults={'icon': cat_data.get('icon', '📦')}
                    )
                    for item_name in cat_data.get('items', []):
                        PackingItem.objects.create(
                            trip=trip,
                            category=category,
                            name=item_name,
                            ai_generated=True
                        )
            except Exception as e:
                print("=" * 60)
                print("CLAUDE API ERROR:")
                print(traceback.format_exc())
                print("=" * 60)
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = TripForm()
    return render(request, 'trips/trip_form.html', {'form': form})


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    items_by_category = {}
    for item in trip.items.select_related('category').order_by('category__name', 'name'):
        cat = item.category
        if cat not in items_by_category:
            items_by_category[cat] = []
        items_by_category[cat].append(item)

    total = trip.items.count()
    packed = trip.items.filter(packed=True).count()
    progress = int((packed / total) * 100) if total > 0 else 0

    return render(request, 'trips/trip_detail.html', {
        'trip': trip,
        'items_by_category': items_by_category,
        'total': total,
        'packed': packed,
        'progress': progress,
    })


def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trip_list')
    return render(request, 'trips/trip_confirm_delete.html', {'trip': trip})