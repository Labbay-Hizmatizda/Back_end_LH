from rest_framework import generics

from .models import Employee, Employer, EmployeeCard, CV, EmployeePassport, Order, Proposal, Job, JobAppeal, \
    EmployeeReview, EmployerReview, Payment, PaymentAppeal
from .serializers import EmployeeSerializer, EmployerSerializer, EmployeeCardSerializer, CvSerializer, \
    EmployeePassportSerializer, OrderSerializer, ProposalSerializer, JobSerializer, JobAppealSerializer, \
    EmployeeReviewSerializer, EmployerReviewSerializer, PaymentSerializer, PaymentAppealSerializer



class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id', None)
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        phone_number = self.request.query_params.get('phone_number', None)

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


class EmployerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployeeCardListCreateAPIView(generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class EmployeeCardDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class CVListCreateAPIView(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CvSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.query_params.get('owner', None)
        rating = self.request.query_params.get('rating', None)
        rating = self.request.query_params.get('rating', None)


        if owner:
            queryset = queryset.filter(owner=owner)
        if rating:
            queryset = queryset.filter(rating=rating)

        return queryset


class CVDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CvSerializer


class EmployeePassportListCreateAPIView( generics.ListCreateAPIView):
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


class EmployeeReviewListCreateAPIView( generics.ListCreateAPIView):
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
