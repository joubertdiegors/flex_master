# cart/context_processors.py
from .mixins import CartMixin

def cart_context(request):
    mixin = CartMixin()
    cart = mixin.get_or_create_cart(request)
    return {'cart': cart}
