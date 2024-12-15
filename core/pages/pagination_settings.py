from rest_framework.pagination import PageNumberPagination


class ClassicPagination(PageNumberPagination):
    page_size = 6


class MiniPagination(PageNumberPagination):
    page_size = 3
