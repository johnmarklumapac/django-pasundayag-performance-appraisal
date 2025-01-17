from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    IPCR,
    IPCRImage,
    IPCRSpecification,
    IPCRSpecificationValue,
    Status,
)

admin.site.register(Category, MPTTModelAdmin)


class IPCRSpecificationInline(admin.TabularInline):
    model = IPCRSpecification


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    inlines = [
        IPCRSpecificationInline,
    ]


class IPCRImageInline(admin.TabularInline):
    model = IPCRImage


class IPCRSpecificationValueInline(admin.TabularInline):
    model = IPCRSpecificationValue


@admin.register(IPCR)
class IPCRAdmin(admin.ModelAdmin):
    inlines = [
        IPCRSpecificationValueInline,
        IPCRImageInline,
    ]
