from django.contrib.postgres.fields import ArrayField  # pragma: no cover
from django.db import models  # pragma: no cover
from django.db.models.signals import post_save  # pragma: no cover
from django.dispatch import receiver  # pragma: no cover

from dna_api.dna.services import DNAService  # pragma: no cover


class DNA(models.Model):  # pragma: no cover
    dna = ArrayField(  # pragma: no cover
        models.CharField(max_length=6),  # pragma: no cover
    )  # pragma: no cover
    is_mutant = models.BooleanField()  # pragma: no cover

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.is_mutant = DNAService.is_mutant(self.dna)
        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )


class Status(models.Model):  # pragma: no cover
    count_mutant_dna = models.PositiveBigIntegerField(default=0)  # pragma: no cover
    count_human_dna = models.PositiveBigIntegerField(default=0)  # pragma: no cover
    ratio = models.FloatField(default=1)  # pragma: no cover

    @receiver(post_save, sender=DNA)
    def update_status(sender, instance, *args, **kwargs):
        status = Status.objects.first()
        if not status:
            status = Status(count_mutant_dna=0, count_human_dna=0)

        status.count_human_dna += 1
        if instance.is_mutant:
            status.count_mutant_dna += 1

        status.ratio = status.count_mutant_dna / status.count_human_dna
        status.save()
