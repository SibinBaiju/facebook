from ecomapp.models import Carts

def cart_count_context(request):
    if request.user.is_authenticated:
        count=Carts.objects.filter(user_id=request.user).exclude(status='order-placed').count()
        return {'count':count}
    else:
        return{'count':0}
    