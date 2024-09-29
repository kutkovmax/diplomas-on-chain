import json
from web3 import Web3
from django.conf import settings

ganache_url = settings.WEB3_PROVIDER
web3 = Web3(Web3.HTTPProvider(ganache_url))

contract_address = settings.CONTRACT_ADDRESS
contract_abi = json.loads(settings.ABI)
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def issue_certificate(student_address, student_name, course_name):
    account = web3.eth.accounts[0]

    tx_hash = contract.functions.issueCertificate(
        student_address, student_name, course_name
    ).transact({
        'from': account,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })

    return web3.to_hex(tx_hash)

