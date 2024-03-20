from rest_framework import generics

from .models import EmployeeCard, CV, EmployeePassport, EmployerPassport, Order, Proposal, Job, JobAppeal, \
    EmployeeReview, EmployerReview, Payment, PaymentAppeal
from .serializers import EmployeeCardSerializer, CVSerializer, EmployeePassportSerializer, EmployerPassportSerializer, \
    OrderSerializer, ProposalSerializer, JobSerializer, JobAppealSerializer, EmployeeReviewSerializer, \
    EmployerReviewSerializer, PaymentSerializer, PaymentAppealSerializer


class EmployeeCardListCreate(generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class EmployeeCardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class CVListCreate(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class EmployeePassportListCreate(generics.ListCreateAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class EmployeePassportRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class EmployerPassportListCreate(generics.ListCreateAPIView):
    queryset = EmployerPassport.objects.all()
    serializer_class = EmployerPassportSerializer


class EmployerPassportRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerPassport.objects.all()
    serializer_class = EmployerPassportSerializer


class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProposalListCreate(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class ProposalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class JobListCreate(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobAppealListCreate(generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class JobAppealRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class EmployeeReviewListCreate(generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployeeReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployerReviewListCreate(generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class EmployerReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAppealListCreate(generics.ListCreateAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer


class PaymentAppealRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer
