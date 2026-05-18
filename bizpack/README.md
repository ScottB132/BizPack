# BizPack 🧳

AI-powered business travel packing app built with Django + Claude.

## Setup

### 1. Install dependencies
```bash
pip install django anthropic
```

### 2. Create a Virtual Environment

**macOS / Linux:**
```bash
python3.12 -m venv venv
source venv/bin/activate


### 3. Run migrations
bash
python3 manage.py createsuperuser

```
```bash
python3 manage.py migrate
```

### 4. Start the server
```bash
python3 manage.py runserver


Visit http://127.0.0.1:8000 in your browser.

---

## How it works

1. Click **New Trip**
2. Enter your destination, dates, climate and meeting type
3. Hit **Generate Packing List** — Claude builds a categorised list tailored to your trip
4. Tick items off as you pack
5. Add custom items anytime

---

## Project Structure

```
bizpack/
├── bizpack/          # Django project settings + URLs
├── trips/            # Trip model, views, forms, URLs
│   ├── models.py     # Trip model
│   ├── views.py      # CRUD views + Claude integration
│   ├── forms.py      # TripForm
│   └── urls.py
├── packing/          # Packing items
│   ├── models.py     # PackingCategory + PackingItem
│   ├── views.py      # Toggle, add, delete item endpoints
│   ├── claude_service.py  # Claude API call → JSON packing list
│   └── urls.py
├── templates/
│   ├── base.html
│   └── trips/
│       ├── trip_list.html
│       ├── trip_form.html
│       ├── trip_detail.html
│       └── trip_confirm_delete.html
└── db.sqlite3        # Created automatically on first migrate
```

---

## Extending the app (ideas)

- Add user accounts so multiple travellers can have their own trips
- Add a "duplicate trip" button for repeat destinations
- Export the packing list to PDF
- Add airline carry-on rules per destination
- Deploy to Railway or Render (free tier)
