import stripe


def stripe_balance(api_key):
    stripe.api_key = api_key
    return stripe.Balance.retrieve()
