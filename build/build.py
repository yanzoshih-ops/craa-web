#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
靜態網站產生器（僅供開發時使用，產出純靜態 HTML，網站上線後不需要 Python）。
用法： python3 build.py
會讀取 pages/*.py 中定義的內容，套用共用 header/footer 樣板，
輸出對應的 .html 檔到專案根目錄。
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_NAME = "中華AI機器人理財協會"
SITE_NAME_EN = "Chinese Robo-Advisor Association"
SITE_URL = "https://www.craa.org.tw"
CONTACT_EMAIL = "craa.tw@gmail.com"
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=100057627691904"

NAV_ITEMS = [
    {"id": "home", "label": "首頁", "href": "index.html"},
    {"id": "activities", "label": "近期活動", "href": "activities.html"},
    {"id": "mission", "label": "協會主要任務", "href": "mission.html"},
    {"id": "about", "label": "關於CRAA", "href": "about.html", "children": [
        {"label": "關於CRAA", "href": "about.html"},
        {"label": "組織架構", "href": "organization.html"},
    ]},
    {"id": "plans", "label": "年度工作計畫", "href": "plan-2024.html", "children": [
        {"label": "2024 年度工作計畫", "href": "plan-2024.html"},
        {"label": "2023 年度工作計畫", "href": "plan-2023.html"},
        {"label": "2022 年度工作計畫", "href": "plan-2022.html"},
        {"label": "2021 年度工作計畫", "href": "plan-2021.html"},
    ]},
    {"id": "resources", "label": "理財補給站", "href": "resources.html"},
    {"id": "reports", "label": "關鍵報告", "href": "reports.html"},
    {"id": "contact", "label": "聯絡我們", "href": "contact.html"},
]

MEMBERSHIP = {"id": "membership", "label": "加入會員", "href": "membership.html"}


def render_nav_desktop(active):
    html = []
    for item in NAV_ITEMS:
        is_active = (item["id"] == active)
        if "children" in item:
            html.append(f'<li class="dropdown{" active" if is_active else ""}">')
            html.append(f'<a href="{item["href"]}">{item["label"]} <span class="caret">▾</span></a>')
            html.append('<div class="dropdown-menu">')
            for c in item["children"]:
                html.append(f'<a href="{c["href"]}">{c["label"]}</a>')
            html.append('</div></li>')
        else:
            html.append(f'<li class="{"active" if is_active else ""}"><a href="{item["href"]}">{item["label"]}</a></li>')
    return "\n".join(html)


def render_nav_mobile(active):
    html = []
    for item in NAV_ITEMS:
        if "children" in item:
            html.append('<li class="has-sub">')
            html.append(f'<a href="#">{item["label"]} <span class="caret">▾</span></a>')
            html.append('<ul class="sub">')
            for c in item["children"]:
                html.append(f'<li><a href="{c["href"]}">{c["label"]}</a></li>')
            html.append('</ul></li>')
        else:
            html.append(f'<li><a href="{item["href"]}">{item["label"]}</a></li>')
    return "\n".join(html)


def page(title, description, active, content, body_class="", filename="index.html"):
    full_title = f"{title} | {SITE_NAME} CRAA" if title != SITE_NAME else f"{SITE_NAME}｜{SITE_NAME_EN} (CRAA)"
    nav_desktop = render_nav_desktop(active)
    nav_mobile = render_nav_mobile(active)
    page_url = f"{SITE_URL}/" if filename == "index.html" else f"{SITE_URL}/{filename}"

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<script>document.documentElement.className += " js";</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="{SITE_URL}/assets/img/logo-color.png">
<link rel="icon" href="assets/img/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="icon" type="image/png" href="assets/img/favicon-192.png" sizes="192x192">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+TC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="{body_class}">

<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand">
      <img src="assets/img/logo-color.png" alt="{SITE_NAME} CRAA Logo">
      <span class="brand-text">{SITE_NAME}<small>{SITE_NAME_EN} · CRAA</small></span>
    </a>
    <nav>
      <ul class="nav-desktop">
{nav_desktop}
      </ul>
    </nav>
    <div class="nav-cta">
      <a href="{MEMBERSHIP['href']}" class="btn btn-primary btn-sm">{MEMBERSHIP['label']}</a>
      <button class="nav-toggle" aria-label="開啟選單" aria-expanded="false">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </div>
</header>

<nav class="nav-mobile">
  <ul>
{nav_mobile}
  </ul>
  <a href="{MEMBERSHIP['href']}" class="btn btn-primary btn-block mobile-cta">{MEMBERSHIP['label']}</a>
</nav>

<main>
{content}
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo-color.png" alt="{SITE_NAME} Logo">
        <p>{SITE_NAME}（{SITE_NAME_EN}，CRAA）致力於推動機器人理財（Robo-Advisor）與 AI 智能理財在台灣的普及與健全發展，結合金融界與科技界人才，促進產官學合作。</p>
        <div class="footer-social">
          <a href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Facebook">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12.06C22 6.51 17.52 2 12 2S2 6.51 2 12.06c0 5.02 3.66 9.18 8.44 9.94v-7.03H7.9v-2.91h2.54V9.85c0-2.51 1.49-3.9 3.77-3.9 1.09 0 2.23.2 2.23.2v2.46h-1.26c-1.24 0-1.63.77-1.63 1.56v1.87h2.78l-.44 2.91h-2.34V22c4.78-.76 8.44-4.92 8.44-9.94z"/></svg>
          </a>
          <a href="mailto:{CONTACT_EMAIL}" aria-label="Email">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M4 6l8 7 8-7"/></svg>
          </a>
        </div>
      </div>
      <div class="footer-col">
        <h4>快速連結</h4>
        <ul>
          <li><a href="about.html">關於CRAA</a></li>
          <li><a href="organization.html">組織架構</a></li>
          <li><a href="activities.html">近期活動</a></li>
          <li><a href="membership.html">加入會員</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>資源</h4>
        <ul>
          <li><a href="resources.html">理財補給站</a></li>
          <li><a href="reports.html">關鍵報告</a></li>
          <li><a href="plan-2024.html">年度工作計畫</a></li>
          <li><a href="mission.html">協會主要任務</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>聯絡方式</h4>
        <ul>
          <li><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>
          <li><a href="{FACEBOOK_URL}" target="_blank" rel="noopener">Facebook 粉絲專頁</a></li>
          <li><a href="contact.html">聯絡我們表單</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> {SITE_NAME} {SITE_NAME_EN}. All rights reserved.</span>
      <span>網站設計、開發：CRAA 網站志工團隊</span>
    </div>
  </div>
</footer>

<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def write(filename, html):
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename, len(html), "bytes")
