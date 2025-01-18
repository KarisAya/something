#include <Python.h>

typedef struct
{
    PyObject_HEAD int value;
} Int32;
static PyObject *newInt32(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Int32 *self = (Int32 *)type->tp_alloc(type, 0);
    if (self == NULL)
    {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory");
        return NULL;
    }
    self->value = 0;
    return (PyObject *)self;
}
static int initInt32(Int32 *self, PyObject *args, PyObject *kwds)
{
    if (!PyArg_ParseTuple(args, "i", &self->value))
        self->value = 0;
    return 0;
}
#define Int32Check(arg)                                            \
    int value;                                                     \
    if (PyObject_TypeCheck(arg, &Int32Type))                       \
        value = ((Int32 *)arg)->value;                             \
    else if (PyLong_Check(arg))                                    \
        value = (int)PyLong_AsLong(arg);                           \
    else if (PyFloat_Check(arg))                                   \
        value = (int)PyFloat_AsDouble(arg);                        \
    else                                                           \
    {                                                              \
        PyErr_SetString(PyExc_TypeError, "Invalid argument type"); \
        return NULL;                                               \
    }

#define Int32newResult                                                   \
    Int32 *result = (Int32 *)PyObject_New(Int32, &Int32Type);            \
    if (result == NULL)                                                  \
    {                                                                    \
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory"); \
        return NULL;                                                     \
    }

static PyTypeObject Int32Type;
static PyObject *Int32_add(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        Int32newResult
            result->value = self->value + value;
    return (PyObject *)result;
}
static PyObject *Int32_iadd(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        self->value += value;
    Py_INCREF(self);
    return (PyObject *)self;
}
static PyObject *Int32_subtract(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        Int32newResult
            result->value = self->value - value;
    return (PyObject *)result;
}
static PyObject *Int32_isubtract(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        self->value -= value;
    Py_INCREF(self);
    return (PyObject *)self;
}
static PyObject *Int32_multiply(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        Int32newResult
            result->value = self->value * value;
    return (PyObject *)result;
}
static PyObject *Int32_imultiply(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        self->value *= value;
    Py_INCREF(self);
    return (PyObject *)self;
}
static PyObject *Int32_divide(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        Int32newResult
            result->value = self->value / value;
    return (PyObject *)result;
}
static PyObject *Int32_idivide(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        self->value /= value;
    Py_INCREF(self);
    return (PyObject *)self;
}
static PyObject *Int32_remainder(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        Int32newResult
            result->value = self->value % value;
    return (PyObject *)result;
}
static PyObject *Int32_iremainder(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        self->value %= value;
    Py_INCREF(self);
    return (PyObject *)self;
}
static PyObject *Int32_power(Int32 *self, PyObject *arg)
{
    Int32Check(arg)
        Int32newResult
            result->value = 1;
    for (int i = 0; i < value; i++)
    {
        result->value *= self->value;
    }
    return (PyObject *)result;
}
static PyObject *Int32_ipower(Int32 *self, PyObject *arg)
{
    Int32Check(arg) int selfValue = self->value;
    self->value = 1;
    for (int i = 0; i < value; i++)
    {
        self->value *= selfValue;
    }
    Py_INCREF(self);
    return (PyObject *)self;
}
static PyNumberMethods Int32_as_number = {
    .nb_add = (binaryfunc)Int32_add,
    .nb_inplace_add = (binaryfunc)Int32_iadd,
    .nb_subtract = (binaryfunc)Int32_subtract,
    .nb_inplace_subtract = (binaryfunc)Int32_isubtract,
    .nb_multiply = (binaryfunc)Int32_multiply,
    .nb_inplace_multiply = (binaryfunc)Int32_imultiply,
    .nb_true_divide = (binaryfunc)Int32_divide,
    .nb_inplace_true_divide = (binaryfunc)Int32_idivide,
    .nb_remainder = (binaryfunc)Int32_remainder,
    .nb_inplace_remainder = (binaryfunc)Int32_iremainder,
    .nb_power = (binaryfunc)Int32_power,
    .nb_inplace_power = (binaryfunc)Int32_ipower,

};

static int Int32_setattr(Int32 *self, const char *name, PyObject *value)
{
    if (strcmp(name, "value") == 0)
    {
        if (value == NULL)
        {
            PyErr_SetString(PyExc_TypeError, "Cannot delete the 'value' attribute");
            return -1;
        }
        if (!PyLong_Check(value))
        {
            PyErr_SetString(PyExc_TypeError, "The 'value' attribute must be an integer");
            return -1;
        }
        self->value = (int)PyLong_AsLong(value);
        return 0;
    }
    return PyObject_GenericSetAttr((PyObject *)self, name, value);
}

// 定义字符串表示
static PyObject *MyInt_repr(Int32 *self)
{
    return PyUnicode_FromFormat("Int32(%d)", self->value);
}

static PyTypeObject Int32Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "myctypes.Int32",
    .tp_doc = "Int32 objects",
    .tp_basicsize = sizeof(Int32),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = newInt32,
    .tp_init = (initproc)initInt32,
    .tp_repr = (reprfunc)MyInt_repr,
    .tp_setattr = (setattrfunc)Int32_setattr,
    .tp_as_number = &Int32_as_number,
};

// 模块方法
static PyMethodDef moduleMethods[] = {
    {NULL} // 结束标志
};

// 模块定义
static struct PyModuleDef myctypes = {
    PyModuleDef_HEAD_INIT,
    .m_name = "myctypes",
    .m_doc = "module 编写示范",
    .m_size = -1,
    .m_methods = moduleMethods,
};

// 模块初始化函数
PyMODINIT_FUNC PyInit_myctypes(void)
{
    PyObject *m;
    if (PyType_Ready(&Int32Type) < 0)
        return NULL;
    m = PyModule_Create(&myctypes);
    if (m == NULL)
        return NULL;
    Py_INCREF(&Int32Type);
    if (PyModule_AddObject(m, "Int32", (PyObject *)&Int32Type) < 0)
    {
        Py_DECREF(&Int32Type);
        Py_DECREF(m);
        return NULL;
    }
    return m;
}