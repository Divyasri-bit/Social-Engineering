import time

def phishing_simulation():
    print("Welcome to the Phishing Awareness Simulator!")
    print("This program will simulate a phishing scenario to teach you how to spot it.")
    print("-" * 50)
    time.sleep(2)

    # Simulated phishing email content
    simulated_email = """
    Subject: Urgent - Verify Your Account Now!

    Dear User,

    We've noticed unusual activity in your account. To secure it, please verify your details by clicking the link below:

    [FAKE LINK] https://secure-verify-fake.com/login

    Failure to do so within 24 hours may result in account suspension.

    Regards,
    Security Team
    """
    print("Here is a simulated email:")
    print("-" * 50)
    print(simulated_email)
    print("-" * 50)

    # Ask user to identify suspicious elements
    time.sleep(2)
    print("Can you spot the suspicious elements in the email?")
    print("1. The sender's address is not real.")
    print("2. The link points to a fake website.")
    print("3. There is unnecessary urgency to make you act quickly.")
    print("4. The email contains generic greetings like 'Dear User'.")
    print("-" * 50)

    # Explanation
    time.sleep(2)
    print("Always verify links, sender addresses, and avoid clicking suspicious links!")
    print("This concludes the phishing awareness simulation.")
    print("-" * 50)

# Run the simulation
phishing_simulation()
