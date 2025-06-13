#include "pocketpy/common/name.h"
#include <string.h>
#include <atomic>
#include <thread>
#include <map>

#include <godot_cpp/variant/string_name.hpp>

using namespace godot;

static struct CachedNames{
    std::map<py_Name, CharString> map;  // must use std::map to ensure iterators are stable
    std::atomic_flag lock;
}* cached_names;


extern "C" {

#define MAGIC_METHOD(x) py_Name x;
#include "pocketpy/xmacros/magics.h"
#undef MAGIC_METHOD
    
void pk_names_initialize() {
    cached_names = new CachedNames;
    cached_names->lock.clear();
}

void pk_names_finalize() {
    delete cached_names;
}

py_Name py_namev(c11_sv name){
    StringName sn(String::utf8(name.data, name.size));
    void* ptr = sn._native_ptr();
    py_Name retval;
    memcpy(&retval, ptr, sizeof(py_Name));
    return retval;
}

c11_sv py_name2sv(py_Name index){
    StringName sn;
    memcpy(&sn, &index, sizeof(py_Name));
    while (cached_names->lock.test_and_set()) {
        std::this_thread::yield();
    }
    auto it = cached_names->map.find(index);
    if (it == cached_names->map.end()) {
        CharString cs = String(sn).utf8();
        it = cached_names->map.insert({index, cs}).first;
    }
    c11_sv sv;
    sv.data = it->second.get_data();
    sv.size = (int)it->second.length();
    cached_names->lock.clear();
    return sv;
}

py_Name py_name(const char* name){
    StringName sn(name);
    void* ptr = sn._native_ptr();
    py_Name retval;
    memcpy(&retval, ptr, sizeof(py_Name));
    return retval;
}

const char* py_name2str(py_Name index){
    return py_name2sv(index).data;
}

}