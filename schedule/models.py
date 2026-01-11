from django.db import models


class Appointment(models.Model):
    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.PROTECT,
        related_name="appointments",
        verbose_name="Paciente",
    )

    professional = models.ForeignKey(
        "auth.User",
        on_delete=models.PROTECT,
        related_name="appointments",
        verbose_name="Profissional",
    )

    start_at = models.DateTimeField("Início")
    end_at = models.DateTimeField("Fim")

    title = models.CharField("Tipo/Descrição", max_length=200, blank=True, default="")
    notes = models.TextField("Observações", blank=True, default="")

    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agenda"
        ordering = ["-start_at"]

    def __str__(self):
        return f"{self.patient} - {self.professional} ({self.start_at:%d/%m %H:%M})"


