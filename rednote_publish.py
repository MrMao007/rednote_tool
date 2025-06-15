from turtle import pu
from typing import List
from playwright.sync_api import Playwright, sync_playwright


def publish_text(playwright: Playwright, 
                 image_urls: List[str], 
                 title: str, 
                 content: str,
                 tags: List[str]) -> None:
    """
    发布小红书图文笔记
    :param playwright: Playwright实例
    :param image_urls: 图片URL列表
    :param title: 笔记标题
    :param content: 笔记内容
    :param tags: 标签列表
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth/xhs_cookies.json")
    page = context.new_page()
    page.goto("https://www.xiaohongshu.com/explore")
    print("🌐 导航到小红书主页...")
    page.wait_for_timeout(10000)
    login_button = page.locator("form").get_by_role("button", name="登录")
    if(login_button.is_visible()):
        print("❌ 未登录小红书，请先登录")
        return
    
    page.get_by_role("button", name="创作中心").hover()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="创作服务").click()
        
    page1 = page1_info.value
    print("🕒 等待页面跳转")
    
    page1.get_by_text("发布图文笔记").click()
    with page1.expect_file_chooser() as fc_info:
        page1.get_by_role("button", name="Choose File").click()
    file_chooser = fc_info.value
    file_chooser.set_files(image_urls)
    
    page1.get_by_role("textbox", name="填写标题会有更多赞哦～").fill(title)
    final_content = content + "\n\n" + " ".join([f"#{tag}" for tag in tags])
    page1.locator("#quillEditor div").fill(final_content)
    page1.wait_for_timeout(10000) # 等待发布内容加载完成
    page1.get_by_role("button", name="发布").click()
    print("🕒 等待发布成功")
    page1.wait_for_timeout(5000) # 等待发布完成
    print("✅ 发布成功")
    
    # ---------------------
    context.close()
    browser.close()

def publish_video(playwright: Playwright, 
                 video_url: str, 
                 title: str, 
                 content: str,
                 tags: List[str]) -> None:
    """
    发布小红书视频笔记
    :param playwright: Playwright实例
    :param video_url: 视频URL
    :param title: 笔记标题
    :param content: 笔记内容
    :param tags: 标签列表
    """
    return

with sync_playwright() as playwright:
    publish_text(
        playwright,
        #替换成自己的图片URL列表
        image_urls=["/Users/maotianyang/Documents/single.png", "/Users/maotianyang/Documents/single2.png"],
        title="这是一个测试标题",
        content="这是一个测试内容",
        tags=["测试", "小红书"]
    )
