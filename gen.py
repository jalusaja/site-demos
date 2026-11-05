import os
T=open('/dev/stdin').read() if False else None
def page(d):
    svc="".join(f'<div class="card"><div class="ic">{i}</div><h3>{n}</h3><p>{t}</p></div>' for i,n,t in d['services'])
    area="".join(f"<li>{a}</li>" for a in d['areas'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="preload" as="image" href="hero.webp"><title>{d['title']}</title><meta name="description" content="{d['desc']}"><meta name="robots" content="noindex">
<meta property="og:title" content="{d['title']}"><meta property="og:description" content="{d['desc']}"><meta property="og:type" content="website">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HouseCleaningService","name":"{d['name']}","telephone":"{d['tel']}","email":"{d['email']}","areaServed":{d['areas']!r}}}</script>
<style>:root{{--c:{d['color']};--d:#12263a}}*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--d);line-height:1.55}}
.demo{{background:#fff4c2;color:#5a4700;text-align:center;font-size:13px;padding:6px}}header{{display:flex;justify-content:space-between;align-items:center;padding:14px 5%;position:sticky;top:0;background:#fff;box-shadow:0 1px 6px #0001;z-index:9}}
.logo{{font-weight:800;font-size:20px;color:var(--c)}}.btn{{background:var(--c);color:#fff;padding:12px 20px;border-radius:999px;text-decoration:none;font-weight:700;display:inline-block;border:0;font-size:16px;cursor:pointer}}
.hero{{background:linear-gradient(90deg,rgba(11,31,51,.88),rgba(11,31,51,.55) 60%,rgba(11,31,51,.25)),url(hero.webp) center/cover no-repeat,var(--c);color:#fff;padding:70px 5% 80px}}.hero h1{{font-size:clamp(30px,6vw,52px);margin:0 0 12px;max-width:760px}}.hero p{{font-size:18px;max-width:600px;opacity:.92}}
.hero .btn{{background:#fff;color:var(--c);margin:8px 8px 0 0}}.hero .ghost{{background:transparent;border:2px solid #fff;color:#fff}}
section{{padding:56px 5%}}h2{{font-size:30px;margin:0 0 20px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}}.card{{background:#f4f8fb;border-radius:14px;padding:22px}}.ic{{font-size:30px}}.card h3{{margin:8px 0}}
.split{{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:center;margin-top:28px}}.split img{{width:100%;height:auto;border-radius:14px;display:block}}@media(max-width:700px){{.split{{grid-template-columns:1fr}}}}.area{{background:#f4f8fb}}.area ul{{columns:2;font-size:17px}}form{{display:grid;gap:12px;max-width:560px}}input,select,textarea{{padding:12px;border:1px solid #c8d3dd;border-radius:10px;font:inherit}}
.ph{{background:#ffe9e9;color:#9b1c1c;padding:2px 6px;border-radius:4px;font-size:13px}}footer{{background:var(--d);color:#cfd8e3;padding:30px 5%;font-size:14px}}footer a{{color:#fff}}</style></head><body>
<div class="demo">Demo preview prepared for {d['name']} — not the official website.</div>
<header><span class="logo">{d['name']}</span><a class="btn" href="tel:{d['telraw']}">Call {d['tel']}</a></header>
<div class="hero" role="img" aria-label="{d['heroalt']}"><h1>{d['h1']}</h1><p>{d['sub']}</p><a class="btn" href="#quote">Get a Free Quote</a><a class="btn ghost" href="tel:{d['telraw']}">Call {d['tel']}</a></div>
<section id="services"><h2>Our Services</h2><div class="grid">{svc}</div><div class="split"><img src="cleaner.webp" alt="{d['alt']}" width="900" height="675" loading="lazy" decoding="async"><p style="font-size:18px">{d['pitch']}</p></div></section>
<section class="area" id="area"><h2>Service Area</h2><ul>{area}</ul>{d.get('extra','')}</section>
<section id="quote"><h2>Request a Free Quote</h2><form action="mailto:{d['email']}" method="post" enctype="text/plain">
<input name="Name" placeholder="Your name" required><input name="Phone" type="tel" placeholder="Phone"><input name="Address" placeholder="Address / ZIP">
<select name="Service">{''.join(f"<option>{n}</option>" for _,n,_ in d['services'])}</select><textarea name="Details" rows="4" placeholder="Home size, preferred date, anything we should know"></textarea>
<button class="btn">Send Request</button><small>Opens your email app. <span class="ph">Placeholder: live form (e.g. Formspree) to be connected</span></small></form></section>
<footer><b>{d['name']}</b><br>{d['foot']}<br>Phone: <a href="tel:{d['telraw']}">{d['tel']}</a> · Email: <a href="mailto:{d['email']}">{d['email']}</a><br><br>© 2026 {d['name']}<br><small style="opacity:.7">Illustrative images (AI-generated); not photos of actual work.</small></footer></body></html>'''
F=dict(name="Frame's Cleaning Crew",title="Frame's Cleaning Crew | House Cleaning in Huntington & SW Fort Wayne, IN",
desc="Home, window, commercial and move-in/move-out cleaning in Huntington County and Southwest Fort Wayne, IN. Evenings & weekends available. Call (260) 224-8685.",
tel="(260) 224-8685",telraw="+12602248685",email="framescleaningcrew@gmail.com",color="#1d7f8c",
h1="Give Your Home Some Shine",sub="Residential and commercial cleaning serving Huntington County and Southwest Fort Wayne. Evenings and weekends available.",
services=[("🏠","Home Cleaning","Regular and one-time cleaning for houses and apartments."),("🪟","Window Washing","Streak-free windows inside and out."),("🏢","Commercial Cleaning","Offices and small business spaces."),("📦","Move-In / Move-Out","Get a deposit-ready or move-in-ready home.")],
areas=["Huntington, IN","Huntington County","Southwest Fort Wayne, IN"],
extra="<p><b>Hours:</b> Mon–Fri 8am–8pm · Sat 9am–7pm</p><p>Environmentally friendly cleaning · Satisfaction guaranteed · Evenings &amp; weekends</p>",
heroalt="Bright, freshly cleaned living room with large windows",alt="Cleaner washing a large window with a squeegee, bucket and spray bottles nearby",pitch="From streak-free windows to deep-cleaned floors, our crew leaves every room fresh, bright and ready to enjoy.",foot="10 Nicole Lane, Huntington, IN 46750")
K=dict(name="Klean Freaks Cleaning LLC",title="Klean Freaks Cleaning LLC | House Cleaning in Fort Wayne, IN",
desc="Klean Freaks Cleaning LLC offers house cleaning in Fort Wayne, Indiana. Request a free quote or call (260) 205-7654.",
tel="(260) 205-7654",telraw="+12602057654",email="kleanfreakscompanyllc@gmail.com",color="#6b3fd1",
h1="A Cleaner Home in Fort Wayne",sub="Local house cleaning by Klean Freaks Cleaning LLC. Tell us about your home and get a free quote.",
services=[("🧽","Standard House Cleaning","Kitchens, bathrooms, dusting, floors."),("✨","Deep Cleaning","A top-to-bottom refresh."),("📦","Move-In / Move-Out","Empty-home cleaning.")],
areas=["Fort Wayne, IN","<span class='ph'>Placeholder: confirm nearby towns served</span>"],
extra="<p><span class='ph'>Placeholder: service list, hours, photos and reviews to be confirmed with owner</span></p>",
heroalt="Sparkling clean white kitchen with marble countertops",alt="Gloved hands carrying a caddy of cleaning supplies and microfiber cloths",pitch="We bring the supplies, the checklist and the elbow grease, so you come home to a kitchen and bathroom that truly sparkle.",foot="Fort Wayne, Indiana")
S=dict(name="Sharons Crystal Touch LLC",title="Sharons Crystal Touch LLC | House Cleaning in Fort Wayne, IN",
desc="Thorough, pet-friendly house cleaning, deep refreshes, rental turnovers and move-in/move-out cleaning in Fort Wayne, IN. Call (260) 450-9581.",
tel="(260) 450-9581",telraw="+12604509581",email="sharonscrystaltouch@gmail.com",color="#7b3fa0",
h1="Cleaner, Calmer Spaces in Fort Wayne",sub="Thorough house cleaning from Sharons Crystal Touch LLC. Pet-friendly, dependable and detail-focused.",
services=[("🏠","House Cleaning","Thorough cleaning for your home."),("✨","Deep Refresh","A detailed top-to-bottom clean."),("🔑","Rental Turnovers","Get your rental guest-ready between stays."),("📦","Move-In / Move-Out","Empty-home cleaning before or after a move.")],
areas=["Fort Wayne, IN","<span class='ph'>Placeholder: confirm nearby towns served</span>"],
extra="<p><b>Hours:</b> Mon–Fri 9am–5pm · Sat–Sun closed</p><p>Pet-friendly · Dependable · Detail-focused</p>",
heroalt="Bright, freshly cleaned living room with lavender accents",alt="Gloved hands polishing a bathroom mirror and faucet while a dog rests nearby",pitch="Pet-friendly and detail-focused: we take care of the scrubbing and polishing so you can enjoy a home that feels clean and calm.",foot="Fort Wayne, Indiana")
E=dict(name="Elite Cleaners of Fort Wayne LLC",title="Elite Cleaners of Fort Wayne LLC | Detailed House Cleaning in Fort Wayne, IN",
desc="Detailed deep house cleaning in Fort Wayne, IN: bi-weekly, monthly, one-time, move-in/move-out, post-construction and commercial. 10% senior discount. Call (260) 310-2101.",
tel="(260) 310-2101",telraw="+12603102101",email="elitecleanersofftw@gmail.com",color="#0f6e5c",
h1="Detailed Cleaning, Every Time",sub="Elite Cleaners of Fort Wayne LLC specializes in deep cleaning for homes in Fort Wayne. No basic cleans, just thorough ones.",
services=[("🔁","Bi-Weekly Cleans","Deep cleans that keep busy homes in great shape."),("📅","Monthly Cleans","Flexible and easy to reschedule."),("✨","One-Time Cleans","No pressure to commit, great for events."),("📦","Move-In / Move-Out","Walls, inside cabinets, closets, fridge and oven."),("🏗️","Post-Construction","Clear the dust after a project."),("🏢","Commercial","Cleaning for business spaces.")],
areas=["Fort Wayne, IN","<span class='ph'>Placeholder: confirm nearby towns served</span>"],
extra="<p><b>10% senior citizen discount.</b> Inside fridge &amp; oven cleaning can be added with advance notice (rate changes apply).</p><p><span class='ph'>Placeholder: hours and customer reviews to be added with owner approval</span></p>",
heroalt="Spotless modern kitchen with a clean, open oven",alt="Gloved hand wiping inside a kitchen cabinet shelf next to a cleaning caddy",pitch="Our cleaners are trained to notice every detail, even the ones you may be missing, so you step into an immaculate home.",foot="Fort Wayne, Indiana")
D=dict(name="It’s Us or Dust",title="It’s Us or Dust | Home & Office Cleaning in Fort Wayne, IN",
desc="One-time, regular, deep, move-in/move-out, post-construction, window and office cleaning in Fort Wayne, IN. Call 260-310-3294.",
tel="260-310-3294",telraw="+12603103294",email="its.us.or.dust@gmail.com",color="#c0562b",
h1="Transform Your Home or Office",sub="We make your home or office spotless so you can enjoy the important things in life. A smaller team you can know and trust.",
services=[("🧹","Regular &amp; Deep Cleaning","Bathrooms, kitchens, living spaces and bedrooms."),("✨","One-Time Cleaning","Special occasions, spring cleaning, after parties."),("📦","Move-In / Move-Out","Ready for the next occupant, or for staging."),("🏗️","Post-Construction","Dust and debris cleared away."),("🪟","Window Cleaning","Sparkling clean windows."),("🏢","Office / Commercial","A clean space for a productive day."),("📝","Customized Plans","A plan built around your home and budget.")],
areas=["Fort Wayne, IN","Surrounding neighborhoods"],
extra="<p>We bring our own supplies and equipment, or use your preferred products on request.</p><p><span class='ph'>Placeholder: hours and reviews to be confirmed with owner</span></p>",
heroalt="Bright, dust-free room with sunlight on clean floors",alt="Gloved hand dusting a bookshelf and window sill, vacuum in background",pitch="After working for larger cleaning companies, we built a smaller business so clients can know and trust the people in their homes.",foot="Fort Wayne, Indiana")
for s,d in (("frames-cleaning-crew",F),("klean-freaks-cleaning",K),("sharons-crystal-touch",S),("elite-cleaners-ftw",E),("its-us-or-dust",D)):
    os.makedirs(s,exist_ok=True);open(f"{s}/index.html","w").write(page(d))
open("index.html","w").write('<!doctype html><meta name=robots content=noindex><title>Site demos</title><p>Demo previews.</p>')
open(".nojekyll","w")
