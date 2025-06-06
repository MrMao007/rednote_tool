import os
from playwright.sync_api import Playwright, sync_playwright


def login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    print("🌐 导航到小红书登录页面...")
    page.goto("https://www.xiaohongshu.com/explore")
    
    print("\n📋 请按照以下步骤操作:")
    print("1. 在浏览器中手动登录小红书")
    print("2. 登录成功后，确保可以正常访问小红书内容")
    print("3. 完成后，在此终端中按 Enter 键继续...")
    
    input()  # 等待用户输入
    
    print("🍪 获取cookies...")
    os.makedirs("auth", exist_ok=True)  # 确保目录存在
    cookies_file = "auth/xhs_cookies.json"
    storage_state = context.storage_state(path=cookies_file)
    
    print(f"✅ Cookies已保存到: {cookies_file}")
    print(f"📊 共保存了 {len(storage_state)} 个cookies")

    # ---------------------
    context.close()
    browser.close()



if __name__ == "__main__":
    with sync_playwright() as playwright:
        login(playwright)
