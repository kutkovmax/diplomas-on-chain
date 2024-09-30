import json
from web3 import Web3
from django.conf import settings
import hashlib
from eth_utils import to_bytes, keccak
import time

ganache_url = settings.WEB3_PROVIDER
web3 = Web3(Web3.HTTPProvider(ganache_url))

contract_address = settings.CONTRACT_ADDRESS
contract_abi = json.loads(settings.ABI)
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


def generate_cert_id(student_address, student_name, course_name):
    unique_string = f"{student_address}{student_name}{course_name}{time.time()}"
    return keccak(text=unique_string)


def send_certificate_to_blockchain(cert_id, student_address, student_name, course_name):
    account = web3.eth.accounts[0]
    
    tx_hash = contract.functions.issueCertificate(
        cert_id,
        student_address,
        student_name,
        course_name
    ).transact({
        'from': account,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })

    return tx_hash



def get_certificate_by_id(cert_id):
    certificate = contract.functions.getCertificateById(cert_id).call()
        
    if certificate:
        return {
            'id': certificate[0],
            'name': certificate[1],
            'course': certificate[2],
            'issued_at': certificate[3]
        }
    
    return None
