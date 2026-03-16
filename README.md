# 🐦 X (Twitter) High-Reach Video Scraper Bot

> A stealth Python bot that automatically scrolls X (Twitter), detects video posts, filters them by impressions, and exports the results to CSV - ready for content repurposing or competitor analysis.

---

## 🎯 What It Does

Marketing teams and content creators need to know **what's going viral**. This bot automates that intelligence-gathering by:

- 🔍 Scrolling through X feeds automatically
- 🎬 Detecting only **video posts** (skips text/image tweets)
- 📊 Filtering by a **minimum reach threshold** (e.g. 80K, 200K, 1M+)
- 💾 Exporting collected posts (URL, reach, description, timestamp) to **CSV**
- 🕵️ Using **stealth scrolling** with randomized timing to avoid detection

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| `SeleniumBase` (UC Mode) | Stealth browser automation, bypasses bot detection |
| `Selenium` | DOM scraping & element interaction |
| `Pandas` | Data collection & CSV export |
| `Python 3.11` | Core language |

---

## 📁 Output Example

The bot exports a clean CSV with the following structure:

| url | reach | description | timestamp |
|---|---|---|---|
| https://x.com/user/status/123... | 3,700,000 | "Just launched our new..." | 14:32:01 |
| https://x.com/user/status/456... | 850,000 | "This marketing tip will..." | 14:35:44 |

---

## ⚙️ How to Use

### 1. Install Dependencies

```bash
pip install seleniumbase pandas
```

### 2. Run Cell 1 — Launch Browser
The first cell opens Chrome and navigates to X.  
**Manually log in** to your X account when prompted.

### 3. Run Cell 2 — Start Scraping
Configure your parameters at the bottom of the notebook:

```python
df_final = run_video_automation(
    driver,
    target_count=20,      # How many videos to collect
    min_reach=80000       # Minimum impressions threshold
)
```

The bot will scroll, collect, and print progress in real time:
```
🎬 NEW VIDEO ADDED!
🔗 URL: https://x.com/hootsuite/status/201329...
📊 Reach: 3.7M
📈 Progress: 1/20 (5.0%) | ⏳ Remaining: 19
```

### 4. Results
Results are saved automatically to `data_links_twitter.csv`.

---

## 💡 Use Cases

- **Content repurposing** - Find viral videos to legally reshare or get inspired by
- **Competitor analysis** - Monitor what content performs best in your niche
- **Trend detection** - Identify rising topics before they peak
- **Influencer research** - Discover high-performing creators in a space

---

## 🔧 Customization

| Parameter | Default | Description |
|---|---|---|
| `target_count` | 20 | Number of videos to collect |
| `min_reach` | 80,000 | Minimum impressions to qualify |
| Scroll distance | 1800–3000px | Randomized for stealth |
| Wait time | 4.5–8.5s | Randomized to mimic human behavior |

---

## ⚠️ Disclaimer

This tool is intended for **personal research and marketing analysis** only. Always comply with [X's Terms of Service](https://twitter.com/en/tos) when using automation tools. Use responsibly.

---

## 👨‍💻 Author

**[Awby]** — Data Scientist & Digital Marketing Analyst  
5 years experience in marketing analytics, automation, and data science.

📧 awbyybwa93@gmail.com

---

*If this was useful, consider ⭐ starring the repo!*
