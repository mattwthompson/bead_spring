"""
Unit and regression test for the bead_spring package.
"""

# Import package, test suite, and other packages as needed
import bead_spring
import pytest
import sys
import mbuild as mb

def test_bead_spring_imported():
    """ Sample test, will always pass so long as import statement worked """
    assert "bead_spring" in sys.modules

def test_import():
    """ Test that mBuild recipe import works """
    assert "BeadSpring" in vars(mb.recipes).keys()

def test_default_build():
    polymer = bead_spring.bead_spring.BeadSpring()
    assert polymer.n_particles == 10
    assert set([c.name for c in polymer.children]) == {'bead'}