from setuptools import setup


setup(
    # Self-descriptive entries which should always be present
    name='bead_spring',
    author='Matthew W. Thompson',
    author_email='matt.thompson@vanderbilt.edu',
    license='MIT',
    version='0.0.0',
    description='mBuild recipe for bead-spring polymers',
    zip_safe=False,
    entry_points={
        'mbuild.plugins':[
        "BeadSpring = bead_spring.bead_spring:BeadSpring"
        ]
        }
    )
