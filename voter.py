from playwright.sync_api import sync_playwright
import time

# Function to run the script
def oaey_voter():
    votes = 0
    with sync_playwright() as p:
        # Launch the Chromium browser (set headless=False to see the browser)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context();
        page = context.new_page()

        # Outer loop: 3000 times. 1500 votes in 2 days
        for i in range(3000): 
            for j in range(5):
                context.clear_cookies();

                page.goto("https://www.thaiupdate.info/female-star-of-the-year-group-1/")

                # Interact with the page
                page.locator("id=PDI_answer65586722").check()
                page.locator("id=pd-vote-button14773738").click()
                page.wait_for_selector("id=PDI_form14773738", timeout=9000)

                # Extract and calculate the answer
                expression = page.locator("id=captcha_14773738").text_content()
                numbers = [int(num) for num in expression.split() if num.isdigit()]
                num1 = numbers[0]
                num2 = numbers[1]
                answer = num1 + num2

                # Fill in the answer and click the vote button
                page.locator("id=answer_14773738").fill(str(answer))
                page.locator("id=pd-vote-button14773738").click()

                votes += 1
                print("vote count: ", votes)

            # Pause for 1 minute and 30 seconds between outer loop iterations
            print("Pausing for 1 minute...")
            time.sleep(60)

        # Close the browser when done
        browser.close()

# Run the script
oaey_voter()
