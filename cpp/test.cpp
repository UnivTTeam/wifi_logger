#include <iostream>
#include "libwheels/transform2d/transform2d.hpp"

using std::cout;
using std::endl;

#define CPP_TEST

#include "util.hpp"
#include "interface.hpp"

int main()
{
  Transform::StaticTransform<double> pos(2.0, 3.0, M_PI / 3.0);
  Transform::DynamicTransform<double> vel(5.0, 20., 1.0);

  Transform::MultidiffTransform<double, 1> frame(pos, vel);

  Transform::StaticTransform<double> sub_pos(20.0, -40.0, -M_PI / 2.0);
  auto sub_frame = frame + sub_pos;
  std::vector<double> a{{2.0, 3.0, M_PI / 3.0, 5.0, 20., 1.0}};
  std::vector<double> b{{20.0, -40.0, -M_PI / 2.0}};
  auto sub_frame2 = framenize(add_frame(a, b));
  
  print(sub_frame);
  print(sub_frame2);

  auto recalc_frame = sub_frame + (-sub_pos);
  std::vector<double> c{{20.0, -40.0, -M_PI / 2.0}};
  auto inv = framenize(inv_frame(c));
  auto recalc_frame2 = sub_frame + inv;
  print(recalc_frame);
  print(recalc_frame2);

  print(frame);
}
