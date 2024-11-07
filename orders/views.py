from django.shortcuts import render

# Create your views here.


def order_list(request):
    # Aquí puedes definir la lógica para mostrar la lista de órdenes
    return render(request, 'orders/order_list.html')