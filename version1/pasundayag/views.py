from django.shortcuts import get_object_or_404, render

from .models import Category, IPCR


def ipcr_all(request):
    ipcrs = IPCR.objects.prefetch_related("ipcr_image").filter(is_active=True)
    return render(request, "pasundayag/index.html", {"ipcrs": ipcrs})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    ipcrs = IPCR.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "pasundayag/category.html", {"category": category, "ipcrs": ipcrs})


def ipcr_detail(request, slug):
    ipcr = get_object_or_404(IPCR, slug=slug, is_active=True)
    ipcr.calculate_stra_total()
    ipcr.calculate_core_acad_total()
    ipcr.calculate_irp_total()
    ipcr.calculate_tae_total()
    ipcr.calculate_supp_total()
    ipcr.calculate_final_numerical_rating()
    return render(request, "pasundayag/single.html", {"ipcr": ipcr})
