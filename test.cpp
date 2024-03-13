#include <vector>

std::vector<int>* rapid_mult_cpp(std::vector<int>* x, std::vector<int>* y) {
    std::vector<int>* return_vector = new std::vector<int>();
    for (int i = 0; i < std::max(x->size(), y->size()); i++) {
        if (x->size() <= i || y->size() <= i) {
            return_vector->push_back(0);
            continue;
        }
        return_vector->push_back((x->at(i))*(y->at(i)));
    }
    return return_vector;
}

extern "C" {
    std::vector<int>* rapid_mult(std::vector<int>* x, std::vector<int>* y) {
        return rapid_mult_cpp(x, y);
    }
}