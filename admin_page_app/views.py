from rest_framework import generics

from .serializers import *


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

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


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

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


class EmployeeCardListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        holder_name = self.request.query_params.get('holder_name', None)
        id = self.request.query_params.get('id', None)

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


class CVListCreateAPIView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

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


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get('owner_id', None)
        category = self.request.query_params.get('category', None)
        price = self.request.query_params.get('price', None)
        id = self.request.query_params.get('id', None)

        if id:
            queryset = queryset.filter(id=id)
        if owner_id:
            queryset = queryset.filter(owner_id=owner_id)
        if category:
            queryset = queryset.filter(category=category)
        if price:
            queryset = queryset.filter(price=price)

        return queryset


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProposalsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proposals.objects.all()
    serializer_class = ProposalsSerializer

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


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

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


class JobAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer

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


class EmployeeReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer

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


class EmployerReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer

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


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguagesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer
