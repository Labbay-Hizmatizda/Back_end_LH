from rest_framework import generics

from .paginations import NumberPagination, PageNumberPagination
from .serializers import *


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id', None)
        user_id = self.request.query_params.get('user_id', None)
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        phone_number = self.request.query_params.get('phone_number', None)

        if id:
            queryset = queryset.filter(id=id)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if name:
            queryset = queryset.filter(name=name)
        if surname:
            queryset = queryset.filter(surname=surname)
        if phone_number:
            queryset = queryset.filter(phone_number=phone_number)
        return queryset


class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    pagination_class = NumberPagination


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id', None)
        user_id = self.request.query_params.get('user_id', None)
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        phone_number = self.request.query_params.get('phone_number', None)

        if id:
            queryset = queryset.filter(id=id)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if name:
            queryset = queryset.filter(name=name)
        if surname:
            queryset = queryset.filter(surname=surname)
        if phone_number:
            queryset = queryset.filter(phone_number=phone_number)

        return queryset


class EmployerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    lookup_field = 'pk'
    pagination_class = NumberPagination


class EmployeeCardListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        holder_name = self.request.query_params.get('holder_name', None)
        id = self.request.query_params.get('id', None)
        page_si

        paginator = self.django_paginator_class(queryset, )

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if holder_name:
            queryset = queryset.filter(holder_name=holder_name)

        return queryset


class EmployeeCardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer
    lookup_field = 'pk'
    pagination_class = NumberPagination


class CVListCreateAPIView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        rating = self.request.query_params.get('rating', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if rating:
            queryset = queryset.filter(rating=rating)

        return queryset


class CVRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    lookup_field = 'pk'
    pagination_class = NumberPagination


class EmployeePassportListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)

        return queryset


class EmployeePassportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer
    lookup_field = 'pk'
    pagination_class = NumberPagination


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        id = self.request.query_params.get('id')
        price = self.request.query_params.get('price')
        owner_id = self.request.query_params.get('owner_id')

        if id:
            queryset = queryset.filter(id=id)
        if price:
            queryset = queryset.filter(price=price)
        if owner_id:
            queryset = queryset.filter(owner__id=owner_id)

        category_name = self.request.query_params.get('category_name')

        if category_name:
            queryset = queryset.filter(category__name=category_name)

        return queryset


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = NumberPagination


class ProposalsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proposals.objects.all()
    serializer_class = ProposalsSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        order_id = self.request.query_params.get('order_id', None)
        price = self.request.query_params.get('price', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if price:
            queryset = queryset.filter(price=price)
        if order_id:
            queryset = queryset.filter(order_id=order_id)

        return queryset


class ProposalsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proposals.objects.all()
    serializer_class = ProposalsSerializer
    pagination_class = NumberPagination


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        order_id = self.request.query_params.get('order_id', None)
        proposal_id = self.request.query_params.get('proposal_id', None)
        price = self.request.query_params.get('price', None)
        rating = self.request.query_params.get('rating', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if order_id:
            queryset = queryset.filter(owner_id=order_id)
        if proposal_id:
            queryset = queryset.filter(proposal_id=proposal_id)
        if price:
            queryset = queryset.filter(price=price)
        if rating:
            queryset = queryset.filter(rating=rating)

        return queryset


class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    pagination_class = NumberPagination


class JobAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        order_id = self.request.query_params.get('order_id', None)
        price = self.request.query_params.get('price', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if price:
            queryset = queryset.filter(price=price)
        if order_id:
            queryset = queryset.filter(order_id=order_id)

        return queryset


class JobAppealRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer
    pagination_class = NumberPagination


class EmployeeReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        job_id = self.request.query_params.get('job_id', None)
        owner_id = self.request.query_params.get('owner_id', None)
        employer_id = self.request.query_params.get('employer_id', None)
        rate = self.request.query_params.get('rate', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if job_id:
            queryset = queryset.filter(job_id=job_id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if employer_id:
            queryset = queryset.filter(employer_id=employer_id)
        if rate:
            queryset = queryset.filter(rate=rate)

        return queryset


class EmployeeReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer
    pagination_class = NumberPagination


class EmployerReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer
    pagination_class = NumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        job_id = self.request.query_params.get('job_id', None)
        owner_id = self.request.query_params.get('owner_id', None)
        employer_id = self.request.query_params.get('employer_id', None)
        rate = self.request.query_params.get('rate', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if job_id:
            queryset = queryset.filter(job_id=job_id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if employer_id:
            queryset = queryset.filter(employer_id=employer_id)
        if rate:
            queryset = queryset.filter(rate=rate)

        return queryset


class EmployerReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        job_id = self.request.query_params.get('job_id', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if job_id:
            queryset = queryset.filter(job_id=job_id)

        return queryset


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)

        return queryset


class PaymentAppealRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer
    pagination_class = NumberPagination


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = NumberPagination


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = NumberPagination


class LanguagesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
    pagination_class = NumberPagination
