import pytest

def test_validation_title():
    titre_attendu = "orange"
    titre_obtenu = "orange"
    url = "https://www.google.com"
    print("debut des validations")
    assert "google" in url
    assert titre_attendu == titre_obtenu,"les titres sont différents"
    print("fin des validations")


