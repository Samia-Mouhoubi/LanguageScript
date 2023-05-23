# """
# l'ouverture et la fermeture du navigateur se repete dans chaque test
# A eviter (DRY : don't repeat yourself)
# pour eviter cela: il faut creer deux fonctions (instructions) (setup et teardown) qui seront repetees a chaque test
# cela permettra ainsi d'eviter la repetition
# """
#
# import pytest
#
# def setup_module(module):
#     print("Ouvrir la base de données")
#
# def teardown_module(module):
#     print("Fermer le navigateur")
#
#
# def setup_function(function):
#     print("Ouvrir le navigateur")
#
# def teardown_function(function):
#     print("Fermer le navigateur")
# #creation de deux fonctions qui jouent le rele que les fonctions du deuxiemeTest
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


def test_login(setup,before):
    #print("Ouvrir le navigateur")
    print("Se connecter sur google")
    #print("Fermer le navigateur")

def test_creerCompte(setup,before):
    #print("Ouvrir le navigateur")
    print("Creer un compte google")
    #print("Fermer le navigateur")

def test_reinitialiserPasse(setup,before):
    # print("Ouvrir le navigateur")
    print("Reinitialiser le mot de passe")
    # print("Fermer le navigateur")











