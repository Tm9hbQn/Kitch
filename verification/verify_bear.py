import os
import time
from playwright.sync_api import sync_playwright

def verify_bear():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        print("Loading page...")
        page.goto("http://localhost:8000/index.html")

        # Wait for initial load
        page.wait_for_timeout(2000)

        # 1. Verify Nag Bubble (Idle)
        # Should appear after 3 seconds.
        print("Waiting for Nag Bubble...")
        page.wait_for_timeout(4000) # Wait 3s + 1s buffer

        # Take screenshot of Nag Bubble
        page.screenshot(path="verification/nag_bubble.png")
        print("Nag bubble screenshot taken: verification/nag_bubble.png")

        # 2. Verify Context Bubble
        # Scroll down to trigger context.
        # "intro" section is at the top.
        # "analysis" is second.
        # Let's scroll to the first highlight.
        # Trigger point is 60% of viewport.
        # If I scroll 200px, maybe?
        print("Scrolling...")
        page.evaluate("window.scrollTo(0, 300)")
        page.wait_for_timeout(2000) # Wait for scroll settle and bear movement

        # Take screenshot
        page.screenshot(path="verification/context_bubble.png")
        print("Context bubble screenshot taken: verification/context_bubble.png")

        browser.close()

if __name__ == "__main__":
    verify_bear()
