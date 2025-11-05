import stripe
#import buy
def process_payment(amount_in_rupees):
    stripe.api_key = "sk_test_51Qf2ToLgPWQJDL79qlQ3fqeij3byJ5G3CshmD0514G7JmQPBCx4XskdqZBHbBBNUhAyaP0lo5ksJE6ukt71y1ZpF00ZuOynVzF"  # Use your test secret key

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "inr",
                    "product_data": {
                        "name": "Your Food Order",
                    },
                    "unit_amount": amount_in_rupees * 100,  # Convert ₹ to paise
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://example.com/success",  # Dummy URL
            cancel_url="https://example.com/cancel",
            
        )

        #print("Please complete the payment using the following link:\n\n")
        #print(session.url)
        url=session.url
        #print(url)
        import webbrowser
        webbrowser.open(url)
        

    #except Exception as e:
        #print("Error during payment:", e)
    finally:
        print("\nThank you...")
