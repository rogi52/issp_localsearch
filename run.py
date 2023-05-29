import numpy as np
import subprocess
import os

class PointSet():
    def __init__(self, num_of_obj, size, pf_shape):
        self.num_of_obj = num_of_obj
        self.size = size
        self.pf_shape = pf_shape

class Indicator():
    def __init__(self, name, ref_point = 1.1, ref_point_set = 1000, weight_point_set = 1000):
        # need = [ref_point, ref_point_set, weight_point_set]
        self.name = name
        if name == 'hv':
            self.need = [True, False, False]
            self.ref_point = ref_point
        if name == 'epsilon':
            self.need = [False, True, False]
            self.ref_point_set = ref_point_set
        if name == 'igd':
            self.need = [False, True, False]
            self.ref_point_set = ref_point_set
        if name == 'igd+':
            self.need = [False, True, False]
            self.ref_point_set = ref_point_set
        if name == 'r2':
            self.need = [False, False, True]
            self.weight_point_set = weight_point_set
        if name == 'nr2':
            self.need = [True, False, True]
            self.ref_point = ref_point
            self.weight_point_set = weight_point_set
        if name == 'senergy':
            self.need = [False, False, False]

class Selector():
    def __init__(self, name, nlist_size = 20, rlist_size = 20):
        self.name = name
        if name == 'fils-nlist':
            self.nlist_size = nlist_size
        if name == 'fils-rlist':
            self.rlist_size = rlist_size
        if name == 'fils-rlist-nlist':
            self.nlist_size = nlist_size
            self.rlist_size = rlist_size


def issp_experiment(point_set, point_subset_size, indicator, selector, run_id):

    for P in point_set:
        for k in point_subset_size:
            for I in indicator:
                for A in selector:
                    for id in run_id:
                        pf = P.pf_shape
                        d = P.num_of_obj
                        n = P.size

                        point_set_file_path = f'./ref_point_dataset/{pf}_d{d}_n{n}.csv'
                        ref_point_set_file_path = f'./ref_point_dataset/{pf}_d{d}_n1000.csv'
                        res_dir_path = os.path.join('./result', f'{A.name}', f'pf-{pf}_d{d}_n{n}_k{k}_I-{I.name}')

                        need_r, need_R, need_W = I.need
                        if need_r:
                            res_dir_path += f'-{I.ref_point}'
                        if A.name == 'fils-nlist':
                            res_dir_path += f'_c{A.nlist_size}'
                        if A.name == 'fils-rlist':
                            res_dir_path += f'_r{A.rlist_size}'
                        if A.name == 'fils-rlist-nlist':
                            res_dir_path += f'_c{A.nlist_size}_r{A.rlist_size}'

                        os.makedirs(res_dir_path, exist_ok = True)

                        out_point_subset_file_path = os.path.join(res_dir_path, f'subset_{id}th_run.csv')
                        out_qi_file_path = os.path.join(res_dir_path, f'qi_{id}th_run.csv')
                        out_time_file_path = os.path.join(res_dir_path, f'time_{id}th_run.csv')
                        out_n_qi_calls_file_path = os.path.join(res_dir_path, f'n_qi_calls_{id}th_run.csv')

                        args = ['./selector']
                        args.append(f'-point_set_file_path {point_set_file_path}')
                        args.append(f'-point_subset_size {k}')
                        args.append(f'-q_indicator {I.name}')
                        args.append(f'-selector_alg {A.name}')
                        args.append(f'-seed {id}')
                        args.append(f'-out_point_subset_file_path {out_point_subset_file_path}')
                        args.append(f'-out_qi_file_path {out_qi_file_path}')
                        args.append(f'-out_time_file_path {out_time_file_path}')
                        args.append(f'-out_n_qi_calls_file_path {out_n_qi_calls_file_path}')
                        if need_r:
                            args.append(f'-hv_ref_point_val {I.ref_point}')
                        if need_R:
                            args.append(f'-ref_point_set_file_path {ref_point_set_file_path}')
                        if need_W:
                            args.append(f'-weight_point_set_file_path ./weight_point_dataset/d{d}_n{I.weight_point_set}.csv')
                        if A.name == 'fils-nlist':
                            args.append(f'-nlist_size {A.nlist_size}')
                        if A.name == 'fils-rlist':
                            args.append(f'-rlist_size {A.rlist_size}')
                        if A.name == 'fils-rlist-nlist':
                            args.append(f'-nlist_size {A.nlist_size}')
                            args.append(f'-rlist_size {A.rlist_size}')

                        #subprocess.run(' '.join(args), shell = True)
                        print(' '.join(args))

if __name__ == '__main__':

    """
    Ps = []
    for pf_shape in ['linear', 'nonconvex', 'convex', 'inverted-linear', 'inverted-nonconvex', 'inverted-convex']:
        for d in [2, 3, 4, 5, 6]:
            for n in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
                Ps.append(PointSet(pf_shape = pf_shape, num_of_obj = d, size = n))
    for n in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        Ps.append(PointSet(pf_shape = 'disconnected', num_of_obj = 2, size = n))
    for n in [961, 2025, 3025, 4096, 5041, 6084, 7056, 8100, 9025, 10000]:
        Ps.append(PointSet(pf_shape = 'disconnected', num_of_obj = 3, size = n))
    for n in [1000, 2197, 3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648]:
        Ps.append(PointSet(pf_shape = 'disconnected', num_of_obj = 4, size = n))
    for n in [1296, 2401, 4096, 6561, 10000]:
        Ps.append(PointSet(pf_shape = 'disconnected', num_of_obj = 5, size = n))
    for n in [1024, 3125, 7776]:
        Ps.append(PointSet(pf_shape = 'disconnected', num_of_obj = 6, size = n))
    """

    Ps = [
        PointSet(pf_shape = 'linear', num_of_obj = 2, size = 1000),
        PointSet(pf_shape = 'disconnected', num_of_obj = 2, size = 1000)
    ]

    Is = [
        Indicator(name = 'hv'),
        Indicator(name = 'epsilon'),
        Indicator(name = 'igd'),
        Indicator(name = 'igd+'),
        Indicator(name = 'r2'),
        Indicator(name = 'nr2'),
        Indicator(name = 'senergy')
    ]

    k = [100]

    As = [
        Selector(name = 'fils'),
        Selector(name = 'fils-nlist', nlist_size = 40),
        Selector(name = 'fils-rlist', rlist_size = 40),
        Selector(name = 'fils-rlist-nlist', nlist_size = 20, rlist_size = 20)
    ]

    id = range(1)

    issp_experiment(point_set = Ps, point_subset_size = k, indicator = Is, selector = As, run_id = id)
