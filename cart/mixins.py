# cart/mixins.py
from .models import Cart

class CartMixin:
    def get_or_create_cart(self, request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            print(f"Authenticated user cart {'created' if created else 'found'} for user {request.user.username}")
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
                print(f"New session created with key: {session_key}")
            cart, created = Cart.objects.get_or_create(session_key=session_key)
            print(f"Anonymous user cart {'created' if created else 'found'} for session key {session_key}")
        return cart