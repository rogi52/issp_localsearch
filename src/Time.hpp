#pragma once
#include <vector>
#include <iostream>
#include <chrono>
#include <assert.h>

class Time {
  public:
    
    void start();
    void end();
    enum { MILLISECONDS, SECONDS, MINUTES, HOURS };
    long long get(int type);

  private:
    using TP = std::chrono::system_clock::time_point;
    TP start_time;
    bool is_working = false;
    long long cast_milliseconds(TP now);
    long long cast_seconds(TP now);
    long long cast_minutes(TP now);
    long long cast_hours(TP now);
};