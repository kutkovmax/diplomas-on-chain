from django.shortcuts import render
from .models import Certificate
from .web3utils import issue_certificate

def issue_certificate_view(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        course_name = request.POST['course_name']
        student_address = request.POST['student_address']

        # Вызываем метод смарт-контракта для выдачи сертификата
        tx_hash = issue_certificate(student_address, student_name, course_name)

        # Сохраняем данные в базу
        certificate = Certificate(
            student_name=student_name,
            course_name=course_name,
            certificate_hash=tx_hash # web3.toHex(tx_hash)
        )
        certificate.save()

        return render(request, 'certificate_issued.html', {'tx_hash': tx_hash})

    return render(request, 'issue_certificate.html')
