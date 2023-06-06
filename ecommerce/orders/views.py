from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order, OrderItem


@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        serializer = OrderSerializer(order)
        return Response({"message: orders created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order_dict = {
            "user": order.user,
            "status": order.status,
            "created_at": order.created_at,
            "updated_at": order.updated_at
        }
        items = OrderItem.objects.filter(order=order)
        order_dict['items'] = items
        serializer = OrderSerializer(order_dict)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.status = request.data.get('status', order.status)
        order.save()
        serializer = OrderSerializer(order)
        return Response({"message: orders updated successfully"})
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_orders(request):
    data_list = []
    orders = Order.objects.all()
    for order in orders:
        order_dict = {
            "user": order.user,
            "status": order.status,
            "created_at": order.created_at,
            "updated_at": order.updated_at
        }
        items = OrderItem.objects.filter(order=order)
        order_dict['items'] = items
        data_list.append(order_dict)
    serializer = OrderSerializer(data_list, many=True)
    return Response(serializer.data)