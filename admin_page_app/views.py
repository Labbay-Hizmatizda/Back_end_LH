from rest_framework import generics

from .serializers import *


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployeeCardListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class EmployeeCardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class CVListCreateAPIView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class EmployeePassportListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class EmployeePassportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProposalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proposals.objects.all()
    serializer_class = ProposalSerializer


class ProposalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proposals.objects.all()
    serializer_class = ProposalSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class JobAppealRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class EmployeeReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployeeReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployerReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class EmployerReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer


class PaymentAppealRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer
