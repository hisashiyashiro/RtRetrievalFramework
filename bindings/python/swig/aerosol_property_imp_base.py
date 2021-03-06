# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _aerosol_property_imp_base.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_aerosol_property_imp_base')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_aerosol_property_imp_base')
    _aerosol_property_imp_base = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_aerosol_property_imp_base', [dirname(__file__)])
        except ImportError:
            import _aerosol_property_imp_base
            return _aerosol_property_imp_base
        try:
            _mod = imp.load_module('_aerosol_property_imp_base', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _aerosol_property_imp_base = swig_import_helper()
    del swig_import_helper
else:
    import _aerosol_property_imp_base
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _aerosol_property_imp_base.SHARED_PTR_DISOWN

def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.aerosol_property
import full_physics_swig.observer
import full_physics_swig.generic_object
import full_physics_swig.state_vector
class SubStateVectorArrayAerosolProperty(full_physics_swig.aerosol_property.AerosolProperty, full_physics_swig.state_vector.SubStateVectorObserver):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol_property_imp_base.delete_SubStateVectorArrayAerosolProperty

    @property
    def coefficient(self):
        return self._v_coefficient()


    @property
    def used_flag_value(self):
        return self._v_used_flag_value()


    @property
    def statevector_covariance(self):
        return self._v_statevector_covariance()


    @property
    def pressure(self):
        return self._v_pressure()

SubStateVectorArrayAerosolProperty.init = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_init, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty.state_vector_name_i = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_state_vector_name_i, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty.update_sub_state_hook = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_update_sub_state_hook, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty._v_coefficient = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_coefficient, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty._v_used_flag_value = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_used_flag_value, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty._v_statevector_covariance = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_statevector_covariance, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty._v_pressure = new_instancemethod(_aerosol_property_imp_base.SubStateVectorArrayAerosolProperty__v_pressure, None, SubStateVectorArrayAerosolProperty)
SubStateVectorArrayAerosolProperty_swigregister = _aerosol_property_imp_base.SubStateVectorArrayAerosolProperty_swigregister
SubStateVectorArrayAerosolProperty_swigregister(SubStateVectorArrayAerosolProperty)

class AerosolPropertyImpBase(SubStateVectorArrayAerosolProperty):
    """

    As a design principle, we have each base class with the absolutely
    minimum interface needed for use from the rest of the system.

    This allows us to support any future code that supports this minimum
    interface.

    However, almost always you will want to derive from this class
    instead. See PressureImpBase for a more complete discussion of this.

    C++ includes: aerosol_property_imp_base.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _aerosol_property_imp_base.delete_AerosolPropertyImpBase

    def clone(self, *args):
        """

        virtual boost::shared_ptr<AerosolProperty> FullPhysics::AerosolPropertyImpBase::clone(const boost::shared_ptr< Pressure > &Press, const boost::shared_ptr<
        RelativeHumidity > &Rh) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_clone(self, *args)


    def extinction_coefficient_each_layer(self, wn):
        """

        virtual ArrayAd<double,1> FullPhysics::AerosolPropertyImpBase::extinction_coefficient_each_layer(double wn) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_extinction_coefficient_each_layer(self, wn)


    def scattering_coefficient_each_layer(self, wn):
        """

        virtual ArrayAd<double, 1> FullPhysics::AerosolPropertyImpBase::scattering_coefficient_each_layer(double wn) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_scattering_coefficient_each_layer(self, wn)


    def phase_function_moment_each_layer(self, wn, nmom=-1, nscatt=-1):
        """

        virtual ArrayAd<double, 3> FullPhysics::AerosolPropertyImpBase::phase_function_moment_each_layer(double wn, int nmom=-1, int nscatt=-1) const =0

        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_phase_function_moment_each_layer(self, wn, nmom, nscatt)


    def desc(self):
        """

        virtual std::string FullPhysics::AerosolPropertyImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_desc(self)


    def print_desc(self, Os):
        """

        virtual void FullPhysics::AerosolPropertyImpBase::print(std::ostream &Os) const
        Print to stream.

        The default calls the function "desc" that returns a string. This
        gives cleaner interface for deriving from this class in python, but
        most C++ classes will want to override this function rather than using
        desc. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase_print_desc(self, Os)


    def _v_desc(self):
        """

        virtual std::string FullPhysics::AerosolPropertyImpBase::desc() const
        Description of object, to be printed to stream.

        This gives a cleaner interface for deriving from python. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase__v_desc(self)


    @property
    def desc(self):
        return self._v_desc()


    def _v_aerosol_parameter(self):
        """

        blitz::Array<double, 1> FullPhysics::AerosolPropertyImpBase::aerosol_parameter() const
        Returns the value of the coefficients used to generate the aerosol
        property. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase__v_aerosol_parameter(self)


    @property
    def aerosol_parameter(self):
        return self._v_aerosol_parameter()


    def _v_aerosol_parameter_uncertainty(self):
        """

        blitz::Array<double, 1> FullPhysics::AerosolPropertyImpBase::aerosol_parameter_uncertainty() const
        Returns the uncertainty of the aerosol type coefficients. 
        """
        return _aerosol_property_imp_base.AerosolPropertyImpBase__v_aerosol_parameter_uncertainty(self)


    @property
    def aerosol_parameter_uncertainty(self):
        return self._v_aerosol_parameter_uncertainty()


    def __init__(self, *args):
        if self.__class__ == AerosolPropertyImpBase:
            _self = None
        else:
            _self = self
        _aerosol_property_imp_base.AerosolPropertyImpBase_swiginit(self, _aerosol_property_imp_base.new_AerosolPropertyImpBase(_self, *args))
    def __disown__(self):
        self.this.disown()
        _aerosol_property_imp_base.disown_AerosolPropertyImpBase(self)
        return weakref_proxy(self)
AerosolPropertyImpBase.clone = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_clone, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.extinction_coefficient_each_layer = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_extinction_coefficient_each_layer, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.scattering_coefficient_each_layer = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_scattering_coefficient_each_layer, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.phase_function_moment_each_layer = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_phase_function_moment_each_layer, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.desc = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_desc, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.add_observer = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_add_observer, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.remove_observer = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_remove_observer, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.update_sub_state_hook = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_update_sub_state_hook, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.print_desc = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_print_desc, None, AerosolPropertyImpBase)
AerosolPropertyImpBase._v_desc = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase__v_desc, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.mark_used = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_mark_used, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.state_vector_name = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_state_vector_name, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.notify_update = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_notify_update, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.notify_add = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_notify_add, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.notify_remove = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_notify_remove, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.update_sub_state = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_update_sub_state, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.state_vector_name_i = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_state_vector_name_i, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.state_vector_name_sub = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_state_vector_name_sub, None, AerosolPropertyImpBase)
AerosolPropertyImpBase._v_aerosol_parameter = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase__v_aerosol_parameter, None, AerosolPropertyImpBase)
AerosolPropertyImpBase._v_aerosol_parameter_uncertainty = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase__v_aerosol_parameter_uncertainty, None, AerosolPropertyImpBase)
AerosolPropertyImpBase.init = new_instancemethod(_aerosol_property_imp_base.AerosolPropertyImpBase_init, None, AerosolPropertyImpBase)
AerosolPropertyImpBase_swigregister = _aerosol_property_imp_base.AerosolPropertyImpBase_swigregister
AerosolPropertyImpBase_swigregister(AerosolPropertyImpBase)



