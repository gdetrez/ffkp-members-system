from .models import Registration
from paypal.standard.ipn.signals import payment_was_successful


def confirm_payment(sender, **kwargs):
    # it's important to check that the product exists
    if int(sender.item_number) != 0:
        return

    # Get the registration object
    registration = get_object_or_404(Registration, token = sender.invoice)
    registration.validate_payment(method = 'paypal', amount = sender.mc_gross)

payment_was_successful.connect(confirm_payment)
