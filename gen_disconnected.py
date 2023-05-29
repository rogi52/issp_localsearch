#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import itertools
import click

@click.command()
@click.option('--n_obj', '-d', type = int)
@click.option('--grid_size', '-g', type = int)
def cmd(n_obj, grid_size):
    if n_obj == 2:
        create_ref_points_disconnected_2d(grid_size)
    else:
        create_ref_points_disconnected(n_obj, grid_size)


def create_ref_points_disconnected(n_obj, grid_size):
    pf_shape = 'disconnected'

    interval = [0,0.251412,0.631627,0.859401]
    median = (interval[1] - interval[0]) / (interval[3] - interval[2] + interval[1] - interval[0])

    x = np.linspace(0, 1, grid_size)
    l = list(itertools.product(x, repeat=n_obj-1))
    grid_point_set = np.array(l)
    grid_point_set = np.where(grid_point_set <= median, grid_point_set * (interval[1] - interval[0]) / median + interval[0], (grid_point_set  - median) * (interval[3] - interval[2]) / (1 - median) + interval[2])

    obj_point_set = []
    for point in grid_point_set:
        mth_p = 0
        for p in point:
            mth_p += (p/2) * (1.0 + np.sin(3 * np.pi * p))
        mth_p = 2 * (n_obj - mth_p)
        obj_point_set.append(np.append(point, mth_p))

    for d in range(n_obj):
        f_d = []
        for i in range(len(obj_point_set)):
            f_d.append(obj_point_set[i][d])

        MIN = min(f_d)
        MAX = max(f_d)

        for i in range(len(obj_point_set)):
            obj_point_set[i][d] = (obj_point_set[i][d] - MIN) / (MAX - MIN)

    n_ref_points = len(obj_point_set)
    ref_point_dir_path = './ref_point_dataset'
    os.makedirs(ref_point_dir_path, exist_ok=True)
    ref_point_file_path = os.path.join(ref_point_dir_path, '{}_d{}_n{}.csv'.format(pf_shape, n_obj, n_ref_points))
    np.savetxt(ref_point_file_path, np.array(obj_point_set), delimiter=',')

    print(f'generated : pf = {pf_shape}, d = {n_obj}, n = {n_ref_points}')

def create_ref_points_disconnected_2d(grid_size):
    pf_shape = 'disconnected'
    n_obj = 2

    x = np.linspace(0, 2.116426807, grid_size)

    x1_ranges = [
        [0, 0.2514118360],
        [0.6316265307, 0.8594008566],
        [1.3596178367, 1.5148392681],
        [2.0518383519, 2.116426807]
    ]

    obj_point_set = []
    for x1 in x:
        for r in x1_ranges:
            if r[0] <= x1 <= r[1]:
                x2 = 4 - (x1 * (1 + np.sin(3 * np.pi * x1)))
                obj_point_set.append(np.array([x1, x2]))
                break

    x0_min = 0.0
    x0_max = 2.116426807
    x1_min = 0.0
    x1_max = 4.0
    for i in range(len(obj_point_set)):
        obj_point_set[i][0] = (obj_point_set[i][0] - x0_min) / (x0_max - x0_min)
        obj_point_set[i][1] = (obj_point_set[i][1] - x1_min) / (x1_max - x1_min)

    n_ref_points = len(obj_point_set)
    ref_point_dir_path = './ref_point_dataset'
    os.makedirs(ref_point_dir_path, exist_ok=True)
    ref_point_file_path = os.path.join(ref_point_dir_path, '{}_d{}_n{}.csv'.format(pf_shape, n_obj, n_ref_points))
    np.savetxt(ref_point_file_path, np.array(obj_point_set), delimiter=',')

    print(f'generated : pf = {pf_shape}, d = {n_obj}, n = {n_ref_points}')

def main():
    cmd()

if __name__ == '__main__':
    main()
