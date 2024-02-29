# main/views.py

from rest_framework import generics

from .models import (
    Employee,
    Employer,
    EmployeeCard,
    CV,
    EmployeePassport,
    EmployerPassport,
    Order,
    Proposal,
    Job,
    JobAppeal,
    EmployeeReview,
    EmployerReview,
    Payment,
    PaymentAppeal,
)
from .serializers import (
    EmployeeSerializer,
    EmployerSerializer,
    EmployeeCardSerializer,
    CVSerializer,
    EmployeePassportSerializer,
    EmployerPassportSerializer,
    OrderSerializer,
    ProposalSerializer,
    JobSerializer,
    JobAppealSerializer,
    EmployeeReviewSerializer,
    EmployerReviewSerializer,
    PaymentSerializer,
    PaymentAppealSerializer,
)


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployerListView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer



class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployeeCardListView(generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class CVListView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class EmployeePassportListView(generics.ListCreateAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class EmployerPassportListView(generics.ListCreateAPIView):
    queryset = EmployerPassport.objects.all()
    serializer_class = EmployerPassportSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProposalListView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobAppealListView(generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class EmployeeReviewListView(generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployerReviewListView(generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class PaymentListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAppealListView(generics.ListCreateAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer
