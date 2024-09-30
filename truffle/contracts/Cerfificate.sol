// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Certificate {
    struct Cert {
        bytes32 id;
        string name;
        string course;
        uint256 issueDate;
    }

    mapping(bytes32 => Cert) private certificates;
    mapping(address => bytes32[]) private userCertificates;

    function issueCertificate(
        bytes32 _certId,
        address _recipient,
        string memory _name,
        string memory _course
    ) public returns (Cert memory) {
        // Проверка на уникальность ID (можно добавить более строгую проверку)
        require(certificates[_certId].issueDate == 0, "Certificate ID already exists");

        certificates[_certId] = Cert({
            id: _certId,
            name: _name,
            course: _course,
            issueDate: block.timestamp
        });
        
        userCertificates[_recipient].push(_certId);
        return certificates[_certId];
    }


    function getCertificateById(bytes32 _id) public view returns (Cert memory) {
        Cert memory cert = certificates[_id];
        require(bytes(cert.name).length > 0, "Certificate not found");
        return cert;
    }

    function getCertificatesByAddress(address _recipient) public view returns (Cert[] memory) {
        bytes32[] memory ids = userCertificates[_recipient];
        Cert[] memory certs = new Cert[](ids.length);
        for (uint256 i = 0; i < ids.length; i++) {
            certs[i] = certificates[ids[i]];
        }
        return certs;
    }
}
