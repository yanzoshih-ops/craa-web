# -*- coding: utf-8 -*-

def person(name, org_role, role_label):
    initial = name[0]
    return f"""<div class="person">
        <span class="role">{role_label}</span>
        <div class="name">{name}</div>
        <div class="org">{org_role}</div>
      </div>"""


ORGANIZATION = """
<section class="page-hero">
  <div class="bg-grid"></div>
  <div class="glow-orb a"></div>
  <div class="container">
    <div class="breadcrumb"><a href="index.html">首頁</a> / <a href="about.html">關於CRAA</a> / 組織架構</div>
    <span class="eyebrow">Organization</span>
    <h1>組織架構</h1>
    <p class="hero-lead">由金融界、學術界與科技界專業人士共同組成的理監事會（2024–2025 年度）。</p>
  </div>
</section>

<section class="section">
  <div class="container">

    <div class="people-grid reveal" style="margin-bottom:44px">
      <div class="person lead">
        <div class="avatar">楊</div>
        <div>
          <span class="role">理事長</span>
          <div class="name">楊琇惠</div>
          <div class="org">阿爾發金融科技 · 董事長</div>
        </div>
      </div>
    </div>

    <div class="section-head reveal"><h3 style="font-size:20px">副理事長</h3></div>
    <div class="people-grid reveal" style="margin-bottom:44px">
      <div class="person"><span class="role">副理事長</span><div class="name">張森林</div><div class="org">台灣大學 · 財金系教授</div></div>
      <div class="person"><span class="role">副理事長</span><div class="name">周冠男</div><div class="org">政治大學 · 財務管理學系教授</div></div>
      <div class="person"><span class="role">副理事長</span><div class="name">江偉源</div><div class="org">永豐金證券（亞洲）· 前董事長</div></div>
    </div>

    <div class="section-head reveal"><h3 style="font-size:20px">理事</h3></div>
    <div class="people-grid reveal" style="margin-bottom:44px">
      <div class="person"><span class="role">理事</span><div class="name">陳志彥</div><div class="org">阿爾發投顧 · 董事長</div></div>
      <div class="person"><span class="role">理事</span><div class="name">劉炳麟</div><div class="org">逢甲大學 · 招生長</div></div>
      <div class="person"><span class="role">理事</span><div class="name">葉俊佑</div><div class="org">菁英財管學院 · 總經理</div></div>
      <div class="person"><span class="role">理事</span><div class="name">蘇隆照</div><div class="org">台灣金融研訓院 · 菁英講師</div></div>
      <div class="person"><span class="role">理事</span><div class="name">蔡政良</div><div class="org">以諾理財規劃顧問股份有限公司 · 理財規劃顧問</div></div>
    </div>

    <div class="section-head reveal"><h3 style="font-size:20px">常務監事 ・ 監事</h3></div>
    <div class="people-grid reveal" style="margin-bottom:44px">
      <div class="person"><span class="role">常務監事</span><div class="name">林志誠</div><div class="org">安信國際資產 · 董事長</div></div>
      <div class="person"><span class="role">監事</span><div class="name">魏光玄</div><div class="org">普晟法律事務所 · 律師</div></div>
      <div class="person"><span class="role">監事</span><div class="name">黃順裕</div><div class="org">公勝保經 · 資深經理</div></div>
    </div>

    <div class="section-head reveal"><h3 style="font-size:20px">秘書處</h3></div>
    <div class="people-grid reveal">
      <div class="person"><span class="role">秘書長</span><div class="name">蔡至誠</div><div class="org">阿爾發投顧 · 教育長</div></div>
      <div class="person"><span class="role">副秘書長</span><div class="name">謝詠宸</div><div class="org">阿爾發金融科技 · 董事長特助</div></div>
    </div>

  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>想與理監事團隊交流？</h2>
        <p>歡迎透過表單與我們聯絡，或直接加入會員參與協會活動。</p>
      </div>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-primary">聯絡我們</a>
        <a href="membership.html" class="btn btn-outline">加入會員</a>
      </div>
    </div>
  </div>
</section>
"""
