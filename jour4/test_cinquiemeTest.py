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

@pytest.mark.usefixtures("setup","before")
def test_login():
    #print("Ouvrir le navigateur")
    print("Se connecter sur google")
    #print("Fermer le navigateur")

@pytest.mark.usefixtures("setup","before")
def test_creerCompte():
    #print("Ouvrir le navigateur")
    print("Creer un compte google")
    #print("Fermer le navigateur")

@pytest.mark.usefixtures("setup","before")
def test_reinitialiserPasse():
    # print("Ouvrir le navigateur")
    print("Reinitialiser le mot de passe")
    # print("Fermer le navigateur")











