g++ -O3 -shared -std=c++17 -fPIC `python3 -m pybind11 --includes` bind.cpp -o libtf`python3-config --extension-suffix`
mv libtf.cpython-310-x86_64-linux-gnu.so ../
