import time
import requests
import asyncio
from pyppeteer import launch


async def capture_screenshot(url, screenshot_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': screenshot_path})
    await browser.close()


# Send GET request and calculate response time
url = "https://mentalaba.uz/"
start_time = time.time()
response = requests.get(url)
end_time = time.time()
response_time = end_time - start_time

# Take a screenshot using Pyppeteer
screenshot_path = "mentalaba.png"
loop = asyncio.get_event_loop()
loop.run_until_complete(capture_screenshot(url, screenshot_path))

# Measure the amount of traffic sent
traffic_sent = len(response.content)
traffic_sent_mb = traffic_sent / (1024 * 1024)

# Print results
print(f"Response time: {response_time} seconds")
print(f"Traffic sent: {traffic_sent_mb} mbbytes")
print(f"Screenshot saved at: {screenshot_path}")
