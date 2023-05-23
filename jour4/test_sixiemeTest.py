"""
executer uniquement login
"""

import pytest


@pytest.fixture(scope="module")
def setup():
    print("Ouvrir la base de données")
    yield
    print("Fermer la base de donnees")
@pytest.fixture(scope="function")
def before():
    print("Ouvrir le navigateur")
    yield
    print("Fermer le navigateur")

@pytest.mark.regression
def test_login():
    #print("Ouvrir le navigateur")
    print("Se connecter sur google")
    #print("Fermer le navigateur")

@pytest.mark.regression
def test_creerCompte():
    #print("Ouvrir le navigateur")
    print("Creer un compte google")
    #print("Fermer le navigateur")

@pytest.mark.charge
def test_reinitialiserPasse():
    # print("Ouvrir le navigateur")
    print("Reinitialiser le mot de passe")
    # print("Fermer le navigateur")

@pytest.mark.charge
def test_quatrieme():
    # print("Ouvrir le navigateur")
    print("quatrieme test")
    # print("Fermer le navigateur")

@pytest.mark.skip
def test_cinquieme():
    # print("Ouvrir le navigateur")
    print("cinquieme test")
    # print("Fermer le navigateur")

@pytest.mark.skip
def test_sixieme():
    # print("Ouvrir le navigateur")
    print("sixieme test")
    # print("Fermer le navigateur")






