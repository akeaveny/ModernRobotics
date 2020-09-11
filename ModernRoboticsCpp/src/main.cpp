#include "../include/modern_robotics.h"

#include <Eigen/Dense>
#include <cmath>
#include <iostream>
#include <vector>

constexpr double pi { 3.14159 };

int main() {
  Eigen::VectorXd twist_vec_(6);
  twist_vec_(0) = 0;
  twist_vec_(1) = 1;
  twist_vec_(2) = 1;
  twist_vec_(3) = 3;
  twist_vec_(4) = 10;
  twist_vec_(5) = 10;
  twist_vec_ = twist_vec_ * pi / (2 * sqrt(2));
  std::cout << "twist_vec_\n" << twist_vec_ << std::endl;

  Eigen::MatrixXd twist_skew_ = mr::VecTose3(twist_vec_);
  std::cout << "twist_skew_:\n" << twist_skew_ << std::endl;

  Eigen::MatrixXd exp_twist_ = mr::MatrixExp6(twist_skew_);
  std::cout << "exp_twist_:\n" << exp_twist_ << std::endl;

  return 0;
}