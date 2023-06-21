#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "interface.hpp"

PYBIND11_MODULE(libtf, m) {
    m.def("add_frame", &add_frame, "Add two frames");
    m.def("inv_frame", &inv_frame, "Inverse frame");
}
