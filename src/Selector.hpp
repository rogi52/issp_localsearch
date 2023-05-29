#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <random>

#include "Indicator.hpp"
#include "Time.hpp"

class Selector {
  private:
    vector<vector<double>> point_set;
    int point_set_size;
    int point_subset_size;
    int d;
    mt19937 rnd_engine;
    int nlist_size;
    int rlist_size;

  public:
    Indicator I;
    Selector(vector<vector<double>>& point_set, int point_subset_size, Indicator &I, mt19937 rnd_engine, int nlist_size, int rlist_size);
    vector<vector<double>> select(string algorithm);
    vector<vector<double>> local_search();
    vector<vector<double>> local_search_with_nearest_list();
    vector<vector<double>> local_search_with_random_list();
    vector<vector<double>> two_phase_local_search();
};