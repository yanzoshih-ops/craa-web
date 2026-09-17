# -*- coding: utf-8 -*-

def tab_nav(active_year):
    years = ["2024", "2023", "2022", "2021"]
    items = []
    for y in years:
        cls = "active" if y == active_year else ""
        items.append(f'<a href="plan-{y}.html" class="{cls}">{y} 年度</a>')
    return '<div class="tab-nav reveal">' + "".join(items) + '</div>'


def plan_hero(year):
    return f"""
<section class="page-hero">
  <div class="bg-grid"></div>
  <div class="glow-orb a"></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">首頁</a> / 年度工作計畫 / {year} 年</div>
    <span class="eyebrow">Annual Work Plan</span>
    <h1>{year} 年度工作計畫</h1>
    {tab_nav(year)}
  </div>
</section>
"""


PLAN_2021 = plan_hero("2021") + """
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Month by Month</span>
      <h2>全年活動時程</h2>
      <p class="text-secondary">2021 年為協會推動機器人理財教育扎根的重要一年，包含臺灣首張機器人理財證照啟動、逢甲大學正式學校課程開設，以及全年不間斷的系列講座。</p>
    </div>
    <div class="timeline reveal">
      <div class="timeline-item">
        <span class="month">1 月</span>
        <ul><li>臺灣首張機器人理財證照啟動</li><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">2 月</span>
        <ul><li>魚竿計畫啟動</li><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">3 月</span>
        <ul><li>110 年度會員大會</li><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">4 月</span>
        <ul><li>理監事聯席會議</li><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">5 月</span>
        <ul><li>機器人理財學術／業界論壇</li><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">6 月</span>
        <ul><li>會員聯誼活動</li><li>機器人理財系列講座</li><li>機器人理財正式學校課程（逢甲大學）</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">7 月</span>
        <ul><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">8 月</span>
        <ul><li>海外參訪－全球最大指數型基金公司 The Vanguard Group 領航集團</li><li>機器人理財系列講座</li></ul>
      </div>
      <div class="timeline-item">
        <span class="month">9 － 12 月</span>
        <ul><li>持續舉辦機器人理財系列講座</li><li>理監事聯席會議</li><li>會員聯誼活動</li></ul>
      </div>
    </div>
  </div>
</section>
""" + """
<section class="section section-alt">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>查看更多年度計畫</h2><p>瀏覽 2022－2024 年度的願景目標與工作項目。</p></div>
      <div class="hero-actions"><a href="plan-2022.html" class="btn btn-primary">2022 年度計畫</a></div>
    </div>
  </div>
</section>
"""


PLAN_2022 = plan_hero("2022") + """
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Vision</span>
      <h2>三大願景</h2>
    </div>
    <div class="grid grid-3 reveal">
      <div class="card"><span class="pillar-num">VISION 01</span><h3>成為台灣最具代表性的機器人理財協會</h3></div>
      <div class="card"><span class="pillar-num">VISION 02</span><h3>樹立台灣理財金融秩序，建立正確理財知識</h3></div>
      <div class="card"><span class="pillar-num">VISION 03</span><h3>建構台灣金融生態圈，成為資源與資訊交流整合平台</h3></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Goals</span>
      <h2>五大目標</h2>
    </div>
    <div class="grid grid-2 reveal">
      <div class="card"><h3>擴大會員數</h3><p>招收新會員至 100 人。</p></div>
      <div class="card"><h3>舉辦會員聯誼活動</h3><p>加強會員感情連結。</p></div>
      <div class="card"><h3>安排企業參訪</h3><p>聚焦金融科技發展前景。</p></div>
      <div class="card"><h3>成立委員會組織</h3><p>加強協會組織運作功能。</p></div>
      <div class="card" style="grid-column:span 2"><h3>創辦理財論壇</h3><p>邀請國內外學者擔任與談人。</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Work Items</span>
      <h2>工作項目</h2>
    </div>
    <div class="table-wrap reveal">
      <table>
        <thead><tr><th>工作項目</th><th>目的</th><th>頻率</th></tr></thead>
        <tbody>
          <tr><td>學術研討</td><td>邀請海內外產官學專業人士參與</td><td>一年一次</td></tr>
          <tr><td>兒童理財營</td><td>讓理財教育納入台灣教育課綱</td><td>每年二次</td></tr>
          <tr><td>企業參訪</td><td>拓展視野、鏈結產業資源</td><td>一年一次</td></tr>
          <tr><td>會員活動</td><td>凝聚會員向心力</td><td>不定期舉辦講座與活動</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
""" + """
<section class="section section-alt">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>查看更多年度計畫</h2><p>瀏覽 2023、2024 年度的活動花絮。</p></div>
      <div class="hero-actions"><a href="plan-2023.html" class="btn btn-primary">2023 年度計畫</a></div>
    </div>
  </div>
</section>
"""


def image_year_plan(year, prev_year, extra_note=""):
    return plan_hero(year) + f"""
<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;gap:48px">
      <div class="reveal">
        <span class="kicker">{year} Highlights</span>
        <h2 style="font-size:26px">路程中的點點滴滴</h2>
        <p class="text-secondary">{year} 年度，協會持續以「教育推廣、人員訓練、國際交流、研究發展」四大任務主軸為核心，舉辦多場會員大會、專題講座與產學合作活動。{extra_note}</p>
        <p class="text-secondary">完整活動花絮與圖冊，歡迎至協會 Facebook 粉絲專頁查看第一手紀錄與現場照片。</p>
        <a href="https://www.facebook.com/profile.php?id=100057627691904" target="_blank" rel="noopener" class="btn btn-outline">前往 Facebook 相簿</a>
      </div>
      <div class="reveal">
        <img src="assets/img/gallery/activity-ai-fintech-academy.jpg" alt="{year} 年度活動花絮" style="border-radius:var(--radius-lg);border:1px solid var(--border);box-shadow:var(--shadow-soft)">
      </div>
    </div>
  </div>
</section>
""" + """
<section class="section section-alt">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>查看更多年度計畫</h2><p>瀏覽其他年度的工作計畫與活動紀錄。</p></div>
      <div class="hero-actions"><a href="plan-""" + prev_year + """.html" class="btn btn-primary">""" + prev_year + """ 年度計畫</a></div>
    </div>
  </div>
</section>
"""


PLAN_2024 = plan_hero("2024") + """
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">2024 Highlights</span>
      <h2>年度重點活動回顧</h2>
      <p class="text-secondary">2024 年協會舉辦多場會員大會、大咖講座與產學交流活動，詳細活動內容請見「近期活動」頁面：</p>
    </div>
    <div class="resource-list reveal">
      <div class="resource-item">
        <div class="rdate">09.09</div>
        <div class="rbody"><h3>【2024 AI HUB－SIG 小聚交流活動】</h3></div>
      </div>
      <div class="resource-item">
        <div class="rdate">08.23</div>
        <div class="rbody"><h3>【2024 專題講座暨第三屆第一次會員大會】</h3></div>
      </div>
      <div class="resource-item">
        <div class="rdate">05.14</div>
        <div class="rbody"><h3>『大咖講座』閱讀前哨站部落格站長－瓦基</h3></div>
      </div>
      <div class="resource-item">
        <div class="rdate">05.10</div>
        <div class="rbody"><h3>AI 新時代金融科技新思維－活動回顧</h3></div>
      </div>
      <div class="resource-item">
        <div class="rdate">04.30</div>
        <div class="rbody"><h3>【2024 會員活動暨大師論壇】</h3></div>
      </div>
      <div class="resource-item">
        <div class="rdate">04.16</div>
        <div class="rbody"><h3>『大咖講座』SUPER 仙女老師－余懷瑾</h3></div>
      </div>
    </div>
    <div class="text-center" style="margin-top:32px">
      <a href="activities.html" class="btn btn-outline">查看完整活動介紹</a>
    </div>
  </div>
</section>
""" + """
<section class="section section-alt">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>查看更多年度計畫</h2><p>瀏覽 2023 年度的活動花絮。</p></div>
      <div class="hero-actions"><a href="plan-2023.html" class="btn btn-primary">2023 年度計畫</a></div>
    </div>
  </div>
</section>
"""

PLAN_2023 = image_year_plan(
    "2023", "2022",
    extra_note="官網原始紀錄以活動照片圖冊呈現，完整內容以協會社群公告為準。"
)
