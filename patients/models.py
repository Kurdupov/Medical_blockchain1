# patients/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import create_blockchain_record

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255)
    visit_date = models.DateField()
    analysis_results = models.TextField()
    blockchain_hash = models.CharField(max_length=64, blank=True, null=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient} - {self.diagnosis}'

class MedicalRecordHashHistory(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    blockchain_hash = models.CharField(max_length=64)

    def __str__(self):
        return f'Хеш истории для {self.medical_record} от {self.timestamp}'

@receiver(post_save, sender=MedicalRecord)
def update_blockchain_chain(sender, instance, **kwargs):
    # Получаем все записи пациента в правильном порядке
    records = MedicalRecord.objects.filter(patient=instance.patient).order_by('visit_date', 'id')

    previous_hash = ''
    for record in records:
        new_hash = create_blockchain_record(
            record.patient.id,
            record.diagnosis,
            record.visit_date,
            record.analysis_results,
            previous_hash
        )
        if record.blockchain_hash != new_hash:
            # Сохраняем старый хеш в историю перед обновлением
            if record.blockchain_hash:
                MedicalRecordHashHistory.objects.create(
                    medical_record=record,
                    blockchain_hash=record.blockchain_hash
                )
            # Обновляем хеш записи
            MedicalRecord.objects.filter(pk=record.pk).update(blockchain_hash=new_hash)
        previous_hash = new_hash
