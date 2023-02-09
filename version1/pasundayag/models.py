from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("pasundayag:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class Status(models.Model):
    """
    IPCRType Table will provide a list of the different types
    of ipcrs that are for sale.
    """

    name = models.CharField(verbose_name=_("IPCR Name"), help_text=_("Required"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Status")

    def __str__(self):
        return self.name


class IPCRSpecification(models.Model):
    """
    The IPCR Specification Table contains ipcr
    specifiction or features for the ipcr status.
    """

    ipcr_type = models.ForeignKey(Status, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("IPCR Specification")
        verbose_name_plural = _("IPCR Specifications")

    def __str__(self):
        return self.name



class IPCR(models.Model):
    """
    The IPCR table contining all ipcr items.
    """

    status = models.ForeignKey(Status, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_("name"),
        help_text=_("Required"),
        max_length=255,
    )

    slug = models.SlugField(max_length=255)

    is_active = models.BooleanField(
        verbose_name=_("IPCR visibility"),
        help_text=_("Change ipcr visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    stra_percentage = models.CharField(verbose_name=_("Strategic Function Adjectival Rating"), max_length=255, default="")

    stra_mfo_pap_1 =  models.TextField(verbose_name=_("MFO/PAP row 1"), blank=True)
    stra_sucess_indicators_1 =  models.TextField(verbose_name=_("Sucess Indecator row 1"), blank=True) 
    stra_actual_accomplishment_indicators_1 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q1 = models.DecimalField(verbose_name=_("Quality rating row 1"),max_digits=5, decimal_places=4, null=True)
    stra_e1 = models.DecimalField(verbose_name=_("Effeciency rating row 1"),max_digits=5, decimal_places=4, null=True)
    stra_t1 = models.DecimalField(verbose_name=_("Timelessness rating row 1"),max_digits=5, decimal_places=4, null=True)
    stra_a1 = models.DecimalField(verbose_name=_("Average rating row 1"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_2 =  models.TextField(verbose_name=_("MFO/PAP row 2"),  blank=True)
    stra_sucess_indicators_2 =  models.TextField(verbose_name=_("Sucess Indecator row 2"), blank=True) 
    stra_actual_accomplishment_indicators_2 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q2 = models.DecimalField(verbose_name=_("Quality rating row 2"),max_digits=5, decimal_places=4, null=True)
    stra_e2 = models.DecimalField(verbose_name=_("Effeciency rating row 2"),max_digits=5, decimal_places=4, null=True)
    stra_t2 = models.DecimalField(verbose_name=_("Timelessness rating row 2"),max_digits=5, decimal_places=4, null=True)
    stra_a2 = models.DecimalField(verbose_name=_("Average rating row 2"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_3 =  models.TextField(verbose_name=_("Stra MFO/PAP row 3"),  blank=True)
    stra_sucess_indicators_3 =  models.TextField(verbose_name=_("Sucess Indecator row 3"), blank=True) 
    stra_actual_accomplishment_indicators_3 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q3 = models.DecimalField(verbose_name=_("Quality rating row 3"),max_digits=5, decimal_places=4, null=True)
    stra_e3 = models.DecimalField(verbose_name=_("Effeciency rating row 3"),max_digits=5, decimal_places=4, null=True)
    stra_t3 = models.DecimalField(verbose_name=_("Timelessness rating row 3"),max_digits=5, decimal_places=4, null=True)
    stra_a3 = models.DecimalField(verbose_name=_("Average rating row 3"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_4 =  models.TextField(verbose_name=_("Stra MFO/PAP row 4"),  blank=True)
    stra_sucess_indicators_4 =  models.TextField(verbose_name=_("Sucess Indecator row 4"), blank=True) 
    stra_actual_accomplishment_indicators_4 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q4 = models.DecimalField(verbose_name=_("Quality rating row 4"),max_digits=5, decimal_places=4, null=True)
    stra_e4 = models.DecimalField(verbose_name=_("Effeciency rating row 4"),max_digits=5, decimal_places=4, null=True)
    stra_t4 = models.DecimalField(verbose_name=_("Timelessness rating row 4"),max_digits=5, decimal_places=4, null=True)
    stra_a4 = models.DecimalField(verbose_name=_("Average rating row 4"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_5 =  models.TextField(verbose_name=_("Stra MFO/PAP row 5"),  blank=True)
    stra_sucess_indicators_5 =  models.TextField(verbose_name=_("Sucess Indecator row 5"), blank=True) 
    stra_actual_accomplishment_indicators_5 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q5 = models.DecimalField(verbose_name=_("Quality rating row 5"),max_digits=5, decimal_places=4, null=True)
    stra_e5 = models.DecimalField(verbose_name=_("Effeciency rating row 5"),max_digits=5, decimal_places=4, null=True)
    stra_t5 = models.DecimalField(verbose_name=_("Timelessness rating row 5"),max_digits=5, decimal_places=4, null=True)
    stra_a5 = models.DecimalField(verbose_name=_("Average rating row 5"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_6 =  models.TextField(verbose_name=_("Stra MFO/PAP row 6"),  blank=True)
    stra_sucess_indicators_6 =  models.TextField(verbose_name=_("Sucess Indecator row 6"), blank=True) 
    stra_actual_accomplishment_indicators_6 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q6 = models.DecimalField(verbose_name=_("Quality rating row 6"),max_digits=5, decimal_places=4, null=True)
    stra_e6 = models.DecimalField(verbose_name=_("Effeciency rating row 6"),max_digits=5, decimal_places=4, null=True)
    stra_t6 = models.DecimalField(verbose_name=_("Timelessness rating row 6"),max_digits=5, decimal_places=4, null=True)
    stra_a6 = models.DecimalField(verbose_name=_("Average rating row 6"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_7 =  models.TextField(verbose_name=_("Stra MFO/PAP row 7"),  blank=True)
    stra_sucess_indicators_7 =  models.TextField(verbose_name=_("Sucess Indecator row 7"), blank=True) 
    stra_actual_accomplishment_indicators_7 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q7 = models.DecimalField(verbose_name=_("Quality rating row 7"),max_digits=5, decimal_places=4, null=True)
    stra_e7 = models.DecimalField(verbose_name=_("Effeciency rating row 7"),max_digits=5, decimal_places=4, null=True)
    stra_t7 = models.DecimalField(verbose_name=_("Timelessness rating row 7"),max_digits=5, decimal_places=4, null=True)
    stra_a7 = models.DecimalField(verbose_name=_("Average rating row 7"),max_digits=5, decimal_places=4, null=True)

    stra_mfo_pap_8 =  models.TextField(verbose_name=_("Stra MFO/PAP row 8"),  blank=True)
    stra_sucess_indicators_8 =  models.TextField(verbose_name=_("Sucess Indecator row 8"), blank=True) 
    stra_actual_accomplishment_indicators_8 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    stra_q8 = models.DecimalField(verbose_name=_("Quality rating row 8"),max_digits=5, decimal_places=4, null=True)
    stra_e8 = models.DecimalField(verbose_name=_("Effeciency rating row 8"),max_digits=5, decimal_places=4, null=True)
    stra_t8 = models.DecimalField(verbose_name=_("Timelessness rating row 8"),max_digits=5, decimal_places=4, null=True)
    stra_a8 = models.DecimalField(verbose_name=_("Average rating row 8"),max_digits=5, decimal_places=4, null=True)

    stra_total = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    stra_adjectival_rating = models.CharField(
        verbose_name=_("Strategic Function Adjectival Rating"), max_length=255, default="Poor"
    )


    core_percentage = models.CharField(
        verbose_name=_("Strategic Function Adjectival Rating"), max_length=255, default="Poor"
    )

    core_acad_mfo_pap_1 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_indicators_1 =  models.TextField(verbose_name=_("Success Indeiator row 1"),  blank=True)
    core_acad_actual_accomplishment_indicators_1 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)  
    core_acad_q1 = models.DecimalField(verbose_name=_("Quality rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_acad_e1 = models.DecimalField(verbose_name=_("Effeciency rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_acad_t1 = models.DecimalField(verbose_name=_("Timelessness rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_acad_a1 = models.DecimalField(verbose_name=_("Average rating row 1"),max_digits=5, decimal_places=4, null=True)

    mfo_acad_mfo_pap_2 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_2 =  models.TextField(verbose_name=_("Success Indeiator row 2"),  blank=True) 
    core_acad_actual_accomplishment_indicators_2 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_acad_q2 = models.DecimalField(verbose_name=_("Quality rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_acad_e2 = models.DecimalField(verbose_name=_("Effeciency rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_acad_t2 = models.DecimalField(verbose_name=_("Timelessness rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_acad_a2 = models.DecimalField(verbose_name=_("Average rating row 2"),max_digits=5, decimal_places=4, null=True)

    mfo_acad_mfo_pap_3 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_3 =  models.TextField(verbose_name=_("Success Indeiator row 3"),  blank=True) 
    core_acad_actual_accomplishment_indicators_3 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_acad_q3 = models.DecimalField(verbose_name=_("Quality rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_acad_e3 = models.DecimalField(verbose_name=_("Effeciency rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_acad_t3 = models.DecimalField(verbose_name=_("Timelessness rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_acad_a3 = models.DecimalField(verbose_name=_("Average rating row 3"),max_digits=5, decimal_places=4, null=True)

    mfo_acad_mfo_pap_4 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_acad_sucess_indicators_4 =  models.TextField(verbose_name=_("Success Indeiator row 4"),  blank=True)
    core_actual_accomplishment_indicators_4 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    core_acad_q4 = models.DecimalField(verbose_name=_("Quality rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_acad_e4 = models.DecimalField(verbose_name=_("Effeciency rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_acad_t4 = models.DecimalField(verbose_name=_("Timelessness rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_acad_a4 = models.DecimalField(verbose_name=_("Average rating row 4"),max_digits=5, decimal_places=4, null=True)

    core_acad_mfo_pap_5 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_5 =  models.TextField(verbose_name=_("Success Indeiator row 5"),  blank=True)
    core_acad_actual_accomplishment_indicators_5 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    core_acad_q5 = models.DecimalField(verbose_name=_("Quality rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_acad_e5 = models.DecimalField(verbose_name=_("Effeciency rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_acad_t5 = models.DecimalField(verbose_name=_("Timelessness rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_acad_a5 = models.DecimalField(verbose_name=_("Average rating row 5"),max_digits=5, decimal_places=4, null=True)

    core_acad_mfo_pap_6 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_6 =  models.TextField(verbose_name=_("Success Indeiator row 6"),  blank=True)
    core_acad_actual_accomplishment_indicators_6 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    core_acad_q6 = models.DecimalField(verbose_name=_("Quality rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_acad_e6 = models.DecimalField(verbose_name=_("Effeciency rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_acad_t6 = models.DecimalField(verbose_name=_("Timelessness rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_acad_a6 = models.DecimalField(verbose_name=_("Average rating row 6"),max_digits=5, decimal_places=4, null=True)

    core_acad_mfo_pap_7 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_7 =  models.TextField(verbose_name=_("Success Indeiator row 7"),  blank=True)
    core_acad_actual_accomplishment_indicators_7 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    core_acad_q7 = models.DecimalField(verbose_name=_("Quality rating row 7"),max_digits=5, decimal_places=4, null=True)
    core_acad_e7 = models.DecimalField(verbose_name=_("Effeciency rating row 7"),max_digits=5, decimal_places=4, null=True)
    core_acad_t7 = models.DecimalField(verbose_name=_("Timelessness rating row 7"),max_digits=5, decimal_places=4, null=True)
    core_acad_a7 = models.DecimalField(verbose_name=_("Average rating row 7"),max_digits=5, decimal_places=4, null=True)

    core_acad_mfo_pap_8 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_8 =  models.TextField(verbose_name=_("Success Indeiator row 8"),  blank=True) 
    core_acad_actual_accomplishment_indicators_8 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_acad_q8 = models.DecimalField(verbose_name=_("Quality rating row 8"),max_digits=5, decimal_places=4, null=True)
    core_acad_e8 = models.DecimalField(verbose_name=_("Effeciency rating row 8"),max_digits=5, decimal_places=4, null=True)
    core_acad_t8 = models.DecimalField(verbose_name=_("Timelessness rating row 8"),max_digits=5, decimal_places=4, null=True)
    core_acad_a8 = models.DecimalField(verbose_name=_("Average rating row 8"),max_digits=5, decimal_places=4, null=True)

    core_mfo_pap_9 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_9 =  models.TextField(verbose_name=_("Success Indeiator row 9"),  blank=True) 
    core_acad_actual_accomplishment_indicators_9 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_acad_q9 = models.DecimalField(verbose_name=_("Quality rating row 9"),max_digits=5, decimal_places=4, null=True)
    core_acad_e9 = models.DecimalField(verbose_name=_("Effeciency rating row 9"),max_digits=5, decimal_places=4, null=True)
    core_acad_t9 = models.DecimalField(verbose_name=_("Timelessness rating row 9"),max_digits=5, decimal_places=4, null=True)
    core_acad_a9 = models.DecimalField(verbose_name=_("Average rating row 9"),max_digits=5, decimal_places=4, null=True)

    core_acad_mfo_pap_10 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_acad_sucess_indicators_10 =  models.TextField(verbose_name=_("Success Indeiator row 10"),  blank=True) 
    core_acad_actual_accomplishment_indicators_10 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_acad_q10 = models.DecimalField(verbose_name=_("Quality rating row 10"),max_digits=5, decimal_places=4, null=True)
    core_acad_e10 = models.DecimalField(verbose_name=_("Effeciency rating row 10"),max_digits=5, decimal_places=4, null=True)
    core_acad_t10 = models.DecimalField(verbose_name=_("Timelessness rating row 10"),max_digits=5, decimal_places=4, null=True)
    core_acad_a10 = models.DecimalField(verbose_name=_("Average rating row 10"),max_digits=5, decimal_places=4, null=True)

    core_acad_total = models.DecimalField(verbose_name=_("Average rating row 9"),max_digits=5, decimal_places=4, null=True)

    core_irp_pap_1 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_irp_indicators_1 =  models.TextField(verbose_name=_("Success Indeiator row 1"),  blank=True) 
    core_irp_actual_accomplishment_indicators_1 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_irp_q1 = models.DecimalField(verbose_name=_("Quality rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_irp_e1 = models.DecimalField(verbose_name=_("Effeciency rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_irp_t1 = models.DecimalField(verbose_name=_("Timelessness rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_irp_a1 = models.DecimalField(verbose_name=_("Average rating row 1"),max_digits=5, decimal_places=4, null=True)

    mfo_irp_pap_2 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_irp_sucess_indicators_2 =  models.TextField(verbose_name=_("Success Indeiator row 2"),  blank=True) 
    core_irp_actual_accomplishment_indicators_2 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_irp_q2 = models.DecimalField(verbose_name=_("Quality rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_irp_e2 = models.DecimalField(verbose_name=_("Effeciency rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_irp_t2 = models.DecimalField(verbose_name=_("Timelessness rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_irp_a2 = models.DecimalField(verbose_name=_("Average rating row 2"),max_digits=5, decimal_places=4, null=True)

    mfo_irp_pap_3 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_irp_sucess_indicators_3 =  models.TextField(verbose_name=_("Success Indeiator row 3"),  blank=True) 
    core_irp_actual_accomplishment_indicators_3 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_irp_q3 = models.DecimalField(verbose_name=_("Quality rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_irp_e3 = models.DecimalField(verbose_name=_("Effeciency rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_irp_t3 = models.DecimalField(verbose_name=_("Timelessness rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_irp_a3 = models.DecimalField(verbose_name=_("Average rating row 3"),max_digits=5, decimal_places=4, null=True)

    mfo_irp_pap_4 =  models.TextField(verbose_name=_("dMFO/PAP row"),  blank=True)
    core_irp_sucess_indicators_4 =  models.TextField(verbose_name=_("Success Indeiator row 4"),  blank=True) 
    core_irp_actual_accomplishment_indicators_4 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_irp_q4 = models.DecimalField(verbose_name=_("Quality rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_irp_e4 = models.DecimalField(verbose_name=_("Effeciency rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_irp_t4 = models.DecimalField(verbose_name=_("Timelessness rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_irp_a4 = models.DecimalField(verbose_name=_("Average rating row 4"),max_digits=5, decimal_places=4, null=True)

    core_irp_mfo_pap_5 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_irp_sucess_indicators_5 =  models.TextField(verbose_name=_("Success Indeiator row 5"),  blank=True) 
    core_irp_actual_accomplishment_indicators_5 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_irp_q5 = models.DecimalField(verbose_name=_("Quality rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_irp_e5 = models.DecimalField(verbose_name=_("Effeciency rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_irp_t5 = models.DecimalField(verbose_name=_("Timelessness rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_irp_a5 = models.DecimalField(verbose_name=_("Average rating row 5"),max_digits=5, decimal_places=4, null=True)

    core_irp_mfo_pap_6 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_irp_sucess_indicators_6 =  models.TextField(verbose_name=_("Success Indeiator row 6"),  blank=True) 
    core_irp_actual_accomplishment_indicators_6 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_irp_q6 = models.DecimalField(verbose_name=_("Quality rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_irp_e6 = models.DecimalField(verbose_name=_("Effeciency rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_irp_t6 = models.DecimalField(verbose_name=_("Timelessness rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_irp_a6 = models.DecimalField(verbose_name=_("Average rating row 6"),max_digits=5, decimal_places=4, null=True)

    core_irp_total = models.DecimalField(verbose_name=_("Improving Research Productivity Average"),max_digits=5, decimal_places=4, null=True)

    core_tae_pap_1 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_tae_indicators_1 =  models.TextField(verbose_name=_("Success Indeiator row 1"),  blank=True) 
    core_tae_actual_accomplishment_indicators_1 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_tae_q1 = models.DecimalField(verbose_name=_("Quality rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_tae_e1 = models.DecimalField(verbose_name=_("Effeciency rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_tae_t1 = models.DecimalField(verbose_name=_("Timelessness rating row 1"),max_digits=5, decimal_places=4, null=True)
    core_tae_a1 = models.DecimalField(verbose_name=_("Average rating row 1"),max_digits=5, decimal_places=4, null=True)

    mfo_tae_pap_2 =  models.TextField(verbose_name=_("Success Indeiator row"),  blank=True)
    core_tae_sucess_indicators_2 =  models.TextField(verbose_name=_("Success Indeiator row 2"),  blank=True) 
    core_tae_actual_accomplishment_indicators_2 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_tae_q2 = models.DecimalField(verbose_name=_("Quality rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_tae_e2 = models.DecimalField(verbose_name=_("Effeciency rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_tae_t2 = models.DecimalField(verbose_name=_("Timelessness rating row 2"),max_digits=5, decimal_places=4, null=True)
    core_tae_a2 = models.DecimalField(verbose_name=_("Average rating row 2"),max_digits=5, decimal_places=4, null=True)

    mfo_tae_pap_3 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_tae_sucess_indicators_3 =  models.TextField(verbose_name=_("Success Indeiator row 3"),  blank=True) 
    core_tae_actual_accomplishment_indicators_3 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_tae_q3 = models.DecimalField(verbose_name=_("Quality rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_tae_e3 = models.DecimalField(verbose_name=_("Effeciency rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_tae_t3 = models.DecimalField(verbose_name=_("Timelessness rating row 3"),max_digits=5, decimal_places=4, null=True)
    core_tae_a3 = models.DecimalField(verbose_name=_("Average rating row 3"),max_digits=5, decimal_places=4, null=True)

    mfo_tae_pap_4 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_tae_sucess_indicators_4 =  models.TextField(verbose_name=_("Success Indeiator row 4"),  blank=True)
    core_tae_actual_accomplishment_indicators_4 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True) 
    core_tae_q4 = models.DecimalField(verbose_name=_("Quality rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_tae_e4 = models.DecimalField(verbose_name=_("Effeciency rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_tae_t4 = models.DecimalField(verbose_name=_("Timelessness rating row 4"),max_digits=5, decimal_places=4, null=True)
    core_tae_a4 = models.DecimalField(verbose_name=_("Average rating row 4"),max_digits=5, decimal_places=4, null=True)

    core_tae_mfo_pap_5 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_tae_sucess_indicators_5 =  models.TextField(verbose_name=_("Success Indeiator row 5"),  blank=True) 
    core_tae_actual_accomplishment_indicators_5 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_tae_q5 = models.DecimalField(verbose_name=_("Quality rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_tae_e5 = models.DecimalField(verbose_name=_("Effeciency rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_tae_t5 = models.DecimalField(verbose_name=_("Timelessness rating row 5"),max_digits=5, decimal_places=4, null=True)
    core_tae_a5 = models.DecimalField(verbose_name=_("Average rating row 5"),max_digits=5, decimal_places=4, null=True)

    core_tae_mfo_pap_6 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_tae_sucess_indicators_6 =  models.TextField(verbose_name=_("Success Indeiator row 6"),  blank=True) 
    core_tae_actual_accomplishment_indicators_6 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_tae_q6 = models.DecimalField(verbose_name=_("Quality rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_tae_e6 = models.DecimalField(verbose_name=_("Effeciency rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_tae_t6 = models.DecimalField(verbose_name=_("Timelessness rating row 6"),max_digits=5, decimal_places=4, null=True)
    core_tae_a6 = models.DecimalField(verbose_name=_("Average rating row 6"),max_digits=5, decimal_places=4, null=True)

    core_tae_mfo_pap_7 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    core_tae_sucess_indicators_7 =  models.TextField(verbose_name=_("Success Indeiator row 7"),  blank=True) 
    core_tae_actual_accomplishment_indicators_7 =  models.TextField(verbose_name=_("Actual Accomplishment row"), blank=True)
    core_tae_q7 = models.DecimalField(verbose_name=_("Quality rating row 7"),max_digits=5, decimal_places=4, null=True)
    core_tae_e7 = models.DecimalField(verbose_name=_("Effeciency rating row 7"),max_digits=5, decimal_places=4, null=True)
    core_tae_t7 = models.DecimalField(verbose_name=_("Timelessness rating row 7"),max_digits=5, decimal_places=4, null=True)
    core_tae_a7 = models.DecimalField(verbose_name=_("Average rating row 7"),max_digits=5, decimal_places=4, null=True)

    core_tae_total = models.DecimalField(verbose_name=_("Improving Research Productivity Average"),max_digits=5, decimal_places=4, null=True)

    supp_percentage = models.CharField(
        verbose_name=_("supptegic Function Adjectival Rating"), max_length=255, default="Poor"
    )

    supp_mfo_pap_1 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    supp_sucess_indicators_1 =  models.TextField(verbose_name=_("Success Indeiator row 1"),  blank=True)
    supp_actual_accomplishment_indicators_1 =  models.TextField(verbose_name=_("Actual Accomplishment row 1"), blank=True) 
    supp_q1 = models.DecimalField(verbose_name=_("Quality rating row 1"),max_digits=5, decimal_places=4, null=True)
    supp_e1 = models.DecimalField(verbose_name=_("Effeciency rating row 1"),max_digits=5, decimal_places=4, null=True)
    supp_t1 = models.DecimalField(verbose_name=_("Timelessness rating row 1"),max_digits=5, decimal_places=4, null=True)
    supp_a1 = models.DecimalField(verbose_name=_("Average rating row 1"),max_digits=5, decimal_places=4, null=True)

    supp_mfo_pap_2 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    supp_sucess_indicators_2 =  models.TextField(verbose_name=_("Success Indeiator row 2"),  blank=True) 
    supp_actual_accomplishment_indicators_2 =  models.TextField(verbose_name=_("Actual Accomplishment row 2"), blank=True) 
    supp_q2 = models.DecimalField(verbose_name=_("Quality rating row 2"),max_digits=5, decimal_places=4, null=True)
    supp_e2 = models.DecimalField(verbose_name=_("Effeciency rating row 2"),max_digits=5, decimal_places=4, null=True)
    supp_t2 = models.DecimalField(verbose_name=_("Timelessness rating row 2"),max_digits=5, decimal_places=4, null=True)
    supp_a2 = models.DecimalField(verbose_name=_("Average rating row 2"),max_digits=5, decimal_places=4, null=True)

    supp_mfo_pap_3 =  models.TextField(verbose_name=_("Success Indeiator row"),  blank=True)
    supp_sucess_indicators_3 =  models.TextField(verbose_name=_("Success Indeiator row 3"),  blank=True) 
    supp_actual_accomplishment_indicators_3 =  models.TextField(verbose_name=_("Actual Accomplishment row 3"), blank=True) 
    supp_q3 = models.DecimalField(verbose_name=_("Quality rating row 3"),max_digits=5, decimal_places=4, null=True)
    supp_e3 = models.DecimalField(verbose_name=_("Effeciency rating row 3"),max_digits=5, decimal_places=4, null=True)
    supp_t3 = models.DecimalField(verbose_name=_("Timelessness rating row 3"),max_digits=5, decimal_places=4, null=True)
    supp_a3 = models.DecimalField(verbose_name=_("Average rating row 3"),max_digits=5, decimal_places=4, null=True)

    supp_mfo_pap_4 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    supp_sucess_indicators_4 =  models.TextField(verbose_name=_("Success Indeiator row 4"),  blank=True) 
    supp_actual_accomplishment_indicators_4 =  models.TextField(verbose_name=_("Actual Accomplishment row 4"), blank=True) 
    supp_q4 = models.DecimalField(verbose_name=_("Quality rating row 4"),max_digits=5, decimal_places=4, null=True)
    supp_e4 = models.DecimalField(verbose_name=_("Effeciency rating row 4"),max_digits=5, decimal_places=4, null=True)
    supp_t4 = models.DecimalField(verbose_name=_("Timelessness rating row 4"),max_digits=5, decimal_places=4, null=True)
    supp_a4 = models.DecimalField(verbose_name=_("Average rating row 4"),max_digits=5, decimal_places=4, null=True)

    supp_mfo_pap_5 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    supp_sucess_indicators_5 =  models.TextField(verbose_name=_("Success Indeiator row 5"),  blank=True) 
    supp_actual_accomplishment_indicators_5 =  models.TextField(verbose_name=_("Actual Accomplishment row 5"), blank=True) 
    supp_q5 = models.DecimalField(verbose_name=_("Quality rating row 5"),max_digits=5, decimal_places=4, null=True)
    supp_e5 = models.DecimalField(verbose_name=_("Effeciency rating row 5"),max_digits=5, decimal_places=4, null=True)
    supp_t5 = models.DecimalField(verbose_name=_("Timelessness rating row 5"),max_digits=5, decimal_places=4, null=True)
    supp_a5 = models.DecimalField(verbose_name=_("Average rating row 5"),max_digits=5, decimal_places=4, null=True)

    supp_mfo_pap_6 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    supp_sucess_indicators_6 =  models.TextField(verbose_name=_("Success Indeiator row 6"),  blank=True) 
    supp_actual_accomplishment_indicators_6 =  models.TextField(verbose_name=_("Actual Accomplishment row 6"), blank=True) 
    supp_q6 = models.DecimalField(verbose_name=_("Quality rating row 6"),max_digits=5, decimal_places=4, null=True)
    supp_e6 = models.DecimalField(verbose_name=_("Effeciency rating row 6"),max_digits=5, decimal_places=4, null=True)
    supp_t6 = models.DecimalField(verbose_name=_("Timelessness rating row 6"),max_digits=5, decimal_places=4, null=True)
    supp_a6 = models.DecimalField(verbose_name=_("Average rating row 6"),max_digits=5, decimal_places=4, null=True)

    supp_mfo_pap_7 =  models.TextField(verbose_name=_("MFO/PAP row"),  blank=True)
    supp_sucess_indicators_7 =  models.TextField(verbose_name=_("Success Indeiator row 7"),  blank=True) 
    supp_actual_accomplishment_indicators_7 =  models.TextField(verbose_name=_("Actual Accomplishment row 7"), blank=True) 
    supp_q7 = models.DecimalField(verbose_name=_("Quality rating row 7"),max_digits=5, decimal_places=4, null=True)
    supp_e7 = models.DecimalField(verbose_name=_("Effeciency rating row 7"),max_digits=5, decimal_places=4, null=True)
    supp_t7 = models.DecimalField(verbose_name=_("Timelessness rating row 7"),max_digits=5, decimal_places=4, null=True)
    supp_a7 = models.DecimalField(verbose_name=_("Average rating row 7"),max_digits=5, decimal_places=4, null=True)

    supp_total = models.DecimalField(max_digits=5, decimal_places=4, null=True)

    final_numerical_rating = models.DecimalField(verbose_name=_("Final Numerical Rating"), max_digits=5, decimal_places=4, null=True)
    final_adjectival_rating = models.CharField(
        verbose_name=_("Final Adjectival Rating"), max_length=255, default="Poor"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("IPCR")
        verbose_name_plural = _("IPCRs")

    def get_absolute_url(self):
        return reverse("pasundayag:ipcr_detail", args=[self.slug])

    def calculate_stra_total(self):
        self.stra_total = (self.stra_a1 + self.stra_a2 + self.stra_a3) / 3
        self.save()

    def calculate_core_total(self):
        core_total = (
            self.core_a1
            + self.core_a2
            + self.core_a3
            + self.core_a4
            + self.core_a5
            + self.core_a6
            + self.core_a7
            + self.core_a8
            + self.core_a9
            + self.core_a10
            + self.core_a11
            + self.core_a12
            + self.core_a13
            + self.core_a14
            + self.core_a15
            + self.core_a16
            + self.core_a17
            + self.core_a18
            + self.core_a19
        ) / 19
        self.core_total = round(core_total, 4)
        self.save()

    def calculate_supp_total(self):
        supp_total = (self.supp_a1 + self.supp_a2 + self.supp_a3 + self.supp_a4 + self.supp_a5 + self.supp_a6) / 6
        self.supp_total = round(supp_total, 4)
        self.save()

    def calculate_final_numerical_rating(self):
        final_numerical_rating = (
            self.stra_a1
            + self.stra_a2
            + self.stra_a3
            + self.core_a1
            + self.core_a2
            + self.core_a3
            + self.core_a4
            + self.core_a5
            + self.core_a6
            + self.core_a7
            + self.core_a8
            + self.core_a9
            + self.core_a10
            + self.core_a11
            + self.core_a12
            + self.core_a13
            + self.core_a14
            + self.core_a15
            + self.core_a16
            + self.core_a17
            + self.core_a18
            + self.core_a19
            + self.supp_a1
            + self.supp_a2
            + self.supp_a3
            + self.supp_a4
            + self.supp_a5
            + self.supp_a6
        ) / 27

        self.final_numerical_rating = round(final_numerical_rating, 4)
        self.save()


class IPCRSpecificationValue(models.Model):
    """
    The IPCR Specification Value table holds each of the
    ipcrs individual specification or bespoke features.
    """

    ipcr = models.ForeignKey(IPCR, on_delete=models.CASCADE)
    specification = models.ForeignKey(IPCRSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("IPCR specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("IPCR Specification Value")
        verbose_name_plural = _("IPCR Specification Values")

    def __str__(self):
        return self.value


class IPCRImage(models.Model):
    """
    The IPCR Image table.
    """

    ipcr = models.ForeignKey(IPCR, on_delete=models.CASCADE, related_name="ipcr_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a ipcr image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("IPCR Image")
        verbose_name_plural = _("IPCR Images")
