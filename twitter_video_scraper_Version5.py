import time
import random
import pandas as pd
from seleniumbase import SB
from datetime import datetime

class TwitterVideoScraper:
    def __init__(self):
        self.driver = None
        self.videos = []
        self.csv_file = "data_links_twitter.csv"
    
    def launch_browser(self):
        """Starte Chrome-Browser"""
        print("🌐 Starte Chrome Browser...")
        self.driver = SB()
        self.driver.open("https://x.com/home")
        print("✅ Browser gestartet!")
        print("⏳ Bitte logge dich manuell in deinen X-Account ein...")
        print("⏳ Warte 30 Sekunden für manuelles Login...")
        time.sleep(30)
        print("✅ Login abgeschlossen - starten Scraping!")
    
    def scroll_and_collect(self, target_count=20, min_reach=80000):
        """Scrolle und sammle Video-URLs"""
        print(f"\n🎬 Starte Video-Sammlung...")
        print(f"📊 Ziel: {target_count} Videos | Minimum Reach: {min_reach:,}")
        print("=" * 60)
        
        collected = 0
        attempts = 0
        max_attempts = 500
        
        while collected < target_count and attempts < max_attempts:
            attempts += 1
            
            try:
                # Scrolle zufällig (1800-3000px)
                scroll_distance = random.randint(1800, 3000)
                self.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
                
                # Warte zufällig (4.5-8.5 Sekunden)
                wait_time = random.uniform(4.5, 8.5)
                time.sleep(wait_time)
                
                # Suche nach Video-Links
                articles = self.driver.find_elements("article")
                
                for article in articles:
                    if collected >= target_count:
                        break
                    
                    try:
                        # Versuche Video-Link zu finden
                        video_link = article.find_element("a", is_visible=True)
                        url = video_link.get_attribute("href")
                        
                        if url and "status" in url and url not in [v['url'] for v in self.videos]:
                            # Versuche Reach/Impressionen zu bekommen
                            try:
                                metrics_text = article.text
                                reach = self.extract_reach(metrics_text)
                                
                                if reach >= min_reach:
                                    video_data = {
                                        "url": url,
                                        "reach": reach,
                                        "date_collected": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                        "platform": "X (Twitter)"
                                    }
                                    self.videos.append(video_data)
                                    collected += 1
                                    
                                    print(f"\n🎬 NEW VIDEO ADDED!")
                                    print(f"🔗 URL: {url}")
                                    print(f"📊 Reach: {reach:,}")
                                    print(f"📈 Progress: {collected}/{target_count} ({(collected/target_count)*100:.1f}%) | ⏳ Remaining: {target_count - collected}")
                            
                            except Exception as e:
                                pass
                    
                    except Exception as e:
                        pass
                
            except Exception as e:
                print(f"⚠️ Fehler beim Scraping: {e}")
                continue
        
        print("\n" + "=" * 60)
        print(f"✅ Scraping abgeschlossen!")
        print(f"📊 Insgesamt {collected} Videos gefunden")
        return collected
    
    def extract_reach(self, text):
        """Extrahiere Reach/Impressionen aus Text"""
        text_lower = text.lower()
        
        # Versuche verschiedene Formate zu parsen
        import re
        
        # Suche nach Zahlen mit M (Millionen), K (Tausend)
        patterns = [
            r'(\d+\.?\d*)\s*[mM](?:\s|$)',  # 3.7M
            r'(\d+\.?\d*)\s*[kK](?:\s|$)',  # 80K
            r'(\d+)\s*(?:million|thousand)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                num = float(match.group(1))
                if 'k' in pattern.lower():
                    return int(num * 1000)
                elif 'm' in pattern.lower():
                    return int(num * 1000000)
        
        # Default fallback
        return 0
    
    def save_results(self):
        """Speichere Ergebnisse als CSV"""
        if self.videos:
            df = pd.DataFrame(self.videos)
            df.to_csv(self.csv_file, index=False, encoding='utf-8')
            print(f"\n💾 Datei gespeichert: {self.csv_file}")
            print("\n📊 Vorschau:")
            print(df.to_string())
        else:
            print("⚠️ Keine Videos gefunden!")
    
    def close_browser(self):
        """Schließe Browser"""
        if self.driver:
            self.driver.quit()
            print("\n🔚 Browser geschlossen!")


# ===========================
# HAUPTPROGRAMM
# ===========================
if __name__ == "__main__":
    print("=" * 60)
    print("🎬 TWITTER VIDEO SCRAPER")
    print("=" * 60)
    
    scraper = TwitterVideoScraper()
    
    try:
        # Schritt 1: Browser starten
        scraper.launch_browser()
        
        # Schritt 2: Videos sammeln
        scraper.scroll_and_collect(
            target_count=20,      # Wie viele Videos sammeln
            min_reach=80000       # Minimum Impressionen
        )
        
        # Schritt 3: Ergebnisse speichern
        scraper.save_results()
    
    except Exception as e:
        print(f"\n❌ Fehler: {e}")
    
    finally:
        scraper.close_browser()