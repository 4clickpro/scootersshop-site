import json
import os

with open('../shopify_products.json', 'r') as f:
    data = json.load(f)

products = data.get('products', [])

# Take top 20 products
selected_products = products[:20]

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ScootersShop.net - Top Rated Electric Scooters & eBikes</title>
    <style>
        :root { --primary: #1e293b; --accent: #f59e0b; --bg: #f8fafc; --text: #334155; }
        body { font-family: -apple-system, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 0; }
        header { background: var(--primary); color: white; padding: 20px; text-align: center; border-bottom: 5px solid var(--accent); }
        .hero { text-align: center; padding: 50px 20px; background: linear-gradient(to right, #e2e8f0, #f1f5f9); border-bottom: 1px solid #cbd5e1; }
        .hero h1 { font-size: 3rem; margin: 0 0 10px; color: var(--primary); }
        .hero p { font-size: 1.2rem; color: #475569; max-width: 600px; margin: 0 auto; }
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        
        .ad-banner { background: #fee2e2; border: 2px dashed #ef4444; color: #b91c1c; text-align: center; padding: 30px; margin: 40px 0; border-radius: 8px; font-weight: bold; font-size: 1.2rem; }
        .forum-banner { background: #e0f2fe; border: 2px solid #38bdf8; color: #0284c7; text-align: center; padding: 30px; margin: 40px 0; border-radius: 8px; text-decoration: none; display: block; font-weight: bold; font-size: 1.5rem; transition: transform 0.2s; }
        .forum-banner:hover { transform: scale(1.02); }
        
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .card { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); display: flex; flex-direction: column; }
        .card img { width: 100%; height: 250px; object-fit: cover; border-radius: 5px; margin-bottom: 15px; }
        .card h3 { font-size: 1.2rem; margin: 0 0 10px; color: var(--primary); }
        .btn { display: block; text-align: center; padding: 12px; margin-top: auto; border-radius: 5px; text-decoration: none; font-weight: bold; color: white; }
        .btn-buy { background: var(--accent); margin-bottom: 10px; }
        .btn-buy:hover { background: #d97706; }
        
        footer { background: var(--primary); color: white; text-align: center; padding: 30px 20px; margin-top: 50px; }
    </style>
</head>
<body>
    <header>
        <h1>🛴 ScootersShop.net</h1>
        <p>Your Ultimate Electric Vehicle Destination</p>
    </header>
    
    <div class="hero">
        <h1>Ride the Future Today</h1>
        <p>The hottest electric scooters and e-bikes handpicked for performance and style.</p>
    </div>

    <div class="container">
        <!-- Affiliate Banner Slot 1 -->
        <div class="ad-banner">
            [ Affiliate Ad Slot: 970x250 Banner - Insert ClickBank or ShareASale Offer Here ]
        </div>
        
        <h2>Featured Deals</h2>
        <div class="grid">
"""

for p in selected_products:
    title = p.get('title', 'Unknown Product')
    handle = p.get('handle', '')
    img_src = p.get('images', [{}])[0].get('src', '') if p.get('images') else 'https://via.placeholder.com/300'
    
    html += f"""
            <div class="card">
                <img src="{img_src}" alt="{title}">
                <h3>{title}</h3>
                <a href="https://shop.theelectricbikesuperstore.com/products/{handle}" class="btn btn-buy" target="_blank">Shop Now</a>
            </div>
"""

html += """
        </div>

        <!-- EVForum Redirect Banner -->
        <a href="https://www.evforum.net" class="forum-banner" target="_blank">
            💬 Join the Discussion! Connect with EV Enthusiasts on EVForum.net →
        </a>

        <!-- Affiliate Banner Slot 2 -->
        <div class="ad-banner">
            [ Affiliate Ad Slot: 970x250 Banner - Recommended Accessories / Gear ]
        </div>
    </div>
    
    <footer>
        <p>&copy; 2026 ScootersShop.net. All rights reserved. | <a href="https://www.evforum.net" style="color: #cbd5e1;">Visit our Forum</a></p>
    </footer>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html)

print("Generated index.html")
