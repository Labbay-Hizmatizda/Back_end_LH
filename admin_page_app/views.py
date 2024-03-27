from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Employee, Employer, EmployeeCard, CV, EmployeePassport, Order, Proposal, Job, JobAppeal, \
    EmployeeReview, EmployerReview, Payment, PaymentAppeal
from .serializers import EmployeeSerializer, EmployerSerializer, EmployeeCardSerializer, CvSerializer, \
    EmployeePassportSerializer, OrderSerializer, ProposalSerializer, JobSerializer, JobAppealSerializer, \
    EmployeeReviewSerializer, EmployerReviewSerializer, PaymentSerializer, PaymentAppealSerializer


class FilterMixin:
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtratsiya uchun parametrlarni olish
        name = self.request.query_params.get('name', None)
        surname = self.request.query_params.get('surname', None)
        location = self.request.query_params.get('location', None)

        # Agar name berilgan bo'lsa, nomga qarab filtratsiya qilish
        if name:
            queryset = queryset.filter(name__icontains=name)

        # Agar surname berilgan bo'lsa, familiyaga qarab filtratsiya qilish
        if surname:
            queryset = queryset.filter(surname__icontains=surname)

        # Agar location berilgan bo'lsa, joylashuvga qarab filtratsiya qilish
        if hasattr(self.queryset.model, 'location') and location:
            queryset = queryset.filter(location__icontains=location)

        return queryset


class EmployeeListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployerListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployerDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class EmployeeCardListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class EmployeeCardDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeCard.objects.all()
    serializer_class = EmployeeCardSerializer


class CVListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CvSerializer


class CVDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CvSerializer


class EmployeePassportListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class EmployeePassportDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeePassport.objects.all()
    serializer_class = EmployeePassportSerializer


class OrderListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProposalListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class ProposalDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class JobListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobAppealListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class JobAppealDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = JobAppeal.objects.all()
    serializer_class = JobAppealSerializer


class EmployeeReviewListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployeeReviewDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeReview.objects.all()
    serializer_class = EmployeeReviewSerializer


class EmployerReviewListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class EmployerReviewDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerReview.objects.all()
    serializer_class = EmployerReviewSerializer


class PaymentListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentAppealListCreateAPIView(FilterMixin, generics.ListCreateAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer


class PaymentAppealDetailAPIView(FilterMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentAppeal.objects.all()
    serializer_class = PaymentAppealSerializer
