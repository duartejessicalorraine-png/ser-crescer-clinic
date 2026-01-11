from django.db import models
from django.utils import timezone

class ServiceType(models.Model):
    """
    Tipo de atendimento (ex: ABA 1h, Neuropsico, Fono, Supervisão, etc.)
    """
    name = models.CharField(max_length=120)
    default_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration_minutes = models.PositiveIntegerField(default=60)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """
    Fatura para um paciente/responsável (mensalidade, pacote, sessões avulsas)
    """
    STATUS_CHOICES = [
        ("open", "Aberta"),
        ("paid", "Paga"),
        ("overdue", "Vencida"),
        ("canceled", "Cancelada"),
    ]

    patient_name = models.CharField(max_length=160)
    responsible_name = models.CharField(max_length=160, blank=True)
    responsible_whatsapp = models.CharField(max_length=30, blank=True)

    description = models.CharField(max_length=200, blank=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fatura #{self.id} - {self.patient_name} - {self.get_status_display()}"


class Payment(models.Model):
    """
    Pagamento (parcial ou total) vinculado a uma fatura
    """
    METHOD_CHOICES = [
        ("pix", "PIX"),
        ("cash", "Dinheiro"),
        ("card", "Cartão"),
        ("transfer", "Transferência"),
        ("other", "Outro"),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    paid_at = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES, default="pix")
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Pagamento #{self.id} - {self.amount} ({self.get_method_display()})"

