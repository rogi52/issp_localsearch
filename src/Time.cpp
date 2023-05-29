#include "Time.hpp"

void Time::start() {
    start_time = std::chrono::system_clock::now();
    is_working = true;
}

void Time::end() { is_working = false; }

long long Time::get(int type) {
    assert(is_working);
    auto now = std::chrono::system_clock::now();
    switch(type) {
        case MILLISECONDS: return cast_milliseconds(now);
        case SECONDS:      return cast_seconds(now);
        case MINUTES:      return cast_minutes(now);
        case HOURS:        return cast_hours(now);
        default:
            std::cout << type << " is not defined" << std::endl;
            exit(1);
    }
}

long long Time::cast_milliseconds(TP now) {
    return std::chrono::duration_cast<std::chrono::milliseconds>(now - start_time).count();
}

long long Time::cast_seconds(std::chrono::system_clock::time_point now) {
    return std::chrono::duration_cast<std::chrono::seconds>(now - start_time).count();
}

long long Time::cast_minutes(std::chrono::system_clock::time_point now) {
    return std::chrono::duration_cast<std::chrono::minutes>(now - start_time).count();
}

long long Time::cast_hours(std::chrono::system_clock::time_point now) {
    return std::chrono::duration_cast<std::chrono::hours>(now - start_time).count();
}