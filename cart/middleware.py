# cart/middleware.py
from .models import Cart, CartItem

class TransferCartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("TransferCartMiddleware __call__ method invoked")
        response = self.get_response(request)

        if request.user.is_authenticated:
            print(f"User {request.user.username} is authenticated.")
            session_key = request.session.session_key
            old_session_key = request.session.get('old_session_key')
            print(f"Current session key: {session_key}, Old session key: {old_session_key}")

            if old_session_key:
                try:
                    anonymous_cart = Cart.objects.get(session_key=old_session_key)
                    print(f"Anonymous cart found for old session key {old_session_key}")

                    user_cart, created = Cart.objects.get_or_create(user=request.user)
                    print(f"User cart {'created' if created else 'found'} for user {request.user.username}")

                    for item in anonymous_cart.items.all():
                        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=item.product)
                        if created:
                            cart_item.quantity = item.quantity
                        else:
                            cart_item.quantity += item.quantity
                        cart_item.price = item.price
                        cart_item.promotion = item.promotion
                        cart_item.save()

                    anonymous_cart.delete()
                    print(f"Anonymous cart for old session key {old_session_key} deleted")
                except Cart.DoesNotExist:
                    print(f"No anonymous cart found for old session key {old_session_key}")
            else:
                print("No old session key found")
        else:
            print("User is not authenticated")

        return response
