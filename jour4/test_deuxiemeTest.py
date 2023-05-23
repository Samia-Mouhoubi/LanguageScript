"""
l'ouverture et la fermeture du navigateur se repete dans chaque test
A eviter (DRY : don't repeat yourself)
pour eviter cela: il faut creer deux fonctions (instructions) (setup et teardown) qui seront repetees a chaque test
cela permettra ainsi d'eviter la repetition
"""

import pytest

def setup_module(module):
    print("Ouvrir la base de données")

def teardown_module(module):
    print("Fermer le navigateur")


def setup_function(function):
    print("Ouvrir le navigateur")

def teardown_function(function):
    print("Fermer le navigateur")


def test_login():
    #print("Ouvrir le navigateur")
    print("Se connecter sur google")
    #print("Fermer le navigateur")

def test_creerCompte():
    #print("Ouvrir le navigateur")
    print("Creer un compte google")
    #print("Fermer le navigateur")

def test_reinitialiserPasse():
    # print("Ouvrir le navigateur")
    print("Reinitialiser le mot de passe")
    # print("Fermer le navigateur")











