# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/CondType13.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/CondType13
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .Conductor import Conductor

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.CondType13.comp_surface_active import comp_surface_active
except ImportError as error:
    comp_surface_active = error

try:
    from ..Methods.Machine.CondType13.comp_height import comp_height
except ImportError as error:
    comp_height = error

try:
    from ..Methods.Machine.CondType13.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Machine.CondType13.comp_width import comp_width
except ImportError as error:
    comp_width = error

try:
    from ..Methods.Machine.CondType13.plot import plot
except ImportError as error:
    plot = error

try:
    from ..Methods.Machine.CondType13.plot_schematics import plot_schematics
except ImportError as error:
    plot_schematics = error

try:
    from ..Methods.Machine.CondType13.comp_width_wire import comp_width_wire
except ImportError as error:
    comp_width_wire = error

try:
    from ..Methods.Machine.CondType13.comp_height_wire import comp_height_wire
except ImportError as error:
    comp_height_wire = error

try:
    from ..Methods.Machine.CondType13.comp_nb_circumferential_wire import (
        comp_nb_circumferential_wire,
    )
except ImportError as error:
    comp_nb_circumferential_wire = error

try:
    from ..Methods.Machine.CondType13.comp_nb_radial_wire import comp_nb_radial_wire
except ImportError as error:
    comp_nb_radial_wire = error

try:
    from ..Methods.Machine.CondType13.is_round_wire import is_round_wire
except ImportError as error:
    is_round_wire = error


from numpy import isnan
from ._check import InitUnKnowClassError


class CondType13(Conductor):
    """parallel stranded conductor consisting of at least a single round wire"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.CondType13.comp_surface_active
    if isinstance(comp_surface_active, ImportError):
        comp_surface_active = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_surface_active: "
                    + str(comp_surface_active)
                )
            )
        )
    else:
        comp_surface_active = comp_surface_active
    # cf Methods.Machine.CondType13.comp_height
    if isinstance(comp_height, ImportError):
        comp_height = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_height: " + str(comp_height)
                )
            )
        )
    else:
        comp_height = comp_height
    # cf Methods.Machine.CondType13.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_surface: " + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Machine.CondType13.comp_width
    if isinstance(comp_width, ImportError):
        comp_width = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_width: " + str(comp_width)
                )
            )
        )
    else:
        comp_width = comp_width
    # cf Methods.Machine.CondType13.plot
    if isinstance(plot, ImportError):
        plot = property(
            fget=lambda x: raise_(
                ImportError("Can't use CondType13 method plot: " + str(plot))
            )
        )
    else:
        plot = plot
    # cf Methods.Machine.CondType13.plot_schematics
    if isinstance(plot_schematics, ImportError):
        plot_schematics = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method plot_schematics: "
                    + str(plot_schematics)
                )
            )
        )
    else:
        plot_schematics = plot_schematics
    # cf Methods.Machine.CondType13.comp_width_wire
    if isinstance(comp_width_wire, ImportError):
        comp_width_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_width_wire: "
                    + str(comp_width_wire)
                )
            )
        )
    else:
        comp_width_wire = comp_width_wire
    # cf Methods.Machine.CondType13.comp_height_wire
    if isinstance(comp_height_wire, ImportError):
        comp_height_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_height_wire: "
                    + str(comp_height_wire)
                )
            )
        )
    else:
        comp_height_wire = comp_height_wire
    # cf Methods.Machine.CondType13.comp_nb_circumferential_wire
    if isinstance(comp_nb_circumferential_wire, ImportError):
        comp_nb_circumferential_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_nb_circumferential_wire: "
                    + str(comp_nb_circumferential_wire)
                )
            )
        )
    else:
        comp_nb_circumferential_wire = comp_nb_circumferential_wire
    # cf Methods.Machine.CondType13.comp_nb_radial_wire
    if isinstance(comp_nb_radial_wire, ImportError):
        comp_nb_radial_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method comp_nb_radial_wire: "
                    + str(comp_nb_radial_wire)
                )
            )
        )
    else:
        comp_nb_radial_wire = comp_nb_radial_wire
    # cf Methods.Machine.CondType13.is_round_wire
    if isinstance(is_round_wire, ImportError):
        is_round_wire = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use CondType13 method is_round_wire: " + str(is_round_wire)
                )
            )
        )
    else:
        is_round_wire = is_round_wire
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Wwire=0.015,
        Wins_cond=0.015,
        Nwppc_rad=1,
        Nwppc_tan=1,
        Wins_wire=0,
        Kwoh=0.5,
        cond_mat=-1,
        ins_mat=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Wwire" in list(init_dict.keys()):
                Wwire = init_dict["Wwire"]
            if "Wins_cond" in list(init_dict.keys()):
                Wins_cond = init_dict["Wins_cond"]
            if "Nwppc_rad" in list(init_dict.keys()):
                Nwppc_rad = init_dict["Nwppc_rad"]
            if "Nwppc_tan" in list(init_dict.keys()):
                Nwppc_tan = init_dict["Nwppc_tan"]
            if "Wins_wire" in list(init_dict.keys()):
                Wins_wire = init_dict["Wins_wire"]
            if "Kwoh" in list(init_dict.keys()):
                Kwoh = init_dict["Kwoh"]
            if "cond_mat" in list(init_dict.keys()):
                cond_mat = init_dict["cond_mat"]
            if "ins_mat" in list(init_dict.keys()):
                ins_mat = init_dict["ins_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.Wwire = Wwire
        self.Wins_cond = Wins_cond
        self.Nwppc_rad = Nwppc_rad
        self.Nwppc_tan = Nwppc_tan
        self.Wins_wire = Wins_wire
        self.Kwoh = Kwoh
        # Call Conductor init
        super(CondType13, self).__init__(cond_mat=cond_mat, ins_mat=ins_mat)
        # The class is frozen (in Conductor init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        CondType13_str = ""
        # Get the properties inherited from Conductor
        CondType13_str += super(CondType13, self).__str__()
        CondType13_str += "Wwire = " + str(self.Wwire) + linesep
        CondType13_str += "Wins_cond = " + str(self.Wins_cond) + linesep
        CondType13_str += "Nwppc_rad = " + str(self.Nwppc_rad) + linesep
        CondType13_str += "Nwppc_tan = " + str(self.Nwppc_tan) + linesep
        CondType13_str += "Wins_wire = " + str(self.Wins_wire) + linesep
        CondType13_str += "Kwoh = " + str(self.Kwoh) + linesep
        return CondType13_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Conductor
        if not super(CondType13, self).__eq__(other):
            return False
        if other.Wwire != self.Wwire:
            return False
        if other.Wins_cond != self.Wins_cond:
            return False
        if other.Nwppc_rad != self.Nwppc_rad:
            return False
        if other.Nwppc_tan != self.Nwppc_tan:
            return False
        if other.Wins_wire != self.Wins_wire:
            return False
        if other.Kwoh != self.Kwoh:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Conductor
        diff_list.extend(
            super(CondType13, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (
            other._Wwire is not None
            and self._Wwire is not None
            and isnan(other._Wwire)
            and isnan(self._Wwire)
        ):
            pass
        elif other._Wwire != self._Wwire:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Wwire) + ", other=" + str(other._Wwire) + ")"
                )
                diff_list.append(name + ".Wwire" + val_str)
            else:
                diff_list.append(name + ".Wwire")
        if (
            other._Wins_cond is not None
            and self._Wins_cond is not None
            and isnan(other._Wins_cond)
            and isnan(self._Wins_cond)
        ):
            pass
        elif other._Wins_cond != self._Wins_cond:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Wins_cond)
                    + ", other="
                    + str(other._Wins_cond)
                    + ")"
                )
                diff_list.append(name + ".Wins_cond" + val_str)
            else:
                diff_list.append(name + ".Wins_cond")
        if other._Nwppc_rad != self._Nwppc_rad:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Nwppc_rad)
                    + ", other="
                    + str(other._Nwppc_rad)
                    + ")"
                )
                diff_list.append(name + ".Nwppc_rad" + val_str)
            else:
                diff_list.append(name + ".Nwppc_rad")
        if other._Nwppc_tan != self._Nwppc_tan:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Nwppc_tan)
                    + ", other="
                    + str(other._Nwppc_tan)
                    + ")"
                )
                diff_list.append(name + ".Nwppc_tan" + val_str)
            else:
                diff_list.append(name + ".Nwppc_tan")
        if (
            other._Wins_wire is not None
            and self._Wins_wire is not None
            and isnan(other._Wins_wire)
            and isnan(self._Wins_wire)
        ):
            pass
        elif other._Wins_wire != self._Wins_wire:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Wins_wire)
                    + ", other="
                    + str(other._Wins_wire)
                    + ")"
                )
                diff_list.append(name + ".Wins_wire" + val_str)
            else:
                diff_list.append(name + ".Wins_wire")
        if (
            other._Kwoh is not None
            and self._Kwoh is not None
            and isnan(other._Kwoh)
            and isnan(self._Kwoh)
        ):
            pass
        elif other._Kwoh != self._Kwoh:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Kwoh) + ", other=" + str(other._Kwoh) + ")"
                )
                diff_list.append(name + ".Kwoh" + val_str)
            else:
                diff_list.append(name + ".Kwoh")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Conductor
        S += super(CondType13, self).__sizeof__()
        S += getsizeof(self.Wwire)
        S += getsizeof(self.Wins_cond)
        S += getsizeof(self.Nwppc_rad)
        S += getsizeof(self.Nwppc_tan)
        S += getsizeof(self.Wins_wire)
        S += getsizeof(self.Kwoh)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Conductor
        CondType13_dict = super(CondType13, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        CondType13_dict["Wwire"] = self.Wwire
        CondType13_dict["Wins_cond"] = self.Wins_cond
        CondType13_dict["Nwppc_rad"] = self.Nwppc_rad
        CondType13_dict["Nwppc_tan"] = self.Nwppc_tan
        CondType13_dict["Wins_wire"] = self.Wins_wire
        CondType13_dict["Kwoh"] = self.Kwoh
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        CondType13_dict["__class__"] = "CondType13"
        return CondType13_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.Wwire = None
        self.Wins_cond = None
        self.Nwppc_rad = None
        self.Nwppc_tan = None
        self.Wins_wire = None
        self.Kwoh = None
        # Set to None the properties inherited from Conductor
        super(CondType13, self)._set_None()

    def _get_Wwire(self):
        """getter of Wwire"""
        return self._Wwire

    def _set_Wwire(self, value):
        """setter of Wwire"""
        check_var("Wwire", value, "float", Vmin=0)
        self._Wwire = value

    Wwire = property(
        fget=_get_Wwire,
        fset=_set_Wwire,
        doc=u"""cf schematics, single wire diameter without insulation [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Wins_cond(self):
        """getter of Wins_cond"""
        return self._Wins_cond

    def _set_Wins_cond(self, value):
        """setter of Wins_cond"""
        check_var("Wins_cond", value, "float", Vmin=0)
        self._Wins_cond = value

    Wins_cond = property(
        fget=_get_Wins_cond,
        fset=_set_Wins_cond,
        doc=u"""(advanced) cf schematics, winding coil insulation diameter [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Nwppc_rad(self):
        """getter of Nwppc_rad"""
        return self._Nwppc_rad

    def _set_Nwppc_rad(self, value):
        """setter of Nwppc_rad"""
        check_var("Nwppc_rad", value, "int", Vmin=1)
        self._Nwppc_rad = value

    Nwppc_rad = property(
        fget=_get_Nwppc_rad,
        fset=_set_Nwppc_rad,
        doc=u"""cf schematics, stator winding number of preformed wires (strands) in parallel per coil along radial (vertical) direction

        :Type: int
        :min: 1
        """,
    )

    def _get_Nwppc_tan(self):
        """getter of Nwppc_tan"""
        return self._Nwppc_tan

    def _set_Nwppc_tan(self, value):
        """setter of Nwppc_tan"""
        check_var("Nwppc_tan", value, "int", Vmin=1)
        self._Nwppc_tan = value

    Nwppc_tan = property(
        fget=_get_Nwppc_tan,
        fset=_set_Nwppc_tan,
        doc=u"""cf schematics, stator winding number of preformed wires (strands) in parallel per coil along tangential (horizontal) direction

        :Type: int
        :min: 1
        """,
    )

    def _get_Wins_wire(self):
        """getter of Wins_wire"""
        return self._Wins_wire

    def _set_Wins_wire(self, value):
        """setter of Wins_wire"""
        check_var("Wins_wire", value, "float", Vmin=0)
        self._Wins_wire = value

    Wins_wire = property(
        fget=_get_Wins_wire,
        fset=_set_Wins_wire,
        doc=u"""(advanced) cf schematics, winding strand insulation thickness [m]

        :Type: float
        :min: 0
        """,
    )

    def _get_Kwoh(self):
        """getter of Kwoh"""
        return self._Kwoh

    def _set_Kwoh(self, value):
        """setter of Kwoh"""
        check_var("Kwoh", value, "float", Vmin=0)
        self._Kwoh = value

    Kwoh = property(
        fget=_get_Kwoh,
        fset=_set_Kwoh,
        doc=u"""winding overhang factor which describes the fact that random round wire end-windings can be more or less compressed (0.5 for small motors, 0.8 for large motors) - can be used to tune the average turn length (relevant if type_cond==1)

        :Type: float
        :min: 0
        """,
    )
