import pytest
from bataille.jeu import Jeu

def test_placement_et_tirs():
    jeu = Jeu(taille=5)
    assert jeu.placer_bateau((0, 0), (0, 2)) is True
    assert jeu.tirer((0, 0)) == "touché"
    assert jeu.tirer((0, 1)) == "touché"
    assert jeu.tirer((0, 2)) == "touché"
    assert jeu.tirer((0, 2)) == "déjà tiré"

def test_tir_hors_limite():
    jeu = Jeu(taille=3)
    jeu.placer_bateau((1, 1), (1, 1))
    with pytest.raises(ValueError):
        jeu.tirer((10, 10))

def test_tous_coules():
    jeu = Jeu(taille=3)
    jeu.placer_bateau((0, 0), (0, 0))
    assert not jeu.tous_les_bateaux_coules()
    jeu.tirer((0, 0))
    assert jeu.tous_les_bateaux_coules()