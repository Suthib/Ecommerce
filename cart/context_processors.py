from . cart import Cart

# Create context processor so our cart can work on all pages


def cart(request):
    # Return the default data from or Cart
    return {'cart': Cart(request)}
