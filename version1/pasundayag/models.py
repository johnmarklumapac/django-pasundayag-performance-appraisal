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

    stra_percentage = models.CharField( max_length=255, default="")

    stra_mfo_pap_1 =  models.TextField( blank=True)
    stra_sucess_indicators_1 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_1 =  models.TextField( blank=True) 
    stra_q1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_1 =  models.TextField( blank=True)

    stra_mfo_pap_2 =  models.TextField(  blank=True)
    stra_sucess_indicators_2 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_2 =  models.TextField( blank=True) 
    stra_q2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_2 =  models.TextField( blank=True)

    stra_mfo_pap_3 =  models.TextField(blank=True)
    stra_sucess_indicators_3 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_3 =  models.TextField( blank=True) 
    stra_q3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_3 =  models.TextField( blank=True)

    stra_mfo_pap_4 =  models.TextField(blank=True)
    stra_sucess_indicators_4 =  models.TextField(blank=True) 
    stra_actual_accomplishment_indicators_4 =  models.TextField( blank=True) 
    stra_q4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_4 =  models.TextField( blank=True)

    stra_mfo_pap_5 =  models.TextField(  blank=True)
    stra_sucess_indicators_5 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_5 =  models.TextField( blank=True) 
    stra_q5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_5 =  models.TextField( blank=True)

    stra_mfo_pap_6 =  models.TextField(  blank=True)
    stra_sucess_indicators_6 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_6 =  models.TextField( blank=True) 
    stra_q6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_6 =  models.TextField(blank=True)

    stra_mfo_pap_7 =  models.TextField( blank=True)
    stra_sucess_indicators_7 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_7 =  models.TextField( blank=True) 
    stra_q7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_7 =  models.TextField( blank=True)

    stra_mfo_pap_8 =  models.TextField(  blank=True)
    stra_sucess_indicators_8 =  models.TextField( blank=True) 
    stra_actual_accomplishment_indicators_8 =  models.TextField( blank=True) 
    stra_q8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_e8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_t8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_a8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    stra_remarks_8 =  models.TextField(blank=True)

    stra_total = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

    core_percentage = models.CharField(max_length=255, default="")

    core_acad_mfo_pap_1 =  models.TextField(  blank=True)
    core_acad_indicators_1 =  models.TextField(blank=True)
    core_acad_actual_accomplishment_indicators_1 =  models.TextField( blank=True)  
    core_acad_q1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_1 =  models.TextField(blank=True)

    mfo_acad_mfo_pap_2 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_2 =  models.TextField(  blank=True) 
    core_acad_actual_accomplishment_indicators_2 =  models.TextField( blank=True)
    core_acad_q2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_2 =  models.TextField( blank=True)

    mfo_acad_mfo_pap_3 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_3 =  models.TextField(  blank=True) 
    core_acad_actual_accomplishment_indicators_3 =  models.TextField( blank=True)
    core_acad_q3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_3 =  models.TextField(blank=True)

    mfo_acad_mfo_pap_4 =  models.TextField(blank=True)
    core_acad_acad_sucess_indicators_4 =  models.TextField(  blank=True)
    core_actual_accomplishment_indicators_4 =  models.TextField( blank=True) 
    core_acad_q4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_4 =  models.TextField( blank=True)

    core_acad_mfo_pap_5 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_5 =  models.TextField(  blank=True)
    core_acad_actual_accomplishment_indicators_5 =  models.TextField( blank=True) 
    core_acad_q5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_5 =  models.TextField( blank=True)

    core_acad_mfo_pap_6 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_6 =  models.TextField(  blank=True)
    core_acad_actual_accomplishment_indicators_6 =  models.TextField( blank=True) 
    core_acad_q6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_6 =  models.TextField( blank=True)

    core_acad_mfo_pap_7 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_7 =  models.TextField(  blank=True)
    core_acad_actual_accomplishment_indicators_7 =  models.TextField( blank=True) 
    core_acad_q7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_7 =  models.TextField( blank=True)

    core_acad_mfo_pap_8 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_8 =  models.TextField(  blank=True) 
    core_acad_actual_accomplishment_indicators_8 =  models.TextField( blank=True)
    core_acad_q8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a8 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_8 =  models.TextField( blank=True)

    core_mfo_pap_9 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_9 =  models.TextField(  blank=True) 
    core_acad_actual_accomplishment_indicators_9 =  models.TextField(blank=True)
    core_acad_q9 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e9 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t9 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a9 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_9 =  models.TextField( blank=True)

    core_acad_mfo_pap_10 =  models.TextField(  blank=True)
    core_acad_sucess_indicators_10 =  models.TextField(  blank=True) 
    core_acad_actual_accomplishment_indicators_10 =  models.TextField( blank=True)
    core_acad_q10 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_e10 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_t10 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_a10 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_acad_remarks_10 =  models.TextField( blank=True)

    core_acad_total = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

    core_irp_pap_1 =  models.TextField(  blank=True)
    core_irp_indicators_1 =  models.TextField(  blank=True) 
    core_irp_actual_accomplishment_indicators_1 =  models.TextField( blank=True)
    core_irp_q1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_e1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_t1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_a1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_remarks_1 =  models.TextField( blank=True)

    mfo_irp_pap_2 =  models.TextField(  blank=True)
    core_irp_sucess_indicators_2 =  models.TextField(  blank=True) 
    core_irp_actual_accomplishment_indicators_2 =  models.TextField( blank=True)
    core_irp_q2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_e2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_t2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_a2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_remarks_2 =  models.TextField( blank=True)

    mfo_irp_pap_3 =  models.TextField(  blank=True)
    core_irp_sucess_indicators_3 =  models.TextField(  blank=True)  
    core_irp_actual_accomplishment_indicators_3 =  models.TextField(  blank=True)
    core_irp_q3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_e3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_t3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_a3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_remarks_3 =  models.TextField( blank=True)

    mfo_irp_pap_4 =  models.TextField(  blank=True)
    core_irp_sucess_indicators_4 =  models.TextField(  blank=True) 
    core_irp_actual_accomplishment_indicators_4 =  models.TextField( blank=True)
    core_irp_q4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_e4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_t4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_a4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_remarks_4 =  models.TextField( blank=True)

    core_irp_mfo_pap_5 =  models.TextField(  blank=True)
    core_irp_sucess_indicators_5 =  models.TextField(  blank=True) 
    core_irp_actual_accomplishment_indicators_5 =  models.TextField( blank=True)
    core_irp_q5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_e5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_t5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_a5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_remarks_6 =  models.TextField( blank=True)

    core_irp_mfo_pap_6 =  models.TextField(  blank=True)
    core_irp_sucess_indicators_6 =  models.TextField( blank=True) 
    core_irp_actual_accomplishment_indicators_6 =  models.TextField( blank=True)
    core_irp_q6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_e6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_t6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_a6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_irp_remarks_6 =  models.TextField( blank=True)

    core_irp_total = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

    core_tae_pap_1 =  models.TextField(  blank=True)
    core_tae_indicators_1 =  models.TextField(  blank=True) 
    core_tae_actual_accomplishment_indicators_1 =  models.TextField( blank=True)
    core_tae_q1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_1 =  models.TextField( blank=True)

    mfo_tae_pap_2 =  models.TextField(verbose_name=_("Success Indeiator row"),  blank=True)
    core_tae_sucess_indicators_2 =  models.TextField(  blank=True) 
    core_tae_actual_accomplishment_indicators_2 =  models.TextField(blank=True)
    core_tae_q2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_2 =  models.TextField( blank=True)

    mfo_tae_pap_3 =  models.TextField(  blank=True)
    core_tae_sucess_indicators_3 =  models.TextField(  blank=True) 
    core_tae_actual_accomplishment_indicators_3 =  models.TextField(  blank=True)
    core_tae_q3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_3 =  models.TextField( blank=True)

    mfo_tae_pap_4 =  models.TextField(  blank=True)
    core_tae_sucess_indicators_4 =  models.TextField(  blank=True)
    core_tae_actual_accomplishment_indicators_4 =  models.TextField( blank=True) 
    core_tae_q4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_4 =  models.TextField( blank=True)

    core_tae_mfo_pap_5 =  models.TextField(  blank=True)
    core_tae_sucess_indicators_5 =  models.TextField(  blank=True) 
    core_tae_actual_accomplishment_indicators_5 =  models.TextField( blank=True)
    core_tae_q5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_5 =  models.TextField( blank=True)

    core_tae_mfo_pap_6 =  models.TextField(  blank=True)
    core_tae_sucess_indicators_6 =  models.TextField( blank=True) 
    core_tae_actual_accomplishment_indicators_6 =  models.TextField( blank=True)
    core_tae_q6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_6 =  models.TextField( blank=True)

    core_tae_mfo_pap_7 =  models.TextField(  blank=True)
    core_tae_sucess_indicators_7 =  models.TextField(  blank=True) 
    core_tae_actual_accomplishment_indicators_7 =  models.TextField( blank=True)
    core_tae_q7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_e7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_t7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_a7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    core_tae_remarks_7 =  models.TextField( blank=True)

    core_tae_total = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

    supp_percentage = models.CharField(
         max_length=255, default=""
    )

    supp_mfo_pap_1 =  models.TextField(  blank=True)
    supp_sucess_indicators_1 =  models.TextField(  blank=True)
    supp_actual_accomplishment_indicators_1 =  models.TextField( blank=True) 
    supp_q1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a1 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_1 =  models.TextField( blank=True)

    supp_mfo_pap_2 =  models.TextField(  blank=True)
    supp_sucess_indicators_2 =  models.TextField(  blank=True) 
    supp_actual_accomplishment_indicators_2 =  models.TextField( blank=True) 
    supp_q2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a2 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_2 =  models.TextField( blank=True)

    supp_mfo_pap_3 =  models.TextField(verbose_name=_("Success Indeiator row"),  blank=True)
    supp_sucess_indicators_3 =  models.TextField(  blank=True) 
    supp_actual_accomplishment_indicators_3 =  models.TextField( blank=True) 
    supp_q3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a3 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_3 =  models.TextField( blank=True)

    supp_mfo_pap_4 =  models.TextField(  blank=True)
    supp_sucess_indicators_4 =  models.TextField(  blank=True) 
    supp_actual_accomplishment_indicators_4 =  models.TextField( blank=True) 
    supp_q4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a4 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_4 =  models.TextField( blank=True)

    supp_mfo_pap_5 =  models.TextField(  blank=True)
    supp_sucess_indicators_5 =  models.TextField(  blank=True) 
    supp_actual_accomplishment_indicators_5 =  models.TextField( blank=True) 
    supp_q5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a5 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_5 =  models.TextField( blank=True)

    supp_mfo_pap_6 =  models.TextField(  blank=True)
    supp_sucess_indicators_6 =  models.TextField( blank=True) 
    supp_actual_accomplishment_indicators_6 =  models.TextField( blank=True) 
    supp_q6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a6 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_6 =  models.TextField( blank=True)

    supp_mfo_pap_7 =  models.TextField(  blank=True)
    supp_sucess_indicators_7 =  models.TextField(  blank=True) 
    supp_actual_accomplishment_indicators_7 =  models.TextField( blank=True) 
    supp_q7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_e7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_t7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_a7 = models.DecimalField(max_digits=5, decimal_places=4, blank=True)
    supp_remarks_7 =  models.TextField( blank=True)

    supp_total = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

    final_numerical_rating = models.DecimalField( max_digits=5, decimal_places=4, blank=True)
    final_adjectival_rating = models.CharField(
        max_length=255, default=""
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("IPCR")
        verbose_name_plural = _("IPCRs")


    def get_absolute_url(self):
        return reverse("pasundayag:ipcr_detail", args=[self.slug])
    

    def __str__(self):
        return self.title
    

    def calculate_stra_total(self):
        self.stra_total = (self.stra_a1 + self.stra_a2 + self.stra_a3) / 3
        self.save()


    def calculate_core_acad_total(self):
        core_acad_total = (
            self.core_acad_a1
            + self.core_acad_a2
            + self.core_acad_a3
            + self.core_acad_a4
            + self.core_acad_a5
            + self.core_acad_a6
            + self.core_acad_a7
            + self.core_acad_a8
            + self.core_acad_a9
            + self.core_acad_a10
        ) / 10
        self.core_acad_total = round(core_acad_total, 4)
        self.save()


    def calculate_irp_total(self):
        core_irp_total = (
            self.core_irp_a1
            + self.core_irp_a2
            + self.core_irp_a3
            + self.core_irp_a4
            + self.core_irp_a5
            + self.core_irp_a6
        ) / 6
        self.core_irp_total = round(core_irp_total, 4)
        self.save()

    
    def calculate_tae_total(self):
        core_tae_total = (
            self.core_tae_a1
            + self.core_tae_a2
            + self.core_tae_a3
            + self.core_tae_a4
            + self.core_tae_a5
            + self.core_tae_a6
            + self.core_tae_a7
        ) / 7
        self.core_tae_total = round(core_tae_total, 4)
        self.save()


    def calculate_supp_total(self):
        supp_total = (
            self.supp_a1
            + self.supp_a2
            + self.supp_a3
            + self.supp_a4
            + self.supp_a5
            + self.supp_a6
            + self.supp_a7
        ) / 7
        self.supp_total = round(supp_total, 4)
        self.save()

    
    def calculate_final_numerical_rating(self):
        final_numerical_rating = (
            self.stra_a1 
            + self.stra_a2 
            + self.stra_a3
            + self.core_acad_a1
            + self.core_acad_a2
            + self.core_acad_a3
            + self.core_acad_a4
            + self.core_acad_a5
            + self.core_acad_a6
            + self.core_acad_a7
            + self.core_acad_a8
            + self.core_acad_a9
            + self.core_acad_a10
            + self.core_irp_a1
            + self.core_irp_a2
            + self.core_irp_a3
            + self.core_irp_a4
            + self.core_irp_a5
            + self.core_irp_a6
            + self.core_tae_a1
            + self.core_tae_a2
            + self.core_tae_a3
            + self.core_tae_a4
            + self.core_tae_a5
            + self.core_tae_a6
            + self.core_tae_a7
            + self.supp_a1
            + self.supp_a2
            + self.supp_a3
            + self.supp_a4
            + self.supp_a5
            + self.supp_a6
            + self.supp_a7     
        ) / 33
        self.final_numerical_rating = round(final_numerical_rating, 4)
        self.save()


    def save(self, *args, **kwargs):
        if self.final_numerical_rating >= 5:
            self.final_adjectival_rating = "Outstanding"
        elif self.final_numerical_rating >= 4:
            self.final_adjectival_rating = "Very Satisfactory"
        elif self.final_numerical_rating >= 3:
            self.final_adjectival_rating = "Satisfactory"
        elif self.final_numerical_rating >= 2:
            self.final_adjectival_rating = "Unsatisfactory"
        else:
            self.final_adjectival_rating = "Very Unsatisfactory"
        super().save(*args, **kwargs)


    

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
