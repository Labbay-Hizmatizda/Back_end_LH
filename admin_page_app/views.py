# views.py
from rest_framework import generics

from .models import Employee, Employer, Order, Proposal, Job, JobAppeal, EmployeeReview, EmployerReview, Payment, \
    PaymentAppeal, EmployeePassport
from .serializers import EmployeeSerializer, EmployerSerializer, EmployeePassportSerializer, OrderSerializer, \
    ProposalSerializer, JobSerializer, JobAppealSerializer, EmployeeReviewSerializer, EmployerReviewSerializer, \
    PaymentSerializer, PaymentAppealSerializer


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployeePassportListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class EmployeePassportDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProposalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class ProposalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class JobAppealDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class EmployeeReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployeeReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployerReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class EmployerReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer


class PaymentAppealDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer
