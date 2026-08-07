from playwright.sync_api import sync_playwright

def scrape_page(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)

        title = page.title()
        text = page.inner_text("body")

        browser.close()

        return {
            "url": url,
            "title": title,
            "text": text[:5000],
        }