from playwright.sync_api import sync_playwright

url = 'https://www.cnn.com/'

# def driver_connection(url):
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         page = browser.new_page()
#         page.goto(url)
#         element = page.wait_for_selector("h1")
#         try:
#             element = page.wait_for_selector("h1", timeout=5000) # added timeout
#             print(element.inner_text())
#         except Exception as e:
#             print(f"Error finding h1: {e}")
#         finally:
#             browser.close()
# from playwright.sync_api import sync_playwright


def driver_connection(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # actually shows the browser
        page = browser.new_page()
        page.goto(url)

        try:
            # Wait for a more consistent element - the page title
            page.wait_for_selector('title', timeout=10000) # Increased timeout

            # Extract the page title
            title = page.title()
            print(f"Page Title: {title}")

            # Example: Find a news headline (adjust selector as needed)
            headline = page.query_selector('.headline__title')
            if headline:
                print(f"First Headline: {headline.inner_text()}")
            else:
                print("Headline not found (selector may need adjustment)")

        except Exception as e:
            print(f"Error during page interaction: {e}")
        finally:
            browser.close()

driver_connection(url)