# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_raxml', [dirname(__file__)])
        except ImportError:
            import _raxml
            return _raxml
        if fp is not None:
            try:
                _mod = imp.load_module('_raxml', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _raxml = swig_import_helper()
    del swig_import_helper
else:
    import _raxml
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


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
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def new_analdef():
    return _raxml.new_analdef()
new_analdef = _raxml.new_analdef

def delete_analdef(adef):
    return _raxml.delete_analdef(adef)
delete_analdef = _raxml.delete_analdef

def new_tree():
    return _raxml.new_tree()
new_tree = _raxml.new_tree

def delete_tree(tr):
    return _raxml.delete_tree(tr)
delete_tree = _raxml.delete_tree

def read_tree(treeFile, tr, adef):
    return _raxml.read_tree(treeFile, tr, adef)
read_tree = _raxml.read_tree

def tree_to_string(tr, adef):
    return _raxml.tree_to_string(tr, adef)
tree_to_string = _raxml.tree_to_string

def init_adef(adef):
    return _raxml.init_adef(adef)
init_adef = _raxml.init_adef

def init_program(adef, tr, argc):
    return _raxml.init_program(adef, tr, argc)
init_program = _raxml.init_program

def optimize_model(adef, tr):
    return _raxml.optimize_model(adef, tr)
optimize_model = _raxml.optimize_model

def compute_best_LH(tr):
    return _raxml.compute_best_LH(tr)
compute_best_LH = _raxml.compute_best_LH

def delete_best_vector(bestVector):
    return _raxml.delete_best_vector(bestVector)
delete_best_vector = _raxml.delete_best_vector

def compute_LH(adef, tr, bestLH, weightSum, bestVector):
    return _raxml.compute_LH(adef, tr, bestLH, weightSum, bestVector)
compute_LH = _raxml.compute_LH
# This file is compatible with both classic and new-style classes.


