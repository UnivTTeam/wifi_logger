#include <vector>

#include "libwheels/transform2d/transform2d.hpp"

inline Transform::MultidiffTransform<double, 1> framenize(const std::vector<double>& x)
{
    Transform::StaticTransform<double> static_frame(x[0], x[1], x[2]);
    Transform::DynamicTransform<double> dynamic_frame(0., 0., 0.);
    if(x.size() > 3){
        dynamic_frame = Transform::DynamicTransform<double>(x[3], x[4], x[5]);
    }
    return Transform::MultidiffTransform<double, 1>(static_frame, dynamic_frame);
}

inline std::vector<double> vectorize(const Transform::MultidiffTransform<double, 1>& frame)
{
    std::vector<double> v(6);
    v[0] = frame.static_frame.pos.x;
    v[1] = frame.static_frame.pos.y;
    v[2] = frame.static_frame.rot.getAngle();
    v[3] = frame.dynamic_frame[0].pos.x;
    v[4] = frame.dynamic_frame[0].pos.y;
    v[5] = frame.dynamic_frame[0].rot;
    return v;
}

inline std::vector<double> add_frame(const std::vector<double>& x, const std::vector<double>& y) {
    auto frame = framenize(x) + framenize(y);
    return vectorize(frame);
}

inline std::vector<double> inv_frame(const std::vector<double>& x){
    auto frame = -framenize(x);
    return vectorize(frame);
}
