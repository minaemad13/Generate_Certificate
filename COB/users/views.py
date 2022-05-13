from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa


# Create your views here.


def certificate(req):
    if req.method == 'GET':

        return render(req, 'certificate_form.html')
    if req.method == 'POST':
        template_path = 'certificate.html'
        context = {"name": req.POST["username"], "special": req.POST["Special"], "work": req.POST["WorkPlace"]}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="products_report.pdf"'

        template = get_template(template_path)

        html = template.render(context)
        # create a pdf

        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


        #return render(req, 'certificate.html',context)
