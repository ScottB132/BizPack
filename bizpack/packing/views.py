from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import PackingItem, PackingCategory
from trips.models import Trip
import json


@require_POST
def toggle_item(request, pk):
    item = get_object_or_404(PackingItem, pk=pk)
    item.packed = not item.packed
    item.save()
    return JsonResponse({'packed': item.packed})


@require_POST
def add_item(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    data = json.loads(request.body)
    name = data.get('name', '').strip()
    category_name = data.get('category', 'Other')

    if not name:
        return JsonResponse({'error': 'No item name provided'}, status=400)

    category, _ = PackingCategory.objects.get_or_create(
        name=category_name,
        defaults={'icon': '📦'}
    )
    item = PackingItem.objects.create(
        trip=trip,
        category=category,
        name=name,
        ai_generated=False
    )
    return JsonResponse({
        'id': item.pk,
        'name': item.name,
        'category': category.name,
        'icon': category.icon,
    })


@require_POST
def delete_item(request, pk):
    item = get_object_or_404(PackingItem, pk=pk)
    item.delete()
    return JsonResponse({'success': True})
