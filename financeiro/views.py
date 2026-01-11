from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from .models import Invoice, Payment

@login_required
def dashboard(request):
    total_open = Invoice.objects.filter(status="open").count()
    total_overdue = Invoice.objects.filter(status="overdue").count()
    total_paid = Invoice.objects.filter(status="paid").count()

    received = Payment.objects.aggregate(total=Sum("amount"))["total"] or 0

    return render(request, "financeiro/dashboard.html", {
        "total_open": total_open,
        "total_overdue": total_overdue,
        "total_paid": total_paid,
        "received": received,
    })


@login_required
def invoice_list(request):
    qs = Invoice.objects.all().order_by("-created_at")

    status = request.GET.get("status", "").strip()
    q = request.GET.get("q", "").strip()

    if status:
        qs = qs.filter(status=status)

    if q:
        qs = qs.filter(patient_name__icontains=q)

    return render(request, "financeiro/invoice_list.html", {
        "invoices": qs,
        "status": status,
        "q": q,
    })

