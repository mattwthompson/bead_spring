"""
Primary function of recipe here
"""

import mbuild as mb


class BeadSpring(mb.Compound):
    """
    Example class that would go in your recipe.

    Parameters
    ----------
    your_argument: int
        This is an example argument

    """
    def __init__(self, n_beads=10, build='linear', bead_name='bead', spring_distance=1):
        super(BeadSpring, self).__init__()
        prev_bead = mb.Particle(pos=[0.0, 0.0, 0.0], name=bead_name)
        self.add(prev_bead)
        for n in range(1, n_beads):
            current_bead = mb.Particle(pos=[0.0, 0.0, n*spring_distance], name=bead_name)
            self.add(current_bead)
            self.add_bond((prev_bead, current_bead))
            prev_bead = current_bead