import json


def testRootTrustResponse(client):
    response = client.get("/ca/root-trust")
    assert response.status_code == 200
    assert "root" in response.json

def testHostCertResponse(client):
    response = client.post("/ca/host-certificate",
                          headers={"Content-Type": "application/json"},
                          data=json.dumps({"hostname": "testhost.local"}))
    assert response.status_code == 200
    assert "key" in response.json
    assert "cert" in response.json
    assert "root" in response.json
    # test GET now that cert is created
    response = client.get("/ca/host-certificate",
                          headers={"Content-Type": "application/json"},
                          data=json.dumps({"hostname": "testhost.local"}))
    assert response.status_code == 200
    assert "key" in response.json
    assert "cert" in response.json
    assert "root" in response.json

