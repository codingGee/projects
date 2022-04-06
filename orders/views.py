from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.conf import settings
import stripe


# Create your views here.
from django.views.generic.base import TemplateView

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
    
    # getting pblic ke for strip and passing it in the template 
    # overiding get_context_data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context
    
    
# stripe api key
stripe.api_key = settings.STRIPE_TEST_PUBLISHABLE_KEY

# charge view 
def charge(request):
    # Get the permission 
    permission = Permission.objects.get(codename='special_status')
    
    # get the user
    u = request.user
    # add user permission 
    u.user_permissions.add(permission)
    if request.method == "Post":
        stripe.Charge.create(
            amount = 3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html', )