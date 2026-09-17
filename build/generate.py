#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build
from pages_index import INDEX
from pages_mission_about import MISSION, ABOUT
from pages_org import ORGANIZATION
from pages_activities import ACTIVITIES
from pages_plans import PLAN_2021, PLAN_2022, PLAN_2023, PLAN_2024
from pages_resources_reports import RESOURCES, REPORTS
from pages_membership_contact import MEMBERSHIP, CONTACT

PAGES = [
    dict(filename="index.html", title="中華AI機器人理財協會",
         description="中華AI機器人理財協會（CRAA）推動機器人理財（Robo-Advisor）在台灣的普及與健全發展，結合金融界與科技界人才，促進產官學合作。",
         active="home", content=INDEX, body_class="page-home"),
    dict(filename="mission.html", title="協會主要任務",
         description="CRAA 協會主要任務：教育推廣、人員訓練與認證、國際交流、研究發展。",
         active="mission", content=MISSION),
    dict(filename="about.html", title="關於CRAA",
         description="認識中華AI機器人理財協會的成立宗旨與理事長的話。",
         active="about", content=ABOUT),
    dict(filename="organization.html", title="組織架構",
         description="中華AI機器人理財協會理監事組織架構與現任理監事名單。",
         active="about", content=ORGANIZATION),
    dict(filename="activities.html", title="近期活動",
         description="CRAA 近期活動、會員大會、專題講座與產學合作活動一覽。",
         active="activities", content=ACTIVITIES),
    dict(filename="plan-2021.html", title="2021年度工作計畫",
         description="中華AI機器人理財協會 2021 年度工作計畫與活動時程。",
         active="plans", content=PLAN_2021),
    dict(filename="plan-2022.html", title="2022年度工作計畫",
         description="中華AI機器人理財協會 2022 年度工作計畫：三大願景、五大目標與工作項目。",
         active="plans", content=PLAN_2022),
    dict(filename="plan-2023.html", title="2023年度工作計畫",
         description="中華AI機器人理財協會 2023 年度活動花絮。",
         active="plans", content=PLAN_2023),
    dict(filename="plan-2024.html", title="2024年度工作計畫",
         description="中華AI機器人理財協會 2024 年度重點活動回顧。",
         active="plans", content=PLAN_2024),
    dict(filename="resources.html", title="理財補給站",
         description="精選機器人理財、金融科技與投資理財相關文章。",
         active="resources", content=RESOURCES),
    dict(filename="reports.html", title="關鍵報告",
         description="CRAA 與阿爾發金融科技共同研究製作之全球機器人理財與 ETF 關鍵報告。",
         active="reports", content=REPORTS),
    dict(filename="membership.html", title="加入會員",
         description="加入中華AI機器人理財協會會員，掌握機器人理財第一手趨勢與資源。",
         active="membership", content=MEMBERSHIP),
    dict(filename="contact.html", title="聯絡我們",
         description="聯絡中華AI機器人理財協會：電子信箱、Facebook 粉絲專頁與線上表單。",
         active="contact", content=CONTACT),
]

if __name__ == "__main__":
    for p in PAGES:
        html = build.page(
            title=p["title"],
            description=p["description"],
            active=p["active"],
            content=p["content"],
            body_class=p.get("body_class", ""),
        )
        build.write(p["filename"], html)
    print(f"\n共產生 {len(PAGES)} 個頁面。")
