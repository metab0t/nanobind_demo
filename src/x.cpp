#include <vector>

#include <nanobind/nanobind.h>
#include <nanobind/operators.h>
#include <nanobind/stl/vector.h>

namespace nb = nanobind;

struct S
{
    std::vector<double> vec;

    void push_back(double x)
    {
        vec.push_back(x);
    }

    void clear()
    {
        vec.clear();
    }

    S& operator+=(double x)
    {
        push_back(x);
        return *this;
    }
};

NB_MODULE(ext, m)
{
	nb::class_<S>(m, "S")
	    .def(nb::init<>())
	    .def("push_back", &S::push_back)
        .def("clear", &S::clear)
	    .def(nb::self += double());
}