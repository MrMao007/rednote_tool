from playwright.sync_api import Playwright, sync_playwright

def test(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth/jygs_cookies.json")
    page = context.new_page()
    page.goto("https://www.jiuyangongshe.com/")
    print("🌐 导航到韭研公社主页...")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="最新热度").hover()
    # page.pause() 
    page.get_by_role("link", name="最新发布").click()
     # 暂停脚本，等待手动操作
     # page.pause() 
    
    # ---------------------
    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        test(playwright)