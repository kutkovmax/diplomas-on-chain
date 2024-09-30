from django.shortcuts import render
from .models import Certificate
from .web3utils import *

def issue_certificate_view(request):
    if request.method == 'POST':
        student_name = request.POST['student_name']
        course_name = request.POST['course_name']
        student_address = request.POST['student_address']

        cert_id = create_certificate(student_address, student_name, course_name)
        certificate = Certificate(
            cert_id=cert_id,
            student_name=student_name,
            course_name=course_name,
            # blockchain_address=student_address
        )
        certificate.save()
        
        tx_hash = send_certificate_to_blockchain(cert_id, student_address, student_name, course_name)

        return render(request, 'certificate_issued.html', {'tx_hash': tx_hash.hex(), 'cert_id': cert_id.hex()})

    return render(request, 'issue_certificate.html')

def get_certificate_view(request):
    if request.method == 'POST':
        cert_id = bytes.fromhex(request.POST['cert_id'])
        try:
            certificate = get_certificate_by_id(cert_id)
            if certificate:
                return render(request, 'certificate_detail.html', {'certificate': certificate})
            else:
                return render(request, 'certificate_not_found.html', {'cert_id': cert_id})
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})
    return render(request, 'get_certificate.html')
