from django.db import models


class Patient(models.Model):
    full_name = models.CharField("Nome completo", max_length=200)
    birth_date = models.DateField("Data de nascimento", null=True, blank=True)

    guardian_name = models.CharField("Responsável", max_length=200, blank=True, default="")
    guardian_phone = models.CharField("Telefone do responsável", max_length=30, blank=True, default="")

    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name

