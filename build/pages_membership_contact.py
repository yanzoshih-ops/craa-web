# -*- coding: utf-8 -*-

MEMBERSHIP = """
<section class="page-hero">
  <div class="bg-grid"></div>
  <div class="glow-orb a"></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">首頁</a> / 加入會員</div>
    <span class="eyebrow">Membership</span>
    <h1>加入會員</h1>
    <p class="hero-lead">成為 CRAA 會員，掌握機器人理財第一手趨勢、教育資源與交流機會，與台灣理財科技社群一起成長。</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="kicker">Fees</span>
      <h2>會費說明</h2>
    </div>
    <div class="grid grid-2 reveal" style="max-width:720px;margin:0 auto">
      <div class="fee-card">
        <div class="badge-soft">一次性</div>
        <div class="amount">NT$ 3,000</div>
        <div class="desc">入會費（僅需繳交一次）</div>
      </div>
      <div class="fee-card">
        <div class="badge-soft">每年</div>
        <div class="amount">NT$ 2,000</div>
        <div class="desc">常年會費（每年年費）</div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-head center reveal">
      <span class="kicker">How to Join</span>
      <h2>入會流程</h2>
    </div>
    <div class="steps reveal">
      <div class="step">
        <h3>填寫線上申請書</h3>
        <p>填妥基本資料與加入動機，送出 Google 表單申請。</p>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSclYGDfmspf4P_mdP-A94sB4ZGqfeWbPW4XFOPZbAaKxvBzUA/viewform" target="_blank" rel="noopener" class="btn btn-outline btn-sm" style="margin-top:14px">前往申請表單 ↗</a>
      </div>
      <div class="step">
        <h3>完成會費繳納</h3>
        <p>可選擇線上刷卡繳費，或以銀行匯款方式繳交入會費及常年會費。</p>
        <a href="https://core.newebpay.com/EPG/memberfee/Qt0CFd" target="_blank" rel="noopener" class="btn btn-outline btn-sm" style="margin-top:14px">線上繳費連結 ↗</a>
      </div>
      <div class="step">
        <h3>審核通知</h3>
        <p>協會秘書處確認資料與款項後，將以 Email 通知您入會結果與後續事宜。</p>
      </div>
    </div>

    <div class="info-box reveal" style="margin-top:40px">
      <strong>匯款資訊：</strong>戶名：中華機器人理財協會　｜　帳號：2007-01-0001033-1（台新銀行－台中分行）
    </div>

    <div class="text-center reveal" style="margin-top:32px">
      <a href="https://uploads.strikinglycdn.com/files/da267861-352a-4132-9a8a-c62b86154bc7/CRAA%E4%B8%AD%E8%8F%AF%E6%A9%9F%E5%99%A8%E4%BA%BA%E7%90%86%E8%B2%A1%E5%8D%94%E6%9C%83%E7%B0%A1%E4%BB%8B_2023.pdf" target="_blank" rel="noopener" class="btn btn-outline">下載協會簡介 PDF</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>有任何入會相關問題？</h2>
        <p>歡迎直接與協會秘書處聯繫，我們將盡快為您說明。</p>
      </div>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-primary">聯絡我們</a>
      </div>
    </div>
  </div>
</section>
"""

CONTACT = """
<section class="page-hero">
  <div class="bg-grid"></div>
  <div class="glow-orb a"></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">首頁</a> / 聯絡我們</div>
    <span class="eyebrow">Contact Us</span>
    <h1>聯絡我們</h1>
    <p class="hero-lead">對協會活動、會員申請或合作提案有任何問題，歡迎透過以下方式與我們聯繫。</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="reveal">
        <div class="contact-info-item">
          <div class="icon-badge">✉️</div>
          <div>
            <h4>電子信箱</h4>
            <p><a href="mailto:craa.tw@gmail.com">craa.tw@gmail.com</a></p>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="icon-badge">📘</div>
          <div>
            <h4>Facebook 粉絲專頁</h4>
            <p><a href="https://www.facebook.com/profile.php?id=100057627691904" target="_blank" rel="noopener">中華AI機器人理財協會 CRAA</a></p>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="icon-badge">🏦</div>
          <div>
            <h4>會費匯款帳戶</h4>
            <p>中華機器人理財協會｜台新銀行台中分行｜2007-01-0001033-1</p>
          </div>
        </div>
        <div class="contact-info-item">
          <div class="icon-badge">🤝</div>
          <div>
            <h4>加入會員</h4>
            <p><a href="membership.html">查看入會流程與費用說明 →</a></p>
          </div>
        </div>
      </div>

      <form class="form-panel reveal" action="mailto:craa.tw@gmail.com" method="post" enctype="text/plain">
        <div class="field">
          <label for="name">名字</label>
          <input id="name" name="名字" type="text" placeholder="請輸入您的姓名" required>
        </div>
        <div class="field">
          <label for="email">電子信箱</label>
          <input id="email" name="電子信箱" type="email" placeholder="you@example.com" required>
        </div>
        <div class="field">
          <label for="message">訊息</label>
          <textarea id="message" name="訊息" placeholder="請輸入您想詢問或討論的內容"></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-block">送出訊息</button>
        <p class="form-note">點擊送出將開啟您的預設郵件軟體以完成寄送；若無法順利開啟，歡迎直接來信 craa.tw@gmail.com。</p>
      </form>
    </div>
  </div>
</section>
"""
