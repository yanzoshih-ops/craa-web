# 中華AI機器人理財協會官方網站

中華AI機器人理財協會（Chinese Robo-Advisor Association，CRAA）官方網站原始碼。純靜態 HTML / CSS / JavaScript 網站，無需任何建置工具，可直接部署於 GitHub Pages。

## 網站架構

```
├── index.html              首頁
├── mission.html            協會主要任務
├── about.html              關於CRAA
├── organization.html       組織架構
├── activities.html         近期活動
├── plan-2024.html          2024 年度工作計畫
├── plan-2023.html          2023 年度工作計畫
├── plan-2022.html          2022 年度工作計畫
├── plan-2021.html          2021 年度工作計畫
├── resources.html          理財補給站
├── reports.html            關鍵報告
├── membership.html         加入會員
├── contact.html            聯絡我們
├── assets/
│   ├── css/style.css       網站樣式（科技感深色風格）
│   ├── js/main.js          導覽選單、捲動顯示等互動效果
│   └── img/                Logo、favicon 與活動照片
└── build/                  網站產生器（僅開發時使用，見下方說明）
```

## 部署到 GitHub Pages

1. 在 GitHub 建立新的 repository（例如 `craa-website`）。
2. 將本資料夾內所有檔案上傳 / push 到該 repository 的預設分支（`main`）。
3. 到 repository 的 **Settings → Pages**，「Build and deployment」來源選擇 **Deploy from a branch**，分支選 `main`、資料夾選 `/ (root)`，儲存。
4. 等待約 1 分鐘，GitHub 會提供一個 `https://<你的帳號>.github.io/<repository名稱>/` 的網址，即為正式網站。
5. 若使用自訂網域，於 repository 新增 `CNAME` 檔案並在 DNS 設定 CNAME 記錄，詳見 GitHub 官方文件。

> 這是純靜態網站，**不需要**安裝 Node.js、Ruby 或任何套件即可部署，push 上去就能直接使用。

## 本機預覽

在專案根目錄下執行（需要 Python 3）：

```bash
python3 -m http.server 8000
```

然後開啟瀏覽器至 `http://localhost:8000/` 即可預覽。

## 內容修改

所有頁面都是獨立的 `.html` 檔案，可直接用文字編輯器打開修改文字內容。共用的頁首、頁尾、選單與配色集中在：

- `assets/css/style.css`：所有顏色、字體、版面樣式（顏色定義在檔案最上方的 `:root` 區塊，方便統一調整）。
- `assets/js/main.js`：手機選單開合、捲動顯示動畫等互動邏輯。

### 進階：使用產生器統一修改頁首/頁尾

若同時要修改「所有頁面」共用的頁首、頁尾或選單結構，建議透過 `build/` 資料夾內的 Python 產生器來源進行修改，可避免 13 個頁面要一一手動修改：

```bash
cd build
python3 generate.py
```

此指令會依據 `build/*.py` 內定義的內容，重新產生所有根目錄下的 `.html` 檔案。此步驟僅為開發輔助工具，**網站上線後完全不需要 Python**，GitHub Pages 只會讀取產生好的靜態 `.html` 檔案。

## 圖片與版權

`assets/img/gallery/` 內的活動照片、`assets/img/logo-*.png` 及 favicon 皆取自協會既有素材（含官方 Logo 向量檔重新輸出）。如需更換照片，直接以相同檔名覆蓋 `assets/img/gallery/` 內對應檔案即可（建議寬度 1200–1920px、JPEG 品質 75–85 以維持網站載入速度）。

## 內容來源

網站文字內容整理自協會官方網站 [craa.org.tw](https://www.craa.org.tw/) 公開資訊（協會宗旨、理監事名單、活動紀錄、理財補給站文章、關鍵報告、會費與入會流程等），並重新設計版面與視覺風格。個別文章與報告的下載連結指向原始官網，如內容有更新請至原始頁面確認。

---

網站設計、開發：CRAA 網站志工團隊
