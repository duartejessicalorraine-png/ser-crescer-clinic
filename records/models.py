from django.db import models


class SessionNote(models.Model):
    patient = models.ForeignKey(
        "patients.Patient",
        on_delete=models.PROTECT,
        related_name="session_notes",
        verbose_name="Paciente",
    )

    professional = models.ForeignKey(
        "auth.User",
        on_delete=models.PROTECT,
        related_name="session_notes",
        verbose_name="Profissional",
    )
    class SessionType(models.TextChoices):
        ABA = "ABA", "ABA"
        AT = "AT", "Acompanhante Terapêutico (AT)"
        FONO = "FONO", "Fonoaudiologia"
        PSICO = "PSICO", "Psicologia"
        PSICOPED = "PSICOPED", "Psicopedagogia"
        NEURO = "NEURO", "Neuropsicologia"
        OUTRO = "OUTRO", "Outro"

    session_type = models.CharField(
        "Tipo de sessão",
        max_length=20,
        choices=SessionType.choices,
        default=SessionType.ABA,
    )


    session_date = models.DateField("Data da sessão")
    start_time = models.TimeField("Hora início", blank=True, null=True)
    end_time = models.TimeField("Hora fim", blank=True, null=True)

    summary = models.TextField("Resumo / Evolução")
    plan_next = models.TextField("Plano para próxima sessão", blank=True, default="")
    family_guidance = models.TextField("Orientações para família", blank=True, default="")

    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Prontuário"
        verbose_name_plural = "Prontuários"
        ordering = ["-session_date", "-created_at"]

    def __str__(self):
        return f"{self.patient} - {self.session_date:%d/%m/%Y} ({self.professional})"


from django.conf import settings  # se já tiver no topo, NÃO repete

class SessionAttachment(models.Model):
    """
    Anexo vinculado a um prontuário (SessionNote).
    Aceita PDF, imagens, docs etc.
    """
    note = models.ForeignKey(
        "records.SessionNote",
        on_delete=models.CASCADE,
        related_name="attachments",
        verbose_name="Prontuário",
    )

    title = models.CharField("Título", max_length=120, blank=True, default="")
    description = models.TextField("Descrição", blank=True, default="")

    file = models.FileField("Arquivo", upload_to="records/attachments/%Y/%m/")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="uploaded_attachments",
        verbose_name="Enviado por",
    )

    uploaded_at = models.DateTimeField("Enviado em", auto_now_add=True)

    class Meta:
        verbose_name = "Anexo do prontuário"
        verbose_name_plural = "Anexos do prontuário"
        ordering = ["-uploaded_at"]

    def __str__(self):
        name = self.title.strip() or "Anexo"
        return f"{name} • {self.note.patient} • {self.uploaded_at:%d/%m/%Y}"



