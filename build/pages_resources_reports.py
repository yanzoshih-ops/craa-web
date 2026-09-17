# -*- coding: utf-8 -*-

RESOURCES_SOURCE = "https://www.craa.org.tw/financial-supply-station"

_articles = [
    ("2025.03.07", "台灣已經進入超高齡社會，政府跨部會加速推動信託3.0", "台灣已經進入超高齡社會，帶來了對高齡及身心障礙者的財產與生活品質保障的迫切需求。"),
    ("2024.06.05", "守護高齡金融安全，探索AI機器人理財！", "高齡金融詐騙頻傳，使得高齡金融剝削風險與安養信託之重要性愈發受到重視。"),
    ("2024.03.14", "黃金價格突破天際，背後真相揭秘！", "黃金市場與美股、比特幣一同締造歷史新高，現貨黃金更是從每盎司 $2119 驚人飆升至 $2195.23。"),
    ("2024.02.17", "金融科技的未來版圖", "新興市場正迅速改寫全球金融科技（FinTech）的成長版圖。"),
    ("2024.01.26", "股市創新高，究竟是福還是禍？", ""),
    ("2024.01.24", "機器人理財的崛起：自動化您的投資組合", ""),
    ("2024.01.20", "開放銀行登三階 可作5業務", "金融業可串聯 TSP，提供存款、信用卡、貸款、支付及手機門號轉帳創新服務。"),
    ("2023.07.24", "想要變有錢 該避開的5個理財陷阱", ""),
    ("2023.07.14", "機器人理財衝逾73億 年增32%", ""),
    ("2023.07.13", "六月最新調查－台灣行動支付使用習慣", ""),
    ("2023.06.28", "開放生成式AI之前，金管會對金融業提出資安五大示警", ""),
    ("2023.06.26", "退休要準備多少錢才夠？財務顧問推薦4%法則給你參考", ""),
    ("2023.06.21", "台灣的銀行與投信投顧辦理機器人理財的差異", ""),
    ("2022.02.25", "盤踞美洲東西岸：理財機器人公司Betterment及WealthFront", ""),
    ("2022.02.25", "日本人工智慧(AI)機器人理財平台WealthNavi在東京交易所IPO", ""),
    ("2022.02.15", "機器人理財小故事－美國第一家機器人理財公司Betterment", ""),
]


def _render_articles():
    items = []
    for date, title, excerpt in _articles:
        p = f"<p>{excerpt}</p>" if excerpt else ""
        items.append(f"""<a class="resource-item" href="{RESOURCES_SOURCE}" target="_blank" rel="noopener">
        <div class="rdate">{date}</div>
        <div class="rbody"><h3>{title}</h3>{p}</div>
        <div class="rarrow">↗</div>
      </a>""")
    return "\n".join(items)


RESOURCES = """
<section class="page-hero">
  <div class="bg-grid"></div>
  <div class="glow-orb a"></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">首頁</a> / 理財補給站</div>
    <span class="eyebrow">Financial Supply Station</span>
    <h1>理財補給站</h1>
    <p class="hero-lead">精選機器人理財、金融科技與投資理財相關文章，補給您的理財知識存量。點選文章將前往協會官方網站閱讀完整內容。</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="resource-list reveal">
""" + _render_articles() + """
    </div>
  </div>
</section>
"""

_reports = [
    ("2023", "全球機器人理財關鍵報告"),
    ("2022", "全球ETF關鍵報告"),
    ("2021", "全球 ETF 關鍵報告"),
    ("2020", "全球 ETF 關鍵報告"),
]

REPORTS_SOURCE = "https://www.craa.org.tw/1"


def _render_reports():
    items = []
    for year, title in _reports:
        items.append(f"""<div class="resource-item report-item">
        <div style="display:flex;align-items:center;gap:18px">
          <div class="rdate">{year}</div>
          <div class="rbody"><h3>【CRAA】{year} {title}</h3></div>
        </div>
        <a href="{REPORTS_SOURCE}" target="_blank" rel="noopener" class="btn btn-outline btn-sm">前往下載 ↗</a>
      </div>""")
    return "\n".join(items)


REPORTS = """
<section class="page-hero">
  <div class="bg-grid"></div>
  <div class="glow-orb a"></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">首頁</a> / 關鍵報告</div>
    <span class="eyebrow">Key Reports</span>
    <h1>關鍵報告</h1>
    <p class="hero-lead">由中華AI機器人理財協會與阿爾發金融科技共同研究製作之年度關鍵報告，涵蓋全球機器人理財與 ETF 市場趨勢。</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="resource-list reveal">
""" + _render_reports() + """
    </div>
    <div class="info-box reveal" style="margin-top:32px">
      <strong>使用說明：</strong>關鍵報告內容由中華民國機器人理財協會與阿爾發金融科技共同研究製作，如需引用內容、文章或數據，須註明出處。
    </div>
  </div>
</section>
"""
