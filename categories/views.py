from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        # 다수의 객체 정보를 직렬화 하기 위해 many 인자 전달
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # POST 데이터를 시리얼라이저에 전달
        serializer = CategorySerializer(data=request.data)
        # User Input 검증
        print(serializer.is_valid())
        if serializer.is_valid():
            return Response(
                {
                    "created": True,
                }
            )
        else:
            return serializer.errors


@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)
