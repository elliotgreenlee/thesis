"""
Elliot Greenlee
Date Started: 2018-01-22
University of Tennessee, Knoxville: WIND
"""

from target import Target


def detect_targets(frame):
    targets = []

    targets.append(Target([(0, 50), (50, 100)], 'person'))

    return targets
