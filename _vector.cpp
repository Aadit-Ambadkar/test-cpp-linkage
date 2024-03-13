#include <vector>

extern "C" {
    std::vector<int>* _create(){
        return new std::vector<int>;
    }
    void _delete(std::vector<int>* v){
        delete v;
    }
    int _size(std::vector<int>* v){
        return v->size();
    }
    int _get(std::vector<int>* v, int i){
        return v->at(i);
    }
    void _push_back(std::vector<int>* v, int i){
        v->push_back(i);
    }
}