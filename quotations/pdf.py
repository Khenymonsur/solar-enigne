from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

from .models import Quotation


def quotation_pdf(request, pk):

    quotation = Quotation.objects.get(pk=pk)

    html = render_to_string(
        "quotations/pdf.html",
        {
            "quotation": quotation,
        },
    )

    pdf = HTML(
        string=html,
        base_url=request.build_absolute_uri("/")
    ).write_pdf()

    response = HttpResponse(
        pdf,
        content_type="application/pdf"
    )

    response[
        "Content-Disposition"
    ] = f'inline; filename="{quotation.quotation_no}.pdf"'

    return response