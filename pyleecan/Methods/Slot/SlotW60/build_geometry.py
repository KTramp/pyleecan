from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment


def build_geometry(self):
    """Compute the curve (Line) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : SlotW60
        A SlotW60 object

    Returns
    -------
    curve_list: list
        A list of 8 Segment and 2 Arc1

    """

    [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11] = self._comp_point_coordinate()

    # Creation of curve
    curve_list = list()
    curve_list.append(Arc1(Z1, Z2, self.R1))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(Segment(Z4, Z5))
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z7))
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Segment(Z9, Z10))
    curve_list.append(Arc1(Z10, Z11, self.R1))

    return curve_list
