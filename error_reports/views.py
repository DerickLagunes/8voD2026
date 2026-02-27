from django.shortcuts import render
from .forms import ErrorReportForm
from .models import ErrorReport
from django.http import JsonResponse



# Create your views here.
def error_reports_view(request):
    if request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el reporte de error en la base de datos
            return JsonResponse({
                'status': 'ok',
                'message': 'Registro exitoso',
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Algo salio mal',
                'errors': form.errors,
            }, status=400)
    else:
        form = ErrorReportForm()
    return render(request, 'error_reports/reporte_error.html', {'form': form})

def obtener_reportes(request):
    reportes = ErrorReport.objects.all().values()
    return JsonResponse(list(reportes), safe=False)