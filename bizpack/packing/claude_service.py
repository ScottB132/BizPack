def generate_packing_list(trip):
    """
    Generates a business travel packing list based on trip details.
    No API required — uses rule-based logic.
    """
    nights = trip.duration_nights
    climate = trip.climate
    meeting = trip.meeting_type

    # Scale clothing to trip length
    shirts = max(2, nights + 1)
    suits = 1 if nights <= 2 else 2
    casual_trousers = 1 if nights <= 2 else 2

    clothing = [
        f"{suits} suit{'s' if suits > 1 else ''}",
        f"{shirts} dress shirts",
        "Tie(s)",
        "Dress shoes",
        f"{casual_trousers} casual trouser{'s' if casual_trousers > 1 else ''}",
        "Belt",
        f"{nights} pairs of socks",
        f"{nights} sets of underwear",
    ]

    if climate == 'cold':
        clothing += ["Wool overcoat", "Scarf", "Gloves", "Thermal underlayer"]
    elif climate == 'hot':
        clothing += ["Light breathable shirts", "Sunglasses"]
    elif climate == 'warm':
        clothing += ["Light jacket"]
    else:
        clothing += ["Versatile mid-layer jacket"]

    if meeting in ('conference', 'mixed'):
        clothing.append("Smart casual outfit for networking evening")

    tech = [
        "Laptop",
        "Laptop charger",
        "Phone charger",
        "Universal travel adapter",
        "Portable power bank",
        "Headphones / earbuds",
        "USB-C / Lightning cable",
    ]

    if nights > 3:
        tech.append("Laptop bag / sleeve")

    documents = [
        "Passport",
        "Flight / train booking confirmations",
        "Hotel confirmation",
        "Travel insurance details",
        "Business cards",
        "Company ID / access pass",
    ]

    if meeting in ('client', 'mixed'):
        documents.append("Printed agenda / presentation notes")

    toiletries = [
        "Toothbrush & toothpaste",
        "Deodorant",
        "Shampoo (travel size)",
        "Razor & shaving foam",
        "Moisturiser (travel size)",
        "Lip balm",
    ]

    if nights > 4:
        toiletries.append("Full size toiletries (check-in bag)")

    expenses = [
        "Company credit card",
        "Personal card (backup)",
        "Cash in local currency",
        "Expense receipt folder / app",
        "VAT receipts envelope",
    ]

    health = [
        "Any prescription medication",
        "Paracetamol / ibuprofen",
        "Hand sanitiser",
        "Plasters",
    ]

    if nights > 2:
        health.append("Eye mask & earplugs")
    if climate == 'hot':
        health.append("Sun cream (travel size)")

    return {
        "categories": [
            {"name": "Clothing", "icon": "👔", "items": clothing},
            {"name": "Tech & Adapters", "icon": "💻", "items": tech},
            {"name": "Documents", "icon": "📄", "items": documents},
            {"name": "Toiletries", "icon": "🧴", "items": toiletries},
            {"name": "Expenses & Finance", "icon": "💳", "items": expenses},
            {"name": "Health & Comfort", "icon": "💊", "items": health},
        ]
    }
